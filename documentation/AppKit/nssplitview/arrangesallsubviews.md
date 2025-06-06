# arrangesAllSubviews

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether the split view arranges all of its subviews as split panes.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var arrangesAllSubviews: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the split view arranges all of its subviews automatically. The [`arrangedSubviews`](nssplitview/arrangedsubviews.md) array is identical to the split view’s [`subviews`](nsview/subviews.md) array, so any change to [`subviews`](nsview/subviews.md) reflects in the [`arrangedSubviews`](nssplitview/arrangedsubviews.md) array. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

If the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), you must explicitly add a view as an arranged subview to arrange it as a split pane. You add an arranged subview using [`addArrangedSubview(_:)`](nssplitview/addarrangedsubview(_:).md).

When you change the value of this property from [`true`](https://developer.apple.com/documentation/swift/true) to [`false`](https://developer.apple.com/documentation/swift/false), all existing subviews stay as arranged subviews in [`arrangedSubviews`](nssplitview/arrangedsubviews.md). When you change the value of this property from [`false`](https://developer.apple.com/documentation/swift/false) to [`true`](https://developer.apple.com/documentation/swift/true), all existing subviews become arranged subviews, and the value of the [`subviews`](nsview/subviews.md) array becomes the [`arrangedSubviews`](nssplitview/arrangedsubviews.md) array.

## See Also

- [var arrangedSubviews: [NSView]](nssplitview/arrangedsubviews.md)
  The array of views that the split view arranges as its split panes.
- [func addArrangedSubview(NSView)](nssplitview/addarrangedsubview(_:).md)
  Adds a view as an arranged split pane.
- [func insertArrangedSubview(NSView, at: Int)](nssplitview/insertarrangedsubview(_:at:).md)
  Adds a view as an arranged split pane at the specified index.
- [func removeArrangedSubview(NSView)](nssplitview/removearrangedsubview(_:).md)
  Removes a view as an arranged split pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/arrangesallsubviews)*