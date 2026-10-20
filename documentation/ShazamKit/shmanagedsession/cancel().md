# cancel()

**Framework**: ShazamKit  
**Kind**: method  
**Role**: Instance Method

Cancels the currently running match attempt.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
final func cancel()
```

## See Also

### Returning queries
- [func result() async -> SHSession.Result](./result%28%29.md)
  Performs an asynchronous match with a single signature.
- [var results: SHSession.Results](./results.md)
  The results as an asynchronous sequence of matches.
- [func prepare() async](./prepare%28%29.md)
  Preallocates the resources needed for a match, which increases the responsiveness of matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmanagedsession/cancel())*