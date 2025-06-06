# session(_:didNotFindMatchFor:error:)

**Framework**: ShazamKit  
**Kind**: method

Tells the delegate that the query signature doesn’t match an item in the catalog, or that there’s an error.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
optional func session(_ session: SHSession, didNotFindMatchFor signature: SHSignature, error: (any Error)?)
```

## Mentions

- [Matching audio using the built-in microphone](matching-audio-using-the-built-in-microphone.md)

#### Discussion

You can retry the match if the error indicates an issue in communicating with the catalog server, such as [`SHError.Code.matchAttemptFailed`](sherror/code/matchattemptfailed.md).

## Parameters

- `session`: The session object that performs the match.
- `signature`: The query signature to use for the match.
- `error`: The error that occurs; otherwise,  , which indicates that there’s no match.

## See Also

- [func session(SHSession, didFind: SHMatch)](shsessiondelegate/session(_:didfind:).md)
  Tells the delegate that the query signature matches an item in the catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsessiondelegate/session(_:didnotfindmatchfor:error:))*