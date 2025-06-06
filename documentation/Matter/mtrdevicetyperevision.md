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
- [init?(coder: NSCoder)](mtrdevicetyperevision/init(coder:).md)
- [init?(deviceTypeStruct: MTRDescriptorClusterDeviceTypeStruct)](mtrdevicetyperevision/init(devicetypestruct:).md)
  Initializes the receiver based on the values in the specified struct.
### Instance Properties
- [var deviceTypeID: NSNumber](mtrdevicetyperevision/devicetypeid.md)
- [var deviceTypeRevision: NSNumber](mtrdevicetyperevision/devicetyperevision.md)
- [var typeInformation: MTRDeviceType?](mtrdevicetyperevision/typeinformation.md)
  Returns the MTRDeviceType corresponding to deviceTypeID, or nil if deviceTypeID does not represent a known device type.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicetyperevision)*