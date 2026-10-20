# alignmentMode

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A constant that specifies how SceneKit horizontally aligns each line of text within its container.

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
var alignmentMode: String { get set }
```

```objc
@property (nonatomic, copy) NSString * alignmentMode;
```

#### Discussion

When you define a layout rectangle for the text using its [`containerFrame`](./containerframe.md) property, SceneKit uses the [`alignmentMode`](./alignmentmode.md) property to determine where each line of text is placed horizontally relative to the layout rectangle. For possible values, see [Horizontal alignment modes](../../QuartzCore/horizontal-alignment-modes.md) in [`CATextLayer`](../../QuartzCore/catextlayer.md).

The default value of this property is [`natural`](../../QuartzCore/catextlayeralignmentmode/natural.md), specifying that text is aligned relative to the default alignment of its script. (For example, left-to-right languages are left-aligned.)

## See Also

### Managing Text Layout
- [var containerFrame: CGRect](./containerframe.md)
  A rectangle specifying the area in which SceneKit should lay out the text.
- [var isWrapped: Bool](./iswrapped.md)
  A Boolean value that specifies whether SceneKit wraps long lines of text.
- [var truncationMode: String](./truncationmode.md)
  A constant that specifies how SceneKit truncates text that is too long to fit its container.
- [var textSize: CGSize](./textsize.md)
  The two-dimensional extent of the text after layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/alignmentmode)*