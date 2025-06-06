# font

**Framework**: SceneKit  
**Kind**: property

The font that SceneKit uses to create geometry from the text.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var font: UIFont! { get set }
```

#### Discussion

If the text geometry’s [`string`](scntext/string.md) property is an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object, SceneKit uses this font to render the entire text. If the [`string`](scntext/string.md) property is an an [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) object, SceneKit uses this font for any portions of the string not containing style attributes.

The default font is Helvetica 36 point.

## See Also

- [var string: Any?](scntext/string.md)
  The string object whose text the geometry represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/font)*