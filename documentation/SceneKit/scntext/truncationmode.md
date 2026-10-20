# truncationMode

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A constant that specifies how SceneKit truncates text that is too long to fit its container.

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
var truncationMode: String { get set }
```

```objc
@property (nonatomic, copy) NSString * truncationMode;
```

#### Discussion

When you define a layout rectangle for the text using its [`containerFrame`](./containerframe.md) property, SceneKit uses the [`truncationMode`](./truncationmode.md) property to determine how to lay out text that does not fit in the layout rectangle. For possible values, see Truncation_modes in [`CATextLayer`](../../QuartzCore/catextlayer.md).

The default value of this property is [`none`](../../QuartzCore/catextlayertruncationmode/none.md), specifying that SceneKit should not truncate the text. If the [`isWrapped`](./iswrapped.md) property is [`true`](../../Swift/true.md), SceneKit continues to automatically wrap each line of text beyond the height of the layout rectangle. Otherwise, SceneKit does not display text that would extend beyond the layout rectangle.

## See Also

### Managing Text Layout
- [var containerFrame: CGRect](./containerframe.md)
  A rectangle specifying the area in which SceneKit should lay out the text.
- [var isWrapped: Bool](./iswrapped.md)
  A Boolean value that specifies whether SceneKit wraps long lines of text.
- [var alignmentMode: String](./alignmentmode.md)
  A constant that specifies how SceneKit horizontally aligns each line of text within its container.
- [var textSize: CGSize](./textsize.md)
  The two-dimensional extent of the text after layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/truncationmode)*