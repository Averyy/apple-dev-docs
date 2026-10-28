# inSessionWithError:executeBlock:

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

Synchronously begins a session, executes the given block, and ends the session.

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
- (BOOL) inSessionWithError:(NSError **) error executeBlock:(BOOL (^)(NSError **error)) block;
```

## Return Value

[`true`](../../Swift/true.md) if the session was successfully created and the specified block returns [`true`](../../Swift/true.md); otherwise, [`false`](../../Swift/false.md).

## Parameters

- `error`: On return, if an error occurred when attempting to create a session or execute the block, contains details about the error.
- `block`: A block to be called in the context of the created session. This block returns a Boolean value indicating whether communication was successful.

  - **error**: To indicate that an error occurred during the session, populate this with an `NSError` object containing details and return [`false`](../../Swift/false.md).

## See Also

### Transmitting Data
- [- sendIns:p1:p2:data:le:reply:](./sendins_p1_p2_data_le_reply_.md)
  Asynchronously transmits an APDU command to the card, returning the response in a completion handler.
- [- sendIns:p1:p2:data:le:sw:error:](./sendins_p1_p2_data_le_sw_error_.md)
  Synchronously transmits an APDU command to the card and returns the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/insessionwitherror:executeblock:)*