# setDraggingSourceOperationMask(_:forLocal:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Configures the drag operation mask.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setDraggingSourceOperationMask(_ mask: NSDragOperation, forLocal isLocal: Bool)
```

```objc
- (void) setDraggingSourceOperationMask:(NSDragOperation) mask forLocal:(BOOL) isLocal;
```

#### Discussion

This method configures the default return value of [`draggingSourceOperationMaskForLocal:`](../../ObjectiveC/nsobject-swift.class/draggingsourceoperationmaskforlocal_.md). By default, this method returns [`every`](../nsdragoperation/every.md) when `isLocal` is [`true`](../../Swift/true.md) and [`NSDragOperationNone`](../nsdragoperation/nsdragoperationnone.md) when `isLocal` is [`false`](../../Swift/false.md).

## Parameters

- `mask`: The types of drag operations allowed.
- `isLocal`: If [`true`](../../Swift/true.md), `mask` applies when the drag destination object is in the same application as the receiver; if [`false`](../../Swift/false.md), `mask` applies when the destination object is outside the receiver’s application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontrol/setdraggingsourceoperationmask(_:forlocal:))*