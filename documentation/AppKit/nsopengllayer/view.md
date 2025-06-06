# view

**Framework**: AppKit  
**Kind**: property

Returns the view associated with the layer.

**Availability**:
- macOS 10.6+

## Declaration

```swift
weak var view: NSView? { get set }
```

#### Discussion

Subclasses shouldn’t invoke setView:, but can override it if desired to intercept the layer’s association to, or dissociation from, a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopengllayer/view)*