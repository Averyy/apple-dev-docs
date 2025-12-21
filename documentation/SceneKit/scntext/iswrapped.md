# isWrapped

**Framework**: SceneKit  
**Kind**: property

A Boolean value that specifies whether SceneKit wraps long lines of text.

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
var isWrapped: Bool { get set }
```

#### Discussion

When you define a layout rectangle for the text using its [`containerFrame`](scntext/containerframe.md) property, SceneKit uses the [`isWrapped`](scntext/iswrapped.md) property to determine whether each line of text that is wider than the layout rectangle automatically wraps onto the next line.

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), specifying that long lines of text do not wrap. (If you specify a container frame, long lines of text extend beyond its width.)

## See Also

- [var containerFrame: CGRect](scntext/containerframe.md)
  A rectangle specifying the area in which SceneKit should lay out the text.
- [var alignmentMode: String](scntext/alignmentmode.md)
  A constant that specifies how SceneKit horizontally aligns each line of text within its container.
- [var truncationMode: String](scntext/truncationmode.md)
  A constant that specifies how SceneKit truncates text that is too long to fit its container.
- [var textSize: CGSize](scntext/textsize.md)
  The two-dimensional extent of the text after layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/iswrapped)*