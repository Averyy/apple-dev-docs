# textInteractionGesture(_:shouldBeginAt:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Returns whether a gesture at the given point in the view needs to begin.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func textInteractionGesture(_ gestureType: BEGestureType, shouldBeginAt point: CGPoint) -> Bool
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Return Value

`true` to permit the text system to proceed with the gesture; `false` otherwise.

## Parameters

- `gestureType`: The type of gesture that’s possibly beginning.
- `point`: The location of the gesture in the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/textinteractiongesture(_:shouldbeginat:))*