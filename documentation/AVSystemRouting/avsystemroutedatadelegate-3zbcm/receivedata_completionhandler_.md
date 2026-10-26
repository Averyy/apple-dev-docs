# receiveData:completionHandler:

**Framework**: AVSystemRouting  
**Kind**: method  
**Role**: Instance Method

Receives data sent from a connected remote application.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
- (void) receiveData:(NSData *) data completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `data`: The data received from the remote application.
- `completionHandler`: A completion handler to call after processing the received data. Pass an error if processing fails, or `nil` on success.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutedatadelegate-3zbcm/receivedata:completionhandler:)*