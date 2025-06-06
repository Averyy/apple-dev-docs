# wait(for:value:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Waits on these shared events before scheduling execution on the HW.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func wait(for event: any MTLSharedEvent, value: UInt64)
```

#### Discussion

This does not include encoding which can still continue.

## Parameters

- `event`: Shared event to wait on.
- `value`: Value for shared event to wait on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutableexecutiondescriptor/wait(for:value:))*