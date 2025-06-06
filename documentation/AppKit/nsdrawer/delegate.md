# delegate

**Framework**: AppKit  
**Kind**: property

The receiver’s delegate.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
unowned(unsafe) var delegate: (any NSDrawerDelegate)? { get set }
```

#### Discussion

You may find it useful to associate a delegate with a drawer, especially since drawers do not open and close instantly. A drawer’s delegate can better regulate drawer behavior.

## See Also

- [init(contentSize: NSSize, preferredEdge: NSRectEdge)](nsdrawer/init(contentsize:preferrededge:).md)
  Creates a new drawer with the given size on the specified edge of the parent window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/delegate)*