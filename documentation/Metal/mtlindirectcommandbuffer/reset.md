# reset(_:)

**Framework**: Metal  
**Kind**: method

Resets a range of commands to their default state.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst ?+
- macOS 10.14+
- tvOS 12.0+
- visionOS ?+

## Declaration

```swift
func reset(_ range: Range<Int>)
```

## Parameters

- `range`: The range of commands to reset. The range must fit inside the indirect command buffer’s extents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbuffer/reset(_:))*