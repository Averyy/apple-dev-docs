# init(queue:)

**Framework**: CallKit  
**Kind**: init

Initializes a new call controller with a specified queue, which is used for calling completion blocks.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(queue: dispatch_queue_t)
```

#### Return Value

A new call controller initialized with the specified queue.

#### Discussion

This is the designated initializer.

## Parameters

- `queue`: The queue used for calling completion blocks.

## See Also

- [convenience init()](cxcallcontroller/init.md)
  Initializes a new call controller with a private, serial queue, which is used for calling completion blocks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallcontroller/init(queue:))*