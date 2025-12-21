# run(reply:)

**Framework**: CryptoTokenKit  
**Kind**: method

Runs the user interaction and asynchronously receives a reply.

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
func run() async throws -> Bool
```

## Parameters

- `reply`: The   object is created in the   domain with a code in the   enumeration.

## See Also

- [func cancel() -> Bool](tksmartcarduserinteraction/cancel.md)
  Attempts to cancel an interaction started by calling [`run(reply:)`](tksmartcarduserinteraction/run(reply:).md). For certain interactions, cancellation may not be available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/run(reply:))*