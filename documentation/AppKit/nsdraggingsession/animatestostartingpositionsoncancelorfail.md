# animatesToStartingPositionsOnCancelOrFail

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Controls whether the dragging image animates back to its starting point on a cancelled or failed drag.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var animatesToStartingPositionsOnCancelOrFail: Bool { get set }
```

```objc
@property BOOL animatesToStartingPositionsOnCancelOrFail;
```

#### Discussion

This property should be set immediately after creating the dragging session.

The default value is [`true`](../../Swift/true.md).

## See Also

### Dragging Visual Representation
- [var draggingFormation: NSDraggingFormation](./draggingformation.md)
  Controls the dragging formation when the drag is not over the source or a valid destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsession/animatestostartingpositionsoncancelorfail)*