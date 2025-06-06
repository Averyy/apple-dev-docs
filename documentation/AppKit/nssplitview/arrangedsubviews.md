# arrangedSubviews

**Framework**: AppKit  
**Kind**: property

The array of views that the split view arranges as its split panes.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var arrangedSubviews: [NSView] { get }
```

#### Discussion

This array contains a subset of the views in the split view’s [`subviews`](nsview/subviews.md) property. The views in this array may appear in a different order than in the [`subviews`](nsview/subviews.md) array.

If the value of [`arrangesAllSubviews`](nssplitview/arrangesallsubviews.md) is [`true`](https://developer.apple.com/documentation/swift/true), this array is identical to the [`subviews`](nsview/subviews.md) array.

## See Also

- [var arrangesAllSubviews: Bool](nssplitview/arrangesallsubviews.md)
  A Boolean value that determines whether the split view arranges all of its subviews as split panes.
- [func addArrangedSubview(NSView)](nssplitview/addarrangedsubview(_:).md)
  Adds a view as an arranged split pane.
- [func insertArrangedSubview(NSView, at: Int)](nssplitview/insertarrangedsubview(_:at:).md)
  Adds a view as an arranged split pane at the specified index.
- [func removeArrangedSubview(NSView)](nssplitview/removearrangedsubview(_:).md)
  Removes a view as an arranged split pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/arrangedsubviews)*