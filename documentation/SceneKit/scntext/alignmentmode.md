# alignmentMode

**Framework**: SceneKit  
**Kind**: property

A constant that specifies how SceneKit horizontally aligns each line of text within its container.

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
var alignmentMode: String { get set }
```

#### Discussion

When you define a layout rectangle for the text using its [`containerFrame`](scntext/containerframe.md) property, SceneKit uses the [`alignmentMode`](scntext/alignmentmode.md) property to determine where each line of text is placed horizontally relative to the layout rectangle. For possible values, see [`Horizontal alignment modes`](https://developer.apple.com/documentation/QuartzCore/horizontal-alignment-modes) in [`CATextLayer`](https://developer.apple.com/documentation/QuartzCore/CATextLayer).

The default value of this property is [`natural`](https://developer.apple.com/documentation/QuartzCore/CATextLayerAlignmentMode/natural), specifying that text is aligned relative to the default alignment of its script. (For example, left-to-right languages are left-aligned.)

## See Also

- [var containerFrame: CGRect](scntext/containerframe.md)
  A rectangle specifying the area in which SceneKit should lay out the text.
- [var isWrapped: Bool](scntext/iswrapped.md)
  A Boolean value that specifies whether SceneKit wraps long lines of text.
- [var truncationMode: String](scntext/truncationmode.md)
  A constant that specifies how SceneKit truncates text that is too long to fit its container.
- [var textSize: CGSize](scntext/textsize.md)
  The two-dimensional extent of the text after layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/alignmentmode)*