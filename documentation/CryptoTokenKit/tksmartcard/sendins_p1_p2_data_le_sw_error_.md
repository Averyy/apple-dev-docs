# sendIns:p1:p2:data:le:sw:error:

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

Synchronously transmits an APDU command to the card and returns the response.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```objc
- (NSData *) sendIns:(UInt8) ins p1:(UInt8) p1 p2:(UInt8) p2 data:(NSData *) requestData le:(NSNumber *) le sw:(UInt16 *) sw error:(NSError **) error;
```

#### Return Value

The returned data without the first two bytes (`SW1SW2`), or `nil` if an error occurred.

## Parameters

- `ins`: The instruction code.
- `p1`: The first parameter.
- `p2`: The second parameter.
- `requestData`: The data field of the APDU, or `nil` if no input data field should be present—for example, a `case1` or `case2` APDU.

  The length of the data serves as `Lc` field of the APDU.
- `le`: The expected number of bytes to be returned, or `nil` if no output data are expected—for example, a `case1` or `case3` APDU. Pass `0` to accept as many bytes as the card provides.
- `sw`: On return, contains the result code as represented by the first two bytes (`SW1SW2`) of the returned data.
- `error`: On return, if an error occurred when attempting to create a session or execute the block, contains details about the error.

## See Also

### Related Documentation
- [func beginSession(reply: (Bool, (any Error)?) -> Void)](./beginsession%28reply%29.md)
  Begins a session with the Smart Card.
### Transmitting Data
- [- sendIns:p1:p2:data:le:reply:](./sendins_p1_p2_data_le_reply_.md)
  Asynchronously transmits an APDU command to the card, returning the response in a completion handler.
- [- inSessionWithError:executeBlock:](./insessionwitherror_executeblock_.md)
  Synchronously begins a session, executes the given block, and ends the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/sendins:p1:p2:data:le:sw:error:)*