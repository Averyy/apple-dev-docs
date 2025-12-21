# cancel()

**Framework**: CryptoTokenKit  
**Kind**: method

Attempts to cancel an interaction started by calling [`run(reply:)`](tksmartcarduserinteraction/run(reply:).md). For certain interactions, cancellation may not be available.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func cancel() -> Bool
```

#### Return Value

Returns [`false`](https://developer.apple.com/documentation/Swift/false) if the operation is not running, or if cancelation is not supported.

## See Also

- [func run(reply: (Bool, (any Error)?) -> Void)](tksmartcarduserinteraction/run(reply:).md)
  Runs the user interaction and asynchronously receives a reply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/cancel())*