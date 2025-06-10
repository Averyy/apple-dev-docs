# Getting processed device-motion data

**Framework**: Core Motion

Retrieve motion data that the system processed to remove environmental bias, such as the effects of gravity.

#### Overview

The Core Motion framework gives you access to the raw data from many different types of hardware sensors, including accelerometers, gyroscopes, and magnetometers. While the raw data is useful, it sometimes contains additional information you don’t need. For example, the raw accelerometer data contains both the acceleration caused by gravity and by the device’s motion. To get only the device-specific acceleration, you must remove the gravitational acceleration from the raw data values. The removal of this data requires additional information and extra processing time.

To make it easier to get the data you want, the device-motion service processes the raw data and makes the following values available:

- The device’s attitude (or orientation) in three-dimensional space
- The unbiased rotation rate of the device
- The current gravity vector
- The device-specific acceleration (without gravity)
- The current magnetic field vector

The device-motion service combines information from multiple sensors to provide the listed results. Device-motion services are available from [`CMMotionManager`](cmmotionmanager.md), [`CMHeadphoneMotionManager`](cmheadphonemotionmanager.md), and [`CMBatchedSensorManager`](cmbatchedsensormanager.md). If your app can’t function without accelerometer or gyroscope data, update your app’s list of required device capabilities to include that hardware. For more information about specifying required device capabilities, see [`UIRequiredDeviceCapabilities`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIRequiredDeviceCapabilities).

##### Check for the Availability of Motion Data

Device-motion data might be unavailable for a variety of reasons, so verify that the service is available before you try to start it. Check the value of the [`isDeviceMotionAvailable`](cmmotionmanager/isdevicemotionavailable.md) property of `CMMotionManager` and make sure it’s `true`. If it’s `false`, starting the service doesn’t deliver any data to your app.

> ❗ **Important**:  In visionOS, device-motion data is available only when your app has an open immersive space. For more information, see [`ImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/ImmersiveSpace).

##### Choose a Frame of Reference for Interpreting Attitude Data

The attitude of a device refers to the amount of rotation around each of the device’s axes. The device-motion service reports attitude values relative to a known orientation of the device, also known as the device’s frame of reference. When you start the device-motion service, you specify which frame of reference you want Core Motion to use.

The default frame of reference is [`xArbitraryZVertical`](cmattitudereferenceframe/xarbitraryzvertical.md), which places the z-axis perpendicular to the ground and matches the x- and y-axes to the device’s current orientation in space. Use this option or the [`xArbitraryCorrectedZVertical`](cmattitudereferenceframe/xarbitrarycorrectedzvertical.md) option to measure changes relative to the device’s initial starting position. For example, a golf swing analysis app might use this frame of reference to measure a person’s golf swing. For compass or navigation apps, choose the [`xMagneticNorthZVertical`](cmattitudereferenceframe/xmagneticnorthzvertical.md) or [`xTrueNorthZVertical`](cmattitudereferenceframe/xtruenorthzvertical.md) frames of reference, which report the device’s orientation relative to specific magnetic and true north, respectively.

Specify the reference frame you want when you start the device-motion service. The `CMMotionManager` object stores your chosen frame of reference in its [`attitudeReferenceFrame`](cmmotionmanager/attitudereferenceframe.md) property, and makes it the default choice.

When a device’s orientation matches the frame of reference’s orientation, the [`roll`](cmattitude/roll.md), [`pitch`](cmattitude/pitch.md), and [`yaw`](cmattitude/yaw.md) rotation values of a reported `CMAttitude` contain the value `0`. As a person rotates the device, the roll, pitch, and yaw values reflect the amount of rotation (in radians) relative to the frame of reference. The following figure shows how to interpret these values around each axis. Rotation values are in the range -π to π.

![Gyroscopes measure the rotation rate around the x, y, and z axes](https://docs-assets.developer.apple.com/published/64b92fc751671c47e15435b373ffc1bf/media-4251993%402x.png)

For information about the coordinate axes of different device types, see [`CMMotionManager`](cmmotionmanager.md) or [`CMHeadphoneMotionManager`](cmheadphonemotionmanager.md).

##### Start Device Motion Updates

To start collecting device-motion data, create a `CMMotionManager` object and call one of the appropriate methods. Core Motion offers two options for processing device-motion updates:

- Process a steady stream of updates using a closure.
- Process updates when you want them.

Both options require you to specify the frequency of updates from the system using the [`deviceMotionUpdateInterval`](cmmotionmanager/devicemotionupdateinterval.md) property of your `CMMotionManager` type. The maximum update frequency is hardware dependent, but is usually at least 100 Hz. If you specify an update frequency greater than what the hardware supports, Core Motion uses the maximum frequency instead.

The following example configures the device-motion service to deliver updates 50 times per second, and to deliver attitude data relative to magnetic north. When starting device motion without a closure, it’s your responsibility to check the [`deviceMotion`](cmmotionmanager/devicemotion.md) property of your `CMMotionManager` at regular intervals. This example sets up a timer to check the value of the property and apply the latest data to the app’s content:

```swift
func startDeviceMotion() {
    if motion.isDeviceMotionAvailable {
        self.motion.deviceMotionUpdateInterval = 1.0 / 50.0
        self.motion.showsDeviceMovementDisplay = true
        self.motion.startDeviceMotionUpdates(using: .xMagneticNorthZVertical)
        
        // Configure a timer to fetch the motion data.
        self.timer = Timer(fire: Date(), interval: (1.0 / 50.0), repeats: true,
                           block: { (timer) in
                            if let data = self.motion.deviceMotion {
                                // Get the attitude relative to the magnetic north reference frame.
                                let x = data.attitude.pitch
                                let y = data.attitude.roll
                                let z = data.attitude.yaw
                                
                                // Use the motion data in your app.
                            }
        })
        
        // Add the timer to the current run loop.
        RunLoop.current.add(self.timer!, forMode: RunLoop.Mode.default)
    }
}
```

To process a steady stream of events, start the device-motion services using an [`OperationQueue`](https://developer.apple.com/documentation/Foundation/OperationQueue) object and a closure of type [`CMDeviceMotionHandler`](cmdevicemotionhandler.md). Each time Core Motion receives a new data value, it runs your closure on the operation queue. Each new data value comes with a [`timestamp`](cmlogitem/timestamp.md) value, which you can use to verify the timeliness of the data and discard data that’s older than a certain threshold. The following example uses an operation queue to process 60 updates per second:

```swift
func startQueuedUpdates() {
   if motion.isDeviceMotionAvailable {
      self.motion.deviceMotionUpdateInterval = 1.0 / 60.0
      self.motion.showsDeviceMovementDisplay = true
      self.motion.startDeviceMotionUpdates(using: .xMagneticNorthZVertical, 
               to: self.queue, withHandler: { (data, error) in
         // Make sure the data is valid before accessing it.
         if let validData = data {
            // Get the attitude relative to the magnetic north reference frame. 
            let roll = validData.attitude.roll
            let pitch = validData.attitude.pitch
            let yaw = validData.attitude.yaw

            // Use the motion data in your app.
         }
      })
   }
}

```

##### Stop Device Motion Updates

To minimize the impact on a device’s battery life, always call the [`stopDeviceMotionUpdates()`](cmmotionmanager/stopdevicemotionupdates().md) method of your [`CMMotionManager`](cmmotionmanager.md) object when you no longer need motion data. The device-motion service captures motion data using special hardware, and running this hardware consumes additional power. In particular, stop services:

- When your app deactivates or enters the background
- When the person stops interacting with the feature that requires motion data
- As soon as your app has all the motion data it needs

If your app doesn’t require constant motion updates, start the device-motion service, fetch the data you need, and stop the service immediately. Don’t leave the service running any longer than necessary.

## See Also

- [class CMDeviceMotion](cmdevicemotion.md)
  Encapsulated measurements of the attitude, rotation rate, and acceleration of a device.
- [class CMAttitude](cmattitude.md)
  The device’s orientation relative to a known frame of reference at a point in time.
- [struct CMAttitudeReferenceFrame](cmattitudereferenceframe.md)
  Constants that indicate the frame of reference for attitude-related motion data.
- [class CMHeadphoneMotionManager](cmheadphonemotionmanager.md)
  An object that starts and manages headphone motion services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)*