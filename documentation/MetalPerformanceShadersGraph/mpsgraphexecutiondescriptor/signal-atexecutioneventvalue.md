# signal(_:atExecutionEvent:value:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Executable signals these shared events at execution stage and immediately proceeds.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func signal(_ event: any MTLSharedEvent, atExecutionEvent executionStage: MPSGraphExecutionStage, value: UInt64)
```

## Parameters

- `event`: Shared event to signal.
- `executionStage`: Execution stage to signal event at.
- `value`: Value for shared event to wait on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutiondescriptor/signal(_:atexecutionevent:value:))*