# splitView(_:constrainSplitPosition:ofSubviewAt:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to constrain the divider to certain positions.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
optional func splitView(_ splitView: NSSplitView, constrainSplitPosition proposedPosition: CGFloat, ofSubviewAt dividerIndex: Int) -> CGFloat
```

#### Return Value

The position for constraining the divider.

#### Discussion

If the delegate implements this method, the split view calls it repeatedly as the user moves the divider.

If a subview’s height must be a multiple of a certain number, use this method to return the multiple nearest to `proposedPosition`.

## Parameters

- `splitView`: The split view that sends the message.
- `proposedPosition`: The cursor’s current position, and the proposed position of the divider.
- `dividerIndex`: The index of the divider the user is moving, with the first divider being   and increasing from top to bottom (or left to right).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/splitview(_:constrainsplitposition:ofsubviewat:))*