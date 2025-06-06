# result(from:)

**Framework**: ShazamKit  
**Kind**: method

Performs an asynchronous match with a signature you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func result(from signature: SHSignature) async -> SHSession.Result
```

#### Return Value

A [`SHSession.Result`](shsession/result.md) enum that indicates the result.

## Parameters

- `signature`: The signature to match.

## See Also

- [SHSession.Result](shsession/result.md)
  Identifies the result from an asynchronous sequence result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsession/result(from:))*