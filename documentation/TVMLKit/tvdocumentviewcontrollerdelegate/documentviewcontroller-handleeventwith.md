# documentViewController(_:handleEvent:with:)

**Framework**: TVMLKit  
**Kind**: method

Handles events natively from document view controllers.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
optional func documentViewController(_ documentViewController: TVDocumentViewController, handleEvent event: TVDocumentViewController.Event, with element: TVViewElement) -> Bool
```

#### Discussion

By default, event handling can happen in either `TVMLKit` or `TVMLKit JS`. To defer event handling exclusively to `TVMLKit JS`, return `false` and don’t handle the event in this `TVMLKit` method. To assign event handling to `TVMLKit`, handle the event in this method and return `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontrollerdelegate/documentviewcontroller(_:handleevent:with:))*