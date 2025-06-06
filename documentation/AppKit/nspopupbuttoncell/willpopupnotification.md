# willPopUpNotification

**Framework**: AppKit  
**Kind**: property

This notification is posted just before a pop-up menu is attached to its window frame.

**Availability**:
- macOS ?+

## Declaration

```swift
class let willPopUpNotification: NSNotification.Name
```

#### Discussion

You can use this notification to lazily construct your part’s menus, thus preventing unnecessary calculations until they are needed. The notification object can be either a pop-up button or its enclosed pop-up button cell. This notification does not contain a `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/willpopupnotification)*