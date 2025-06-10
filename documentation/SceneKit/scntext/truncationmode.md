# truncationMode

**Framework**: SceneKit  
**Kind**: property

A constant that specifies how SceneKit truncates text that is too long to fit its container.

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
var truncationMode: String { get set }
```

#### Discussion

When you define a layout rectangle for the text using its [`containerFrame`](scntext/containerframe.md) property, SceneKit uses the [`truncationMode`](scntext/truncationmode.md) property to determine how to lay out text that does not fit in the layout rectangle. For possible values, see Truncation_modes in [`CATextLayer`](https://developer.apple.com/documentation/QuartzCore/CATextLayer).

The default value of this property is [`none`](https://developer.apple.com/documentation/QuartzCore/CATextLayerTruncationMode/none), specifying that SceneKit should not truncate the text. If the [`isWrapped`](scntext/iswrapped.md) property is [`true`](https://developer.apple.com/documentation/swift/true), SceneKit continues to automatically wrap each line of text beyond the height of the layout rectangle. Otherwise, SceneKit does not display text that would extend beyond the layout rectangle.

## See Also

- [var containerFrame: CGRect](scntext/containerframe.md)
  A rectangle specifying the area in which SceneKit should lay out the text.
- [var isWrapped: Bool](scntext/iswrapped.md)
  A Boolean value that specifies whether SceneKit wraps long lines of text.
- [var alignmentMode: String](scntext/alignmentmode.md)
  A constant that specifies how SceneKit horizontally aligns each line of text within its container.
- [var textSize: CGSize](scntext/textsize.md)
  The two-dimensional extent of the text after layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/truncationmode)*