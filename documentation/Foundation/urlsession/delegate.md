# delegate

**Framework**: Foundation  
**Kind**: property

The delegate assigned when this object was created.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var delegate: (any URLSessionDelegate)? { get }
```

#### Discussion

This delegate object is responsible for handling authentication challenges, for making caching decisions, and for handling other session-related events. The session object keeps a strong reference to this delegate until your app exits or explicitly invalidates the session. If you do not invalidate the session, your app leaks memory until it exits.

> **Note**:  This delegate object must be set at object creation time and may not be changed.

## See Also

- [protocol URLSessionDelegate](urlsessiondelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle session-level events, like session life cycle changes.
- [protocol URLSessionTaskDelegate](urlsessiontaskdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events.
- [var delegateQueue: OperationQueue](urlsession/delegatequeue.md)
  The operation queue provided when this object was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/delegate)*