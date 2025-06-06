# delegate

**Framework**: AVFoundation  
**Kind**: property

The content key session’s delegate object.

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
weak var delegate: (any AVContentKeySessionDelegate)? { get }
```

#### Discussion

Set the session’s delegate using the [`setDelegate(_:queue:)`](avcontentkeysession/setdelegate(_:queue:).md) method.

## See Also

- [func setDelegate((any AVContentKeySessionDelegate)?, queue: dispatch_queue_t?)](avcontentkeysession/setdelegate(_:queue:).md)
  Sets the session’s delegate object and the dispatch queue on which to call the delegate’s methods.
- [var delegateQueue: dispatch_queue_t?](avcontentkeysession/delegatequeue.md)
  The dispatch queue the session uses to invoke delegate callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/delegate)*