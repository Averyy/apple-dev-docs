# string

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The string object whose text the geometry represents.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var string: Any? { get set }
```

```objc
@property (nonatomic, copy, nullable) id string;
```

## Discussion

You can supply text as an [`NSString`](../../Foundation/nsstring.md) or [`NSAttributedString`](../../Foundation/nsattributedstring.md) object. When you use an [`NSString`](../../Foundation/nsstring.md) object, the text geometry’s properties determine the style of the entire body of text. You can use an [`NSAttributedString`](../../Foundation/nsattributedstring.md) object to provide a body of text containing multiple styles, in which case the text geometry’s properties define the default style for portions of the string without style attributes.

The default value of this property is `nil`, which creates an empty text geometry.

## See Also

### Managing the Geometry’s Text Content
- [var font: UIFont!](./font.md)
  The font that SceneKit uses to create geometry from the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/string)*