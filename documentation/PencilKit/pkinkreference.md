# PKInkReference

**Framework**: PencilKit  
**Kind**: class

Provides a description of the creation and rendering of marks on a canvas.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PKInkReference
```

## Topics

### Creating an ink
- [init(inkType: __PKInkType, color: UIColor)](pkinkreference/init(inktype:color:).md)
  Create a new ink, specifying its type, color.
### Getting the ink attributes
- [var color: UIColor](pkinkreference/color.md)
  The base color for this ink.
- [var inkType: __PKInkType](pkinkreference/inktype.md)
  The type of ink, such as pen or pencil, as defined in the [`PKInkType`](pkinktype.md) enumeration.
### Supporting backward compatibility
- [var requiredContentVersion: PKContentVersion](pkinkreference/requiredcontentversion.md)
  The version of PencilKit necessary to use the ink.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkreference)*