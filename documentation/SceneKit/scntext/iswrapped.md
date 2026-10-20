# isWrapped

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether SceneKit wraps long lines of text.

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
var isWrapped: Bool { get set }
```

```objc
@property (nonatomic, getter=isWrapped) BOOL wrapped;
```

#### Discussion

When you define a layout rectangle for the text using its [`containerFrame`](./containerframe.md) property, SceneKit uses the [`isWrapped`](./iswrapped.md) property to determine whether each line of text that is wider than the layout rectangle automatically wraps onto the next line.

The default value of this property is [`false`](../../Swift/false.md), specifying that long lines of text do not wrap. (If you specify a container frame, long lines of text extend beyond its width.)

## See Also

### Managing Text Layout
- [var containerFrame: CGRect](./containerframe.md)
  A rectangle specifying the area in which SceneKit should lay out the text.
- [var alignmentMode: String](./alignmentmode.md)
  A constant that specifies how SceneKit horizontally aligns each line of text within its container.
- [var truncationMode: String](./truncationmode.md)
  A constant that specifies how SceneKit truncates text that is too long to fit its container.
- [var textSize: CGSize](./textsize.md)
  The two-dimensional extent of the text after layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/iswrapped)*