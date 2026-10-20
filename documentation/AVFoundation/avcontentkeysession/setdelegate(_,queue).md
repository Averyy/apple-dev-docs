# setDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the session’s delegate object and the dispatch queue on which to call the delegate’s methods.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func setDelegate(_ delegate: (any AVContentKeySessionDelegate)?, queue delegateQueue: dispatch_queue_t?)
```

```objc
- (void) setDelegate:(id<AVContentKeySessionDelegate>) delegate queue:(dispatch_queue_t) delegateQueue;
```

## Parameters

- `delegate`: An object that conforms to the [`AVContentKeySessionDelegate`](../avcontentkeysessiondelegate.md) protocol.
- `delegateQueue`: The dispatch queue on which the session calls the delegate object.

## See Also

### Managing the delegate object
- [var delegate: (any AVContentKeySessionDelegate)?](./delegate.md)
  The content key session’s delegate object.
- [var delegateQueue: dispatch_queue_t?](./delegatequeue.md)
  The dispatch queue the session uses to invoke delegate callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/setdelegate(_:queue:))*