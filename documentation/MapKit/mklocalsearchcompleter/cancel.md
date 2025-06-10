# cancel()

**Framework**: MapKit  
**Kind**: method

Cancels an in-progress search operation.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.4+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func cancel()
```

#### Discussion

If a search operation is in progress, this method attempts to cancel it. If cancellation is successful, the search completer doesn’t notify its delegate. If no search operation is in progress, this method does nothing.

## See Also

- [var isSearching: Bool](mklocalsearchcompleter/issearching.md)
  A Boolean value that indicates whether a search operation is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/cancel())*