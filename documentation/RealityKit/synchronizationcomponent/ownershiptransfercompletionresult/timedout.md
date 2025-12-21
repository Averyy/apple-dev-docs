# SynchronizationComponent.OwnershipTransferCompletionResult.timedOut

**Framework**: RealityKit  
**Kind**: case

The ownership transfer request timed out.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
case timedOut
```

#### Discussion

A timeout doesn’t necessarily mean that the request is denied. It might succeed after the timeout.

## See Also

- [SynchronizationComponent.OwnershipTransferCompletionResult.granted](synchronizationcomponent/ownershiptransfercompletionresult/granted.md)
  The request is accepted and ownership is transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/synchronizationcomponent/ownershiptransfercompletionresult/timedout)*