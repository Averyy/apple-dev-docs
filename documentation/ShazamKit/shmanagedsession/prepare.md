# prepare()

**Framework**: ShazamKit  
**Kind**: method

Preallocates the resources needed for a match, which increases the responsiveness of matches.

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
final func prepare() async
```

## See Also

- [func result() async -> SHSession.Result](shmanagedsession/result.md)
  Performs an asynchronous match with a single signature.
- [var results: SHSession.Results](shmanagedsession/results.md)
  The results as an asynchronous sequence of matches.
- [func cancel()](shmanagedsession/cancel.md)
  Cancels the currently running match attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmanagedsession/prepare())*