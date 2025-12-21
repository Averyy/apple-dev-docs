# send(ins:p1:p2:data:le:reply:)

**Framework**: CryptoTokenKit  
**Kind**: method

Asynchronously transmits an APDU command to the card, returning the response in a completion handler.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst ?+
- macOS 10.10+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func send(ins: UInt8, p1: UInt8, p2: UInt8, data: Data? = nil, le: Int? = nil, reply: @escaping (Data?, UInt16, (any Error)?) -> Void)
```

#### Discussion

This call handles all ISO7816-4 APDU cases, translating to proper the sequences according to the protocol.  It consults the [`useExtendedLength`](tksmartcard/useextendedlength.md) and [`useCommandChaining`](tksmartcard/usecommandchaining.md) properties and uses these modes whenever appropriate for sending the APDU request.

## Parameters

- `ins`: The instruction code.
- `p1`: The first parameter.
- `p2`: The second parameter.
- `data`: The length of the data serves as   field of the APDU.
- `le`: The expected number of bytes to be returned, or   if no output data are expected—for example, a   or   APDU. Pass   to accept as many bytes as the card provides.
- `reply`: A closure to call when the response is returned from the card.

## See Also

- [func send(ins: UInt8, p1: UInt8, p2: UInt8, data: Data?, le: Int?) throws -> (sw: UInt16, response: Data)](tksmartcard/send(ins:p1:p2:data:le:).md)
  Synchronously transmits an APDU command to the card and returns the response.
- [func withSession<T>(() throws -> T) throws -> T](tksmartcard/withsession(_:).md)
  Synchronously begins a session, executes the given closure, and ends the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/send(ins:p1:p2:data:le:reply:))*