# delegate

**Framework**: AppKit  
**Kind**: property

The image’s delegate object.

**Availability**:
- macOS ?+

## Declaration

```swift
weak var delegate: (any NSImageDelegate)? { get set }
```

#### Discussion

By default, this property contains `nil`.

## See Also

- [protocol NSImageDelegate](nsimagedelegate.md)
  A set of optional methods that you can use to respond to drawing failures and manage incremental loads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/delegate)*