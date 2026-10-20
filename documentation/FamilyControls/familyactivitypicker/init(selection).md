# init(selection:)

**Framework**: Family Controls  
**Kind**: init  
**Role**: Initializer

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

### Creating activity pickers
- [init(headerText: String?, footerText: String?, selection: Binding<FamilyActivitySelection>)](./init%28headertext,footertext,selection%29.md)
  Creates a new activity picker with optional header and footer text.
- [func familyActivityPicker(title: String?, headerText: String?, footerText: String?, isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View
](../../SwiftUI/view/familyactivitypicker%28title,headertext,footertext,ispresented,selection%29.md)
  Present an activity picker sheet for selecting apps and websites to manage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/init(selection:))*