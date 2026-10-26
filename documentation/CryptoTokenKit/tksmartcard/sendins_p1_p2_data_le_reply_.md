# sendIns:p1:p2:data:le:reply:

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously transmits an APDU command to the card, returning the response in a completion handler.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```objc
- (void) sendIns:(UInt8) ins p1:(UInt8) p1 p2:(UInt8) p2 data:(NSData *) requestData le:(NSNumber *) le reply:(void (^)(NSData *replyData, UInt16 sw, NSError *error)) reply;
```

## Parameters

- `ins`: The instruction code.
- `p1`: The first parameter.
- `p2`: The second parameter.
- `requestData`: The data field of the APDU, or `nil` if no input data field should be present—for example, a `case1` or `case2` APDU.

  The length of the data serves as `Lc` field of the APDU.
- `le`: The expected number of bytes to be returned, or `nil` if no output data are expected—for example, a `case1` or `case3` APDU. Pass `0` to accept as many bytes as the card provides.
- `reply`: A block to be called when the response is returned.

  - **replyData**: The returned data without the first two bytes (`SW1SW2`), or `nil` if an error occurred.
  - **sw**: The result code as represented by the first two bytes (`SW1SW2`) of the returned data.
  - **error**: If a communication error occurred or the `sw` result code is anything other than `0x9000`, contains details about the error.

## See Also

### Related Documentation
- [func transmit(Data, reply: (Data?, (any Error)?) -> Void)](./transmit%28_,reply%29.md)
  Transmits data in Application Protocol Data Unit (APDU) format to the Smart Card.
### Transmitting Data
- [- sendIns:p1:p2:data:le:sw:error:](./sendins_p1_p2_data_le_sw_error_.md)
  Synchronously transmits an APDU command to the card and returns the response.
- [- inSessionWithError:executeBlock:](./insessionwitherror_executeblock_.md)
  Synchronously begins a session, executes the given block, and ends the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/sendins:p1:p2:data:le:reply:)*