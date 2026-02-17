# activityViewControllerShareRecipients(_:)

**Framework**: UIKit  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
optional func activityViewControllerShareRecipients(_ activityViewController: UIActivityViewController) -> [INPerson]
```

#### Discussion

Allows the activity item source to provide recipients who will be filled in by default in the compose view if that sharing app supports it.

This might fail to pre-fill correctly if the sharing app chosen by the user can’t recognize the provided person. Also, if a people suggestion is chosen, that suggestion will override this provided value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsource/activityviewcontrollersharerecipients(_:))*