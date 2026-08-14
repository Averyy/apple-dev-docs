# init(selection:)

**Framework**: Family Controls  
**Kind**: init

Creates a new activity picker.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
@MainActor
@preconcurrency init(selection: Binding<FamilyActivitySelection>)
```

## Parameters

- `selection`: A binding that manages the user-selected categories, apps, and web domains.

## See Also

- [init(headerText: String?, footerText: String?, selection: Binding<FamilyActivitySelection>)](familyactivitypicker/init(headertext:footertext:selection:).md)
  Creates a new activity picker with optional header and footer text.
- [func familyActivityPicker(title: String?, headerText: String?, footerText: String?, isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View
](../swiftui/view/familyactivitypicker(title:headertext:footertext:ispresented:selection:).md)
  Present an activity picker sheet for selecting apps and websites to manage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/init(selection:))*