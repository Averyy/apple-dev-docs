# binaryName(from:)

**Framework**: MetricKit  
**Kind**: method

Binary name - look up from tree

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func binaryName(from tree: CallStackTree) -> String?
```

#### Return Value

The binary name, or nil if not found

## Parameters

- `tree`: The call stack tree containing this frame

## See Also

- [let subFrames: ContiguousArray<CallStackFrame>](callstackframe/subframes.md)
  Sub-frames (children in the call tree)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/callstackframe/binaryname(from:))*