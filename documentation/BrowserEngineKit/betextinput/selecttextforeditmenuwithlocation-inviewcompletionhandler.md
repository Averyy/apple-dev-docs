# selectTextForEditMenuWithLocation(inView:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Indicates the edit menu displays at the given location in the text input view’s coordinate space.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func selectTextForEditMenuWithLocation(inView locationInView: CGPoint) async -> (Bool, String?, NSRange)
```

#### Discussion

The completion handler arguments are:

- A Boolean value that indicates whether the menu displays
- A string that represents the text context around the updated selection range (generally, this encompasses the paragraph containing the selection range)
- The range of the updated selection relative to the paragraph context

## See Also

- [func canPerformAction(Selector, withSender: Any?) -> Bool](betextinput/canperformaction(_:withsender:).md)
  Indicates whether the text view can process a given action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/selecttextforeditmenuwithlocation(inview:completionhandler:))*