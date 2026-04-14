# autoscroll(to:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Indicates that a text gesture initiated autoscrolling.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func autoscroll(to point: CGPoint)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

The text system calls the method repeatedly when a gesture requires the text view to scroll, for example, when a person adjusts the text selection range, or places the text cursor. The text system sends [`cancelAutoscroll()`](betextinput/cancelautoscroll().md) when there are no further updates.

## Parameters

- `point`: The location to which to autoscroll, in the coordinate system of your view’s [`textInputView`](betextinput/textinputview.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/autoscroll(to:))*