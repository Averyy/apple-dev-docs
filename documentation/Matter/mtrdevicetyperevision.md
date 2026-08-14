# MTRDeviceTypeRevision

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
class MTRDeviceTypeRevision
```

## Topics

### Initializers
- [init?(deviceTypeID: NSNumber, revision: NSNumber)](mtrdevicetyperevision/init(devicetypeid:revision:).md)
- [init?(deviceTypeStruct: MTRDescriptorClusterDeviceTypeStruct)](mtrdevicetyperevision/init(devicetypestruct:).md)
  Initializes the receiver based on the values in the specified struct.
### Instance Properties
- [var deviceTypeID: NSNumber](mtrdevicetyperevision/devicetypeid.md)
- [var deviceTypeRevision: NSNumber](mtrdevicetyperevision/devicetyperevision.md)
- [var typeInformation: MTRDeviceType?](mtrdevicetyperevision/typeinformation.md)
  Returns the MTRDeviceType corresponding to deviceTypeID, or nil if deviceTypeID does not represent a known device type.
### Default Implementations
- [MTRDeviceTypeRevision Implementations](mtrdevicetyperevision/mtrdevicetyperevision-implementations.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicetyperevision)*