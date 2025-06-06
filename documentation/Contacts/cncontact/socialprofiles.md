# socialProfiles

**Framework**: Contacts  
**Kind**: property

An array of labeled social profiles for a contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var socialProfiles: [CNLabeledValue<CNSocialProfile>] { get }
```

#### Discussion

This property is an array of [`CNLabeledValue`](cnlabeledvalue.md) objects, each of which has a label and a [`CNSocialProfile`](cnsocialprofile.md) value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/socialprofiles)*