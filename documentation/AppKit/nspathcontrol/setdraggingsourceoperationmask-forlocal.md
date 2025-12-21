# setDraggingSourceOperationMask(_:forLocal:)

**Framework**: AppKit  
**Kind**: method

Configures the drag operation mask.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setDraggingSourceOperationMask(_ mask: NSDragOperation, forLocal isLocal: Bool)
```

#### Discussion

This method configures the default return value of [`draggingSourceOperationMaskForLocal:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/draggingSourceOperationMaskForLocal:). By default, this method returns [`every`](nsdragoperation/every.md) when `isLocal` is [`true`](https://developer.apple.com/documentation/Swift/true) and [`NSDragOperationNone`](nsdragoperation/nsdragoperationnone.md) when `isLocal` is [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `mask`: The types of drag operations allowed.
- `isLocal`: If  ,   applies when the drag destination object is in the same application as the receiver; if  ,   applies when the destination object is outside the receiver’s application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontrol/setdraggingsourceoperationmask(_:forlocal:))*