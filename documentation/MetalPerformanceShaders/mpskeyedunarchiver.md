# MPSKeyedUnarchiver

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [init?(device: any MTLDevice)](mpskeyedunarchiver/init(device:).md)
- [init(forReadingFrom: Data, device: any MTLDevice, error: NSErrorPointer)](mpskeyedunarchiver/init(forreadingfrom:device:error:).md)
- [init(forReadingFromData: Data, device: any MTLDevice, error: NSErrorPointer)](mpskeyedunarchiver/init(forreadingfromdata:device:error:).md)
- [init(forReadingWith: Data, device: any MTLDevice)](mpskeyedunarchiver/init(forreadingwith:device:).md)
- [init(forReadingWithData: Data, device: any MTLDevice)](mpskeyedunarchiver/init(forreadingwithdata:device:).md)
### Instance Methods
- [func mpsMTLDevice() -> any MTLDevice](mpskeyedunarchiver/mpsmtldevice.md)
### Type Methods
- [class func unarchiveObject(with: Data, device: any MTLDevice) -> Any?](mpskeyedunarchiver/unarchiveobject(with:device:).md)
- [class func unarchiveObject(withFile: String, device: any MTLDevice) -> Any?](mpskeyedunarchiver/unarchiveobject(withfile:device:).md)
- [class func unarchiveTopLevelObject(with: Data, device: any MTLDevice) throws -> Any](mpskeyedunarchiver/unarchivetoplevelobject(with:device:).md)
- [class func unarchivedObject(of: AnyClass, from: Data, device: any MTLDevice) throws -> Any](mpskeyedunarchiver/unarchivedobject(of:from:device:).md)
- [class func unarchivedObject(ofClasses: Set<AnyHashable>, from: Data, device: any MTLDevice) throws -> Any](mpskeyedunarchiver/unarchivedobject(ofclasses:from:device:).md)

## Relationships

### Inherits From
- [NSKeyedUnarchiver](../foundation/nskeyedunarchiver.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [MPSDeviceProvider](mpsdeviceprovider.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class NSKeyedArchiver](../foundation/nskeyedarchiver.md)
  An encoder that stores an object’s data to an archive referenced by keys.
- [protocol MPSDeviceProvider](mpsdeviceprovider.md)
  An interface that enables the setting of a Metal device for unarchived objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpskeyedunarchiver)*