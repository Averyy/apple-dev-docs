# MTRDeviceType

**Framework**: Matter  
**Kind**: class

Meta-data about a device type defined in the Matter specification.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
class MTRDeviceType
```

## Topics

### Initializers
- [init?(forID: NSNumber)](mtrdevicetype/init(forid:).md)
  Returns an MTRDeviceType for the given ID, if the ID is known.  Returns nil for unknown IDs.
### Instance Properties
- [var id: NSNumber](mtrdevicetype/id.md)
  The identifier of the device type (32-bit unsigned integer).
- [var isUtility: Bool](mtrdevicetype/isutility.md)
  Returns whether this is a utility device type.
- [var name: String](mtrdevicetype/name.md)
  Returns the name of the device type.

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
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicetype)*