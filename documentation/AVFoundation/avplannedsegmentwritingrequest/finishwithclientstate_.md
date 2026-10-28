# finishWithClientState:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Clients must call this method after all writing activities for the intermediate segment file have successfully completed. If called with nil, this is equivalent to calling finish.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (void) finishWithClientState:(NSData *) segmentEndingClientState;
```

## Discussion

This method throws NSGenericException if finish, finishWithClientState:, finishWithError:, or cancel has already been called on this request.

## See Also

### Managing client state
- [var clientStateToRestore: Data?](./clientstatetorestore.md)
  The client state persisted from the previous segment, if any. Specifically, this is the NSData provided to the previous segment’s finishWithClientState: method. The client is responsible to restore its client state before writing the current segment. For example, clients such as compositors with a temporal element may need some processing history of previous samples in order to generate an output sample at time N. This will be nil for algorithms that are stateless.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest/finishwithclientstate:)*