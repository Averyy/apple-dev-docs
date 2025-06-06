# setDraggingSourceOperationMask(_:forLocal:)

**Framework**: AppKit  
**Kind**: method

Configures the default value returned from [`draggingSourceOperationMaskForLocal:`](https://developer.apple.com/documentation/objectivec/nsobject/1415984-draggingsourceoperationmaskforlo).

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setDraggingSourceOperationMask(_ mask: NSDragOperation, forLocal isLocal: Bool)
```

#### Discussion

By default, [`draggingSourceOperationMaskForLocal:`](https://developer.apple.com/documentation/objectivec/nsobject/1415984-draggingsourceoperationmaskforlo) returns `NSDragOperationEvery` when `isLocal` is [`true`](https://developer.apple.com/documentation/swift/true) and `NSDragOperationNone` when `isLocal` is [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `mask`: The types of drag operations allowed.
- `isLocal`: If  ,   applies when the drag destination object is in the same application as the receiver; if  ,   applies when the destination object is outside the receiver’s application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontrol/setdraggingsourceoperationmask(_:forlocal:))*