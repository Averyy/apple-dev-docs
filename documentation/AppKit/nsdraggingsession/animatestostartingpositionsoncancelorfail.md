# animatesToStartingPositionsOnCancelOrFail

**Framework**: AppKit  
**Kind**: property

Controls whether the dragging image animates back to its starting point on a cancelled or failed drag.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var animatesToStartingPositionsOnCancelOrFail: Bool { get set }
```

#### Discussion

This property should be set immediately after creating the dragging session.

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var draggingFormation: NSDraggingFormation](nsdraggingsession/draggingformation.md)
  Controls the dragging formation when the drag is not over the source or a valid destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsession/animatestostartingpositionsoncancelorfail)*