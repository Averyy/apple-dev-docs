# session(_:didFind:)

**Framework**: ShazamKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the query signature matches an item in the catalog.

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
optional func session(_ session: SHSession, didFind match: SHMatch)
```

```objc
- (void) session:(SHSession *) session didFindMatch:(SHMatch *) match;
```

## Parameters

- `session`: The session object that performs the match.
- `match`: The matching items from the catalog.

## See Also

### Handling matches
- [func session(SHSession, didNotFindMatchFor: SHSignature, error: (any Error)?)](./session%28_,didnotfindmatchfor,error%29.md)
  Tells the delegate that the query signature doesn’t match an item in the catalog, or that there’s an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsessiondelegate/session(_:didfind:))*