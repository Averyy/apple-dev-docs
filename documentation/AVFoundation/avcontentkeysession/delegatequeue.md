# delegateQueue

**Framework**: AVFoundation  
**Kind**: property

The dispatch queue the session uses to invoke delegate callbacks.

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
var delegateQueue: dispatch_queue_t? { get }
```

## See Also

- [func setDelegate((any AVContentKeySessionDelegate)?, queue: dispatch_queue_t?)](avcontentkeysession/setdelegate(_:queue:).md)
  Sets the session’s delegate object and the dispatch queue on which to call the delegate’s methods.
- [var delegate: (any AVContentKeySessionDelegate)?](avcontentkeysession/delegate.md)
  The content key session’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/delegatequeue)*