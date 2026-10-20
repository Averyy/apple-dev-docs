# MTRDeviceTypeRevision

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRDeviceTypeRevision : NSObject
```

## Topics

### Initializers
- [init?(deviceTypeID: NSNumber, revision: NSNumber)](./mtrdevicetyperevision/init%28devicetypeid,revision%29.md)
- [init?(deviceTypeStruct: MTRDescriptorClusterDeviceTypeStruct)](./mtrdevicetyperevision/init%28devicetypestruct%29.md)
  Initializes the receiver based on the values in the specified struct.
### Instance Properties
- [var deviceTypeID: NSNumber](./mtrdevicetyperevision/devicetypeid.md)
- [var deviceTypeRevision: NSNumber](./mtrdevicetyperevision/devicetyperevision.md)
- [var typeInformation: MTRDeviceType?](./mtrdevicetyperevision/typeinformation.md)
  Returns the MTRDeviceType corresponding to deviceTypeID, or nil if deviceTypeID does not represent a known device type.
### Default Implementations
- [MTRDeviceTypeRevision Implementations](./mtrdevicetyperevision/mtrdevicetyperevision-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicetyperevision)*