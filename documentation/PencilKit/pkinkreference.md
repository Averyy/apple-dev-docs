# PKInkReference

**Framework**: PencilKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface PKInk : NSObject
```

## Topics

### Creating an ink
- [init(inkType: __PKInkType, color: UIColor)](./pkinkreference/init%28inktype,color%29.md)
  Create a new ink, specifying its type, color.
### Getting the ink attributes
- [var color: UIColor](./pkinkreference/color.md)
  The base color for this ink.
- [var inkType: __PKInkType](./pkinkreference/inktype.md)
  The type of ink, such as pen or pencil, as defined in the [`PKInkType`](./pkinktype.md) enumeration.
### Supporting backward compatibility
- [var requiredContentVersion: PKContentVersion](./pkinkreference/requiredcontentversion.md)
  The version of PencilKit necessary to use the ink.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkreference)*