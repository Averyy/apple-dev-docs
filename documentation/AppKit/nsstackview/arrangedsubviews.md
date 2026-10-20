# arrangedSubviews

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The array of views arranged by the stack view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var arrangedSubviews: [NSView] { get }
```

```objc
@property (copy, readonly) NSArray<__kindof NSView *> * arrangedSubviews;
```

#### Discussion

The stack view ensures that the contents of this array are always a subset of its [`subviews`](../nsview/subviews.md) array.

## See Also

### Managing the Arranged Subviews
- [func addArrangedSubview(NSView)](./addarrangedsubview%28_%29.md)
  Adds the specified view to the end of the arranged subviews list.
- [func insertArrangedSubview(NSView, at: Int)](./insertarrangedsubview%28_,at%29.md)
  Adds the provided view to the array of arranged subviews at the specified index.
- [func removeArrangedSubview(NSView)](./removearrangedsubview%28_%29.md)
  Removes the provided view from the stack’s array of arranged subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/arrangedsubviews)*