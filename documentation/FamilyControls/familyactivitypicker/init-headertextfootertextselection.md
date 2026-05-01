# init(headerText:footerText:selection:)

**Framework**: Family Controls  
**Kind**: init

Creates a new activity picker with optional header and footer text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency init(headerText: String? = nil, footerText: String? = nil, selection: Binding<FamilyActivitySelection>)
```

## Parameters

- `headerText`: An optional string that provides text for the header of the picker view.
- `footerText`: An optional string that provides text for the footer of the picker view.
- `selection`: A binding that manages the user-selected categories, apps, and web domains.

## See Also

- [init(selection: Binding<FamilyActivitySelection>)](familyactivitypicker/init(selection:).md)
  Creates a new activity picker.
- [func familyActivityPicker(title: String?, headerText: String?, footerText: String?, isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View
](../SwiftUI/View/familyActivityPicker(title:headerText:footerText:isPresented:selection:).md)
  Present an activity picker sheet for selecting apps and websites to manage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/init(headertext:footertext:selection:))*