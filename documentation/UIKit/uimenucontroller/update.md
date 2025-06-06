# update()

**Framework**: UIKit  
**Kind**: method

Updates the appearance and enabled state of menu commands.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func update()
```

#### Discussion

By default, `UIMenuController` calls this method just before the editing menu is made visible and when touches occur in the menu. As a result, a responder object in the application enables or disables menu commands depending on the context; for example, if the pasteboard holds no data of a compatible type, the Paste command would be disabled. You can call this method to force an update of the editing menu. You may also override this method to add any custom behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenucontroller/update())*