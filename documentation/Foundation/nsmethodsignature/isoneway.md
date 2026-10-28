# isOneway

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Whether the receiver is asynchronous when invoked through distributed objects.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (BOOL) isOneway;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver is asynchronous when invoked through distributed objects, otherwise [`false`](../../Swift/false.md).

## Discussion

If the method is `oneway`, the sender of the remote message doesn’t block awaiting a reply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmethodsignature/isoneway)*