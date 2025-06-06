# string

**Framework**: SceneKit  
**Kind**: property

The string object whose text the geometry represents.

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
var string: Any? { get set }
```

#### Discussion

You can supply text as an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) or [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) object. When you use an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object, the text geometry’s properties determine the style of the entire body of text. You can use an [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) object to provide a body of text containing multiple styles, in which case the text geometry’s properties define the default style for portions of the string without style attributes.

The default value of this property is `nil`, which creates an empty text geometry.

## See Also

- [var font: UIFont!](scntext/font.md)
  The font that SceneKit uses to create geometry from the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/string)*