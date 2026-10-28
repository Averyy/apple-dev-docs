# announcementWasSuccessfulUserInfoKey

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the announcement is successful.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
nonisolated
static let announcementWasSuccessfulUserInfoKey: String
```

```c
extern NSString * const UIAccessibilityAnnouncementKeyWasSuccessful;
```

## Discussion

The value of this key is an [`NSNumber`](../../Foundation/nsnumber.md) object that the system interprets as a Boolean value.

## See Also

### Notification keys
- [static let announcementStringValueUserInfoKey: String](./announcementstringvalueuserinfokey.md)
  The text of the announcement.
- [static let focusedElementUserInfoKey: String](./focusedelementuserinfokey.md)
  The element currently in focus by the assistive app.
- [static let unfocusedElementUserInfoKey: String](./unfocusedelementuserinfokey.md)
  The element previously in focus by the assistive app.
- [static let assistiveTechnologyUserInfoKey: String](./assistivetechnologyuserinfokey.md)
  The identifier of the assistive app.
- [UIAccessibility.AssistiveTechnologyIdentifier](./assistivetechnologyidentifier.md)
  Identifiers for assistive apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/announcementwassuccessfuluserinfokey)*