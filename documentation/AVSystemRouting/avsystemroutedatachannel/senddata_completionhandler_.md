# sendData:completionHandler:

**Framework**: AVSystemRouting  
**Kind**: method  
**Role**: Instance Method

Sends data to a remote application.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
- (void) sendData:(NSData *) data completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

Calling this function again before the completion handler of a previous send is called is safe; multiple send operations can be in-flight concurrently.

## Parameters

- `data`: The data to send to the remote application.
- `completionHandler`: A completion handler called when the send operation completes. The handler receives an error if the send failed, or `nil` on success.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutedatachannel/senddata:completionhandler:)*