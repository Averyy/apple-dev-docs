# beginSession(reply:)

**Framework**: CryptoTokenKit  
**Kind**: method

Begins a session with the Smart Card.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func beginSession() async throws -> Bool
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func beginSession() async throws -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method will fail if there is already an existing session for the Smart Card.

Calls to this method must be balanced with calls to [`endSession()`](tksmartcard/endsession().md).

## Parameters

- `reply`: The   object is created in the   domain with a code in the   enumeration.

## See Also

- [func transmit(Data, reply: (Data?, (any Error)?) -> Void)](tksmartcard/transmit(_:reply:).md)
  Transmits data in Application Protocol Data Unit (APDU) format to the Smart Card.
- [func endSession()](tksmartcard/endsession.md)
  Completes any pending transmissions and ends the session to the Smart Card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/beginsession(reply:))*