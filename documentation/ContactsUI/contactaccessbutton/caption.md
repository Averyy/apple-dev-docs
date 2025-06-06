# ContactAccessButton.Caption

**Framework**: Contacts UI  
**Kind**: enum

A list of access options to display in the contact access button when matching a contact’s name.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
enum Caption
```

#### Overview

Set the caption of a contact access button with the view modifier [`contactAccessButtonCaption(_:)`](https://developer.apple.com/documentation/SwiftUI/View/contactAccessButtonCaption(_:)). When the query produces a single result, the content access button shows the the caption under the matching contact name. For example, a search for `Anne` could show a button that displays the matching name “Anne Johnson” with a caption line of “annejohnson1@icloud.com” when the caption type is [`ContactAccessButton.Caption.email`](contactaccessbutton/caption/email.md).

## Topics

### Caption options
- [ContactAccessButton.Caption.defaultText](contactaccessbutton/caption/defaulttext.md)
  A caption option that displays a default value.
- [ContactAccessButton.Caption.email](contactaccessbutton/caption/email.md)
  A caption option that displays an email address for the contact.
- [ContactAccessButton.Caption.phone](contactaccessbutton/caption/phone.md)
  A caption option that displays a phone number for the contact.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/contactaccessbutton/caption)*