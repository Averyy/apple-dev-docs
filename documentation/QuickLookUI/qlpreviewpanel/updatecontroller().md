# updateController()

**Framework**: Quick Look UI  
**Kind**: method  
**Role**: Instance Method

Asks the preview panel to update its current controller.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func updateController()
```

```objc
- (void) updateController;
```

#### Discussion

The preview panel automatically updates its controller (by searching the responder chain) whenever the main or key window changes. You should only invoke this method if the responder chain changes without explicit notice.

## See Also

### Accessing the Preview Panel Controller
- [var currentController: Any!](./currentcontroller.md)
  The current first responder accepting to control the preview panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/updatecontroller())*