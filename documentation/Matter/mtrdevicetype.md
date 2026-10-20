# MTRDeviceType

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRDeviceType : NSObject
```

## Topics

### Initializers
- [init?(forID: NSNumber)](./mtrdevicetype/init%28forid%29.md)
  Returns an MTRDeviceType for the given ID, if the ID is known.  Returns nil for unknown IDs.
### Instance Properties
- [var id: NSNumber](./mtrdevicetype/id.md)
  The identifier of the device type (32-bit unsigned integer).
- [var isUtility: Bool](./mtrdevicetype/isutility.md)
  Returns whether this is a utility device type.
- [var name: String](./mtrdevicetype/name.md)
  Returns the name of the device type.

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
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicetype)*