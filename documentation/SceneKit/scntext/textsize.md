# textSize

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The two-dimensional extent of the text after layout.

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
var textSize: CGSize { get }
```

```objc
@property (nonatomic, readonly) CGSize textSize;
```

## Discussion

This property reports the size of the smallest bounding rectangle containing the text.

This size does not necessarily match that of the layout rectangle specified by the [`containerFrame`](./containerframe.md) property. A long body of text may overflow the layout rectangle, depending on the values of the [`isWrapped`](./iswrapped.md) and [`truncationMode`](./truncationmode.md) properties, and a short string of text may fit in an area smaller than the layout rectangle.

## See Also

### Managing Text Layout
- [var containerFrame: CGRect](./containerframe.md)
  A rectangle specifying the area in which SceneKit should lay out the text.
- [var isWrapped: Bool](./iswrapped.md)
  A Boolean value that specifies whether SceneKit wraps long lines of text.
- [var alignmentMode: String](./alignmentmode.md)
  A constant that specifies how SceneKit horizontally aligns each line of text within its container.
- [var truncationMode: String](./truncationmode.md)
  A constant that specifies how SceneKit truncates text that is too long to fit its container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/textsize)*