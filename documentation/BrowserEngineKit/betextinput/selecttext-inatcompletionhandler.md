# selectText(in:at:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Selects the text within the given granularity at the given point in the text view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func selectText(in granularity: UITextGranularity, at point: CGPoint) async
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

## Parameters

- `granularity`: The amount of text to select.
- `point`: The location of the selection in the text view.
- `completionHandler`: A block you call after your text view handles the gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/selecttext(in:at:completionhandler:))*