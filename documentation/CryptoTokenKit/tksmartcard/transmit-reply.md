# transmit(_:reply:)

**Framework**: CryptoTokenKit  
**Kind**: method

Transmits data in Application Protocol Data Unit (APDU) format to the Smart Card.

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
func transmit(_ request: Data) async throws -> Data
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func transmit(_ request: Data) async throws -> Data
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func transmit(_ request: Data) async throws -> Data
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

You should only call this method after a session to the Smart Card has been established using the [`beginSession(reply:)`](tksmartcard/beginsession(reply:).md) method, and before the session is terminated using the [`endSession()`](tksmartcard/endsession().md) method.

## Parameters

- `request`: The APDU request data.
- `reply`: The   object is created in the   domain with a code in the   enumeration.

## See Also

- [func beginSession(reply: (Bool, (any Error)?) -> Void)](tksmartcard/beginsession(reply:).md)
  Begins a session with the Smart Card.
- [func endSession()](tksmartcard/endsession.md)
  Completes any pending transmissions and ends the session to the Smart Card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/transmit(_:reply:))*