# delegate

**Framework**: AppKit  
**Kind**: property

The object that acts as the delegate of the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
weak var delegate: (any NSScrubberDelegate)? { get set }
```

## See Also

- [var dataSource: (any NSScrubberDataSource)?](nsscrubber/datasource.md)
  The object that provides the data for the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/delegate)*