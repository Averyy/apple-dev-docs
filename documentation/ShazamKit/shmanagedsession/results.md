# results

**Framework**: ShazamKit  
**Kind**: property

The results as an asynchronous sequence of matches.

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
final var results: SHSession.Results { get }
```

#### Discussion

This session continues to return results until the sequence is exhausted or the app calls [`cancel()`](shmanagedsession/cancel().md).

## See Also

- [func result() async -> SHSession.Result](shmanagedsession/result.md)
  Performs an asynchronous match with a single signature.
- [func cancel()](shmanagedsession/cancel.md)
  Cancels the currently running match attempt.
- [func prepare() async](shmanagedsession/prepare.md)
  Preallocates the resources needed for a match, which increases the responsiveness of matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmanagedsession/results)*