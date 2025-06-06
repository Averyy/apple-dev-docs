# metadata

**Framework**: HealthKit  
**Kind**: property

The metadata for this HealthKit object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var metadata: [String : Any]? { get }
```

#### Discussion

The metadata dictionary contains extra information describing this object. The dictionary’s keys are all [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects. The values can be [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects, [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects or [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate) objects. For a complete list of predefined metadata keys, see [`Metadata Keys`](metadata-keys.md).

Using predefined keys helps facilitate sharing data between apps; however, you are also encouraged to create your own, custom keys as needed to extend the HealthKit object’s capabilities.

You set an object’s metadata when you create the object by calling one of these methods (or a related method):

- [`init(type:quantity:start:end:metadata:)`](hkquantitysample/init(type:quantity:start:end:metadata:).md)
- [`init(type:value:start:end:metadata:)`](hkcategorysample/init(type:value:start:end:metadata:).md)
- [`init(type:start:end:objects:metadata:)`](hkcorrelation/init(type:start:end:objects:metadata:).md)
- [`init(activityType:start:end:duration:totalEnergyBurned:totalDistance:metadata:)`](hkworkout/init(activitytype:start:end:duration:totalenergyburned:totaldistance:metadata:).md)

## See Also

- [var uuid: UUID](hkobject/uuid.md)
  The universally unique identifier (UUID) for this HealthKit object.
- [var device: HKDevice?](hkobject/device.md)
  The device that generated the data for this object.
- [var sourceRevision: HKSourceRevision](hkobject/sourcerevision.md)
  The app or device that created this object.
- [var source: HKSource](hkobject/source.md)
  A HealthKit source, representing the app or device that created this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobject/metadata)*