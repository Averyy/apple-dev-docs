# currentController

**Framework**: Quick Look UI  
**Kind**: property

The current first responder accepting to control the preview panel.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var currentController: Any! { get }
```

#### Discussion

You should never change the preview panel’s state (for example, its delegate, datasource, and so on) if you aren’t controlling it.

## See Also

- [func updateController()](qlpreviewpanel/updatecontroller.md)
  Asks the preview panel to update its current controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/currentcontroller)*