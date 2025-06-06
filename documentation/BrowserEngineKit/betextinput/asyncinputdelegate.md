# asyncInputDelegate

**Framework**: BrowserEngineKit  
**Kind**: property  
**Required**: Yes

A system-provided input delegate is assigned when the system is interested in input changes.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
weak var asyncInputDelegate: (any BETextInputDelegate)? { get set }
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

A delegate object that your text view notifies of events and changes in the text’s state.

## See Also

- [func canPerformAction(Selector, withSender: Any?) -> Bool](betextinput/canperformaction(_:withsender:).md)
  Returns whether text related actions, such those included in UIResponderStandardEditActions, can be handled


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/asyncinputdelegate)*