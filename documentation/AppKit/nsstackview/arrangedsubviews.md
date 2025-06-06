# arrangedSubviews

**Framework**: AppKit  
**Kind**: property

The array of views arranged by the stack view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var arrangedSubviews: [NSView] { get }
```

#### Discussion

The stack view ensures that the contents of this array are always a subset of its [`subviews`](nsview/subviews.md) array.

## See Also

- [func addArrangedSubview(NSView)](nsstackview/addarrangedsubview(_:).md)
  Adds the specified view to the end of the arranged subviews list.
- [func insertArrangedSubview(NSView, at: Int)](nsstackview/insertarrangedsubview(_:at:).md)
  Adds the provided view to the array of arranged subviews at the specified index.
- [func removeArrangedSubview(NSView)](nsstackview/removearrangedsubview(_:).md)
  Removes the provided view from the stack’s array of arranged subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/arrangedsubviews)*