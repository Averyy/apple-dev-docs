# withSession(_:)

**Framework**: CryptoTokenKit  
**Kind**: method

Synchronously begins a session, executes the given closure, and ends the session.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS 10.12+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func withSession<T>(_ body: @escaping () throws -> T) throws -> T
```

## Parameters

- `body`: A closure to be called in the context of the created session.

## See Also

- [func send(ins: UInt8, p1: UInt8, p2: UInt8, data: Data?, le: Int?, reply: (Data?, UInt16, (any Error)?) -> Void)](tksmartcard/send(ins:p1:p2:data:le:reply:).md)
  Asynchronously transmits an APDU command to the card, returning the response in a completion handler.
- [func send(ins: UInt8, p1: UInt8, p2: UInt8, data: Data?, le: Int?) throws -> (sw: UInt16, response: Data)](tksmartcard/send(ins:p1:p2:data:le:).md)
  Synchronously transmits an APDU command to the card and returns the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/withsession(_:))*