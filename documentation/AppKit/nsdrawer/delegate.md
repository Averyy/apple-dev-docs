# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s delegate.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Drawers are deprecated; consider using NSSplitViewController

## Declaration

```swift
unowned(unsafe) var delegate: (any NSDrawerDelegate)? { get set }
```

```objc
@property (assign, nullable) id<NSDrawerDelegate> delegate;
```

## Discussion

You may find it useful to associate a delegate with a drawer, especially since drawers do not open and close instantly. A drawer’s delegate can better regulate drawer behavior.

## See Also

### Creating Drawers
- [init(contentSize: NSSize, preferredEdge: NSRectEdge)](./init%28contentsize,preferrededge%29.md)
  Creates a new drawer with the given size on the specified edge of the parent window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/delegate)*