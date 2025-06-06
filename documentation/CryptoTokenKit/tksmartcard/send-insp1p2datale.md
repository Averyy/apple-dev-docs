# send(ins:p1:p2:data:le:)

**Framework**: CryptoTokenKit  
**Kind**: method

Synchronously transmits an APDU command to the card and returns the response.

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
func send(ins: UInt8, p1: UInt8, p2: UInt8, data: Data? = nil, le: Int? = nil) throws -> (sw: UInt16, response: Data)
```

#### Return Value

A tuple containing the result code as contained in the first two bytes (`SW1SW2`) of the returned data, and the returned data excluding the first two bytes.

## Parameters

- `ins`: The instruction code.
- `p1`: The first parameter.
- `p2`: The second parameter.
- `data`: The length of the data serves as   field of the APDU.
- `le`: The expected number of bytes to be returned, or nil if no output data are expected—for example, a   or   APDU. Pass   to accept as many bytes as the card provides.

## See Also

- [func send(ins: UInt8, p1: UInt8, p2: UInt8, data: Data?, le: Int?, reply: (Data?, UInt16, (any Error)?) -> Void)](tksmartcard/send(ins:p1:p2:data:le:reply:).md)
  Asynchronously transmits an APDU command to the card, returning the response in a completion handler.
- [func withSession<T>(() throws -> T) throws -> T](tksmartcard/withsession(_:).md)
  Synchronously begins a session, executes the given closure, and ends the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/send(ins:p1:p2:data:le:))*