# cancel()

**Framework**: CryptoTokenKit  
**Kind**: method

Attempts to cancel an interaction started by calling [`run(reply:)`](tksmartcarduserinteraction/run(reply:).md). For certain interactions, cancellation may not be available.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func cancel() -> Bool
```

#### Return Value

Returns [`false`](https://developer.apple.com/documentation/swift/false) if the operation is not running, or if cancelation is not supported.

## See Also

- [func run(reply: (Bool, (any Error)?) -> Void)](tksmartcarduserinteraction/run(reply:).md)
  Runs the user interaction and asynchronously receives a reply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/cancel())*