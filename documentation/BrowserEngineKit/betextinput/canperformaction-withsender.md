# canPerformAction(_:withSender:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Indicates whether the text view can process a given action.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func canPerformAction(_ action: Selector, withSender sender: Any?) -> Bool
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)
- [Supporting extended text interactions](support-extended-text-interactions.md)

#### Return Value

A Boolean value that indicates whether the text view can handle the action message.

#### Discussion

This method is similar to [`responds(to:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/responds(to:)), except that even if your text view implements the action message, it can decline to handle it by returning `false` from this method.

## Parameters

- `action`: A selector for the action.
- `sender`: The object that’s sending the message.

## See Also

- [func selectTextForEditMenuWithLocation(inView: CGPoint, completionHandler: (Bool, String?, NSRange) -> Void)](betextinput/selecttextforeditmenuwithlocation(inview:completionhandler:).md)
  Indicates the edit menu displays at the given location in the text input view’s coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/canperformaction(_:withsender:))*