# font

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The font that SceneKit uses to create geometry from the text.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
var font: UIFont! { get set }
```

*macOS*

```swift
var font: NSFont! { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, retain, null_resettable) UIFont * font;
```

*macOS*

```objc
@property (nonatomic, retain, null_resettable) NSFont * font;
```

## Discussion

If the text geometry’s [`string`](./string.md) property is an [`NSString`](../../Foundation/nsstring.md) object, SceneKit uses this font to render the entire text. If the [`string`](./string.md) property is an an [`NSAttributedString`](../../Foundation/nsattributedstring.md) object, SceneKit uses this font for any portions of the string not containing style attributes.

The default font is Helvetica 36 point.

## See Also

### Managing the Geometry’s Text Content
- [var string: Any?](./string.md)
  The string object whose text the geometry represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/font)*