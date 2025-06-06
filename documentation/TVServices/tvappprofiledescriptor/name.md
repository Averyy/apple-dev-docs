# name

**Framework**: TV Services  
**Kind**: property

The user-visible label associated with the app profile.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var name: String { get set }
```

#### Discussion

Use this property to store the user-readable name for the user profile. When prompting the user to select a preferred profile, the [`TVUserManager`](tvusermanager.md) displays the names from your [`TVAppProfileDescriptor`](tvappprofiledescriptor.md) objects in the selection dialog.

You must specify a nonempty string in this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvappprofiledescriptor/name)*