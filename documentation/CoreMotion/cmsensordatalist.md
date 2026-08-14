# CMSensorDataList

**Framework**: Core Motion  
**Kind**: class

A list of the accelerometer data recorded by the system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
class CMSensorDataList
```

#### Overview

You do not create instances of this class directly. Instead, you receive one as the result of a query for accelerometer data from a [`CMSensorRecorder`](cmsensorrecorder.md) object.

You use a sensor data list object to enumerate over the accelerometer data as shown in the following example:

```objc
-(void)processSamplesFromDate:(NSDate*)start toDate:(NSDate)end {
   CMSensorRecorder* recorder = [[CMSensorRecorder alloc] init];
   CMSensorDataList* list = [recorder accelerometerDataFrom:start to:end];
 
   for (CMRecordedAccelerometerData* data in list) {
      // Process the data.
      NSLog(@"Sample: (%f, %f, %f)", data.acceleration.x,
              data.acceleration.y, data.acceleration.z);
   }
}
```

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSFastEnumeration](../foundation/nsfastenumeration.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Getting raw accelerometer events](getting-raw-accelerometer-events.md)
  Retrieve data from the onboard accelerometers.
- [class CMAccelerometerData](cmaccelerometerdata.md)
  A data sample from the device’s three accelerometers.
- [class CMRecordedAccelerometerData](cmrecordedaccelerometerdata.md)
  A single piece of accelerometer data that was recorded by the device.
- [class CMSensorRecorder](cmsensorrecorder.md)
  An object that gathers and retrieves accelerometer data from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmsensordatalist)*