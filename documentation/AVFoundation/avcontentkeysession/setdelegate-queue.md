# setDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method

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

## Parameters

- `delegate`: An object that conforms to the   protocol.
- `delegateQueue`: The dispatch queue on which the session calls the delegate object.

## See Also

- [var delegate: (any AVContentKeySessionDelegate)?](avcontentkeysession/delegate.md)
  The content key session’s delegate object.
- [var delegateQueue: dispatch_queue_t?](avcontentkeysession/delegatequeue.md)
  The dispatch queue the session uses to invoke delegate callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/setdelegate(_:queue:))*