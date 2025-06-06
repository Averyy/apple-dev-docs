# prepareForReuse()

**Framework**: AppKit  
**Kind**: method

Restores the view to an initial state so that it can be reused.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func prepareForReuse()
```

#### Discussion

The default implementation of this method sets the view’s alpha to `1.0` and its hidden state to [`false`](https://developer.apple.com/documentation/swift/false). Subclasses can override this method and use it to return the view to its initial state. Subclasses should call `super` at some point in their implementation.

This method offers a way to reset a view to some initial state so that it can be reused. For example, the [`NSTableView`](nstableview.md) class uses it to prepare views for reuse and thereby avoid the expense of creating new views as they scroll into view. If you implement a view-reuse system in your own code, you can call this method from your own code prior to reusing them.

## See Also

- [init(frame: NSRect)](nsview/init(frame:).md)
  Initializes and returns a newly allocated `NSView` object with a specified frame rectangle.
- [init?(coder: NSCoder)](nsview/init(coder:).md)
  Initializes a view using from data in the specified coder object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/prepareforreuse())*