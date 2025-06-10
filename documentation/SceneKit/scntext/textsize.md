# textSize

**Framework**: SceneKit  
**Kind**: property

The two-dimensional extent of the text after layout.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var textSize: CGSize { get }
```

#### Discussion

This property reports the size of the smallest bounding rectangle containing the text.

This size does not necessarily match that of the layout rectangle specified by the [`containerFrame`](scntext/containerframe.md) property. A long body of text may overflow the layout rectangle, depending on the values of the [`isWrapped`](scntext/iswrapped.md) and [`truncationMode`](scntext/truncationmode.md) properties, and a short string of text may fit in an area smaller than the layout rectangle.

## See Also

- [var containerFrame: CGRect](scntext/containerframe.md)
  A rectangle specifying the area in which SceneKit should lay out the text.
- [var isWrapped: Bool](scntext/iswrapped.md)
  A Boolean value that specifies whether SceneKit wraps long lines of text.
- [var alignmentMode: String](scntext/alignmentmode.md)
  A constant that specifies how SceneKit horizontally aligns each line of text within its container.
- [var truncationMode: String](scntext/truncationmode.md)
  A constant that specifies how SceneKit truncates text that is too long to fit its container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/textsize)*