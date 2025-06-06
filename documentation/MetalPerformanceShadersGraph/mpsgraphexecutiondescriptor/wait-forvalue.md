# wait(for:value:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Executable waits on these shared events before scheduling execution on the HW, this does not include encoding which can still continue.

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

## Parameters

- `event`: Shared event graph waits on.
- `value`: Value of shared event graph waits on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutiondescriptor/wait(for:value:))*