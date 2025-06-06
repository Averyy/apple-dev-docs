# Getting raw gyroscope events

**Framework**: Core Motion

Retrieve data from the onboard gyroscopes.

#### Overview

A gyroscope measures the rate at which a device rotates around a spatial axis. Many iOS devices have a three-axis gyroscope, which delivers rotation values in each of the three axes shown in the next illustration. Rotation values are measured in radians per second around the given axis. Rotation values may be positive or negative depending on the direction of rotation.

![Gyroscopes measure the rotation rate around the x, y, and z axes](https://docs-assets.developer.apple.com/published/cd1feafe8399d86e120bf5f723a12459/media-2904021%402x.png)

You access the raw gyroscope data using the classes of the Core Motion framework. Specifically, the [`CMMotionManager`](cmmotionmanager.md) class provides the interfaces for enabling the gyroscope hardware. When enabling the hardware, choose the interfaces that are best suited for your app. You can pull the gyroscope data only when you need it, or you can ask the framework to push updates to your app at regular intervals. Each technique involves different configuration steps and has a different use case.

> ❗ **Important**:  If your app relies on the presence of gyroscope hardware, configure the `UIRequiredDeviceCapabilities` key of its `Info.plist` file with the `gyroscope` value. For more information about the meaning of this key, see [`Information Property List Key Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/).

 If your app relies on the presence of gyroscope hardware, configure the `UIRequiredDeviceCapabilities` key of its `Info.plist` file with the `gyroscope` value. For more information about the meaning of this key, see [`Information Property List Key Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/).

The raw rotation rate data delivered by the gyroscope interfaces may be biased by other factors such as temperature. If your app requires unbiased rotation values, use the device-motion interfaces instead. The device-motion interfaces use special algorithms to remove any bias and deliver more precise rotation values. For more information, see [`Getting processed device-motion data`](getting-processed-device-motion-data.md).

For information about the coordinate axes of different device types, see [`CMMotionManager`](cmmotionmanager.md).

##### Check for the Availability of Gyroscope Data

Gyroscope data might be unavailable for a variety of reasons, so verify that the data is available before you try to obtain it. Check the value of the [`isGyroAvailable`](cmmotionmanager/isgyroavailable.md) property of `CMMotionManager` and make sure it’s `true`. If it’s `false`, starting updates doesn’t deliver any data to your app.

> ❗ **Important**:  In visionOS, gyroscope data is available only when your app has an open immersive space. For more information, see [`ImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/ImmersiveSpace).

 In visionOS, gyroscope data is available only when your app has an open immersive space. For more information, see [`ImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/ImmersiveSpace).

##### Get Gyroscope Data Only When You Need It

For apps that process gyroscope data on their own schedule, such as games, use the [`startGyroUpdates()`](cmmotionmanager/startgyroupdates().md) method of [`CMMotionManager`](cmmotionmanager.md) to start the delivery of rotation data. When you call this method, the system enables the gyroscope hardware and begins updating the [`gyroData`](cmmotionmanager/gyrodata.md) property of your [`CMMotionManager`](cmmotionmanager.md) object. However, the system does not notify you when it updates that property. You must explicitly check the value of the property when you need the rotation data.

Before you start the delivery of gyroscope updates, specify an update frequency by assigning a value to the [`gyroUpdateInterval`](cmmotionmanager/gyroupdateinterval.md) property. The maximum frequency at which you can request updates is hardware-dependent but is usually at least 100 Hz. If you request a frequency that is greater than what the hardware supports, Core Motion uses the supported maximum instead.

The next example shows a method that configures gyroscope updates to occur 50 times per second. The method then configures a timer to fetch those updates at the same frequency and do something with the data. You could configure the timer to fire at a lower frequency, but doing so would waste power by causing the hardware to generate more updates than were actually used.

```swift
func startGyros() {
   if motion.isGyroAvailable {
      self.motion.gyroUpdateInterval = 1.0 / 50.0
      self.motion.startGyroUpdates()

      // Configure a timer to fetch the accelerometer data.
      self.timer = Timer(fire: Date(), interval: (1.0/50.0), 
             repeats: true, block: { (timer) in
         // Get the gyro data.
         if let data = self.motion.gyroData {
            let x = data.rotationRate.x
            let y = data.rotationRate.y
            let z = data.rotationRate.z

            // Use the gyroscope data in your app. 
         }
      })

      // Add the timer to the current run loop.
      RunLoop.current.add(self.timer!, forMode: .defaultRunLoopMode)
   }
}

func stopGyros() {
   if self.timer != nil {
      self.timer?.invalidate()
      self.timer = nil

      self.motion.stopGyroUpdates()
   }
}
```

##### Process a Steady Stream of Gyroscope Updates

When you want to capture all of the gyroscope data, perhaps so you can analyze it for movement patterns, use the [`startGyroUpdates(to:withHandler:)`](cmmotionmanager/startgyroupdates(to:withhandler:).md) method of [`CMMotionManager`](cmmotionmanager.md). This method pushes each new set of rotation values to your app by executing your handler block on the specified queue. The queueing of these blocks ensures that your app receives all of the gyroscope data, even if your app becomes busy and is unable to process updates for a brief period of time.

Before you start the delivery of gyroscope updates, specify an update frequency by assigning a value to the [`gyroUpdateInterval`](cmmotionmanager/gyroupdateinterval.md) property. The maximum frequency at which you can request updates is hardware-dependent but is usually at least 100 Hz. If you request a frequency that is greater than what the hardware supports, Core Motion uses the supported maximum instead.

The next example shows a method from the [`MotionGraphs`](https://developer.apple.comhttps://developer.apple.com/library/archive/samplecode/MotionGraphs/Introduction/Intro.html#//apple_ref/doc/uid/DTS40012333) sample code project, which you can examine for more context. The app displays a real-time graph of rotation data from the onboard gyroscopes. The user configures the update frequency for the gyroscopes using a slider, the changing of which results in a call to the `startUpdatesWithSliderValue:` method shown in the example. This method restarts the gyroscope updates with the new frequency. Each time a new sample is received, the specified block is queued on the main thread. That block updates the app’s graph view and labels with the new rotation values.

```objc
static const NSTimeInterval gyroMin = 0.01;
- (void)startUpdatesWithSliderValue:(int)sliderValue {
   // Determine the update interval
   NSTimeInterval delta = 0.005;
   NSTimeInterval updateInterval = gyroMin + delta * sliderValue;

   // Create a CMMotionManager
   CMMotionManager *mManager = [(APLAppDelegate *)
            [[UIApplication sharedApplication] delegate] sharedManager];
   APLGyroGraphViewController * __weak weakSelf = self;

   // Check whether the gyroscope is available
   if ([mManager isGyroAvailable] == YES) {
      // Assign the update interval to the motion manager
      [mManager setGyroUpdateInterval:updateInterval];
      [mManager startGyroUpdatesToQueue:[NSOperationQueue mainQueue] 
               withHandler:^(CMGyroData *gyroData, NSError *error) {
         [weakSelf.graphView addX:gyroData.rotationRate.x 
                  y:gyroData.rotationRate.y 
                  z:gyroData.rotationRate.z];
         [weakSelf setLabelValueX:gyroData.rotationRate.x 
                  y:gyroData.rotationRate.y 
                  z:gyroData.rotationRate.z];
      }];
   }
   self.updateIntervalLabel.text = [NSString stringWithFormat:@"%f", updateInterval];
}
- (void)stopUpdates{
   CMMotionManager *mManager = [(APLAppDelegate *)
            [[UIApplication sharedApplication] delegate] sharedManager];
   if ([mManager isGyroActive] == YES) {
      [mManager stopGyroUpdates];
   }
}
```

## See Also

- [class CMGyroData](cmgyrodata.md)
  A single measurement of the device’s rotation rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events)*