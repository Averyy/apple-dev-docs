# adjustSelectionBoundary(to:touchPhase:baseIsStart:flags:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Adjusts the start or end boundary of the current selection to the given point.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func adjustSelectionBoundary(to point: CGPoint, touchPhase touch: BESelectionTouchPhase, baseIsStart boundaryIsStart: Bool, flags: BESelectionFlags)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

When you receive this method, call [`selectionBoundaryAdjusted(to:touchPhase:flags:)`](betextinteraction/selectionboundaryadjusted(to:touchphase:flags:).md) to notify the system that your text view handled the update.

## Parameters

- `point`: The new boundary point of the selection.
- `touch`: The touch phase of the gesture.
- `boundaryIsStart`: `true` if the `point` is at the new start of the selection; `false` if it’s at the end.
- `flags`: Extra information about the selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/adjustselectionboundary(to:touchphase:baseisstart:flags:))*