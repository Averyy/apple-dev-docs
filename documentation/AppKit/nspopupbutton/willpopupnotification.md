# willPopUpNotification

**Framework**: AppKit  
**Kind**: property

Posted when an `NSPopUpButton` object receives a mouse-down event—that is, when the user is about to select an item from the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
class let willPopUpNotification: NSNotification.Name
```

#### Discussion

The notification object is the selected `NSPopUpButton` object. This notification does not contain a `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/willpopupnotification)*