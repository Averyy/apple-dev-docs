# MPSKeyedUnarchiver

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A keyed archiver that supports Metal Performance Shaders kernel decoding.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSKeyedUnarchiver
```

```objc
@interface MPSKeyedUnarchiver : NSKeyedUnarchiver
```

## Topics

### Initializers
- [init?(device: any MTLDevice)](./mpskeyedunarchiver/init%28device%29.md)
- [init(forReadingFrom: Data, device: any MTLDevice, error: NSErrorPointer)](./mpskeyedunarchiver/init%28forreadingfrom,device,error%29.md)
- [init(forReadingFromData: Data, device: any MTLDevice, error: NSErrorPointer)](./mpskeyedunarchiver/init%28forreadingfromdata,device,error%29.md)
- [init(forReadingWith: Data, device: any MTLDevice)](./mpskeyedunarchiver/init%28forreadingwith,device%29.md)
- [init(forReadingWithData: Data, device: any MTLDevice)](./mpskeyedunarchiver/init%28forreadingwithdata,device%29.md)
### Instance Methods
- [func mpsMTLDevice() -> any MTLDevice](./mpskeyedunarchiver/mpsmtldevice%28%29.md)
### Type Methods
- [class func unarchiveObject(with: Data, device: any MTLDevice) -> Any?](./mpskeyedunarchiver/unarchiveobject%28with,device%29.md)
- [class func unarchiveObject(withFile: String, device: any MTLDevice) -> Any?](./mpskeyedunarchiver/unarchiveobject%28withfile,device%29.md)
- [class func unarchiveTopLevelObject(with: Data, device: any MTLDevice) throws -> Any](./mpskeyedunarchiver/unarchivetoplevelobject%28with,device%29.md)
- [class func unarchivedObject(of: AnyClass, from: Data, device: any MTLDevice) throws -> Any](./mpskeyedunarchiver/unarchivedobject%28of,from,device%29.md)
- [class func unarchivedObject(ofClasses: Set<AnyHashable>, from: Data, device: any MTLDevice) throws -> Any](./mpskeyedunarchiver/unarchivedobject%28ofclasses,from,device%29.md)

## Relationships

### Inherits From
- [NSKeyedUnarchiver](../Foundation/nskeyedunarchiver.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MPSDeviceProvider](./mpsdeviceprovider.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Keyed Archivers
- [class NSKeyedArchiver](../Foundation/nskeyedarchiver.md)
  An encoder that stores an object’s data to an archive referenced by keys.
- [protocol MPSDeviceProvider](./mpsdeviceprovider.md)
  An interface that enables the setting of a Metal device for unarchived objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpskeyedunarchiver)*