# usesFindBar

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to use the find bar for this text view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var usesFindBar: Bool { get set }
```

```objc
@property BOOL usesFindBar;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the find bar is used for this text view; otherwise [`false`](../../Swift/false.md). See [`NSTextFinder`](../nstextfinder.md) for information about the find bar.

A text view can use either a find panel or a find bar. If [`usesFindBar`](./usesfindbar.md) is set to [`true`](../../Swift/true.md),  [`usesFindPanel`](./usesfindpanel.md) is set to [`false`](../../Swift/false.md) and vice versa.

## See Also

### Related Documentation
- [var usesFindPanel: Bool](./usesfindpanel.md)
  A Boolean value that indicates whether the receiver allows for a find panel.
### Using the Find Bar
- [var isIncrementalSearchingEnabled: Bool](./isincrementalsearchingenabled.md)
  A Boolean value that indicates whether incremental searching is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/usesfindbar)*