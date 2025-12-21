# familyActivityPicker(headerText:footerText:isPresented:selection:)

**Framework**: SwiftUI  
**Kind**: method

Presents an activity picker view as a sheet.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency func familyActivityPicker(headerText: String? = nil, footerText: String? = nil, isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View
```

#### Discussion

Use this view modifier to present a `FamilyControls/FamilyActivityPicker`.

## Parameters

- `headerText`: An optional string that provides text for the header of the picker view.
- `footerText`: An optional string that provides text for the footer of the picker view.
- `isPresented`: A binding that indicates whether the app presents the picker view.
- `selection`: A binding that manages the user-selected categories, apps, and web domains.

## See Also

- [struct FamilyActivityPicker](../FamilyControls/FamilyActivityPicker.md)
  A view in which users specify applications, web domains, and categories without revealing their choices to the app.
- [func familyActivityPicker(isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View](view/familyactivitypicker(ispresented:selection:).md)
  Presents an activity picker view as a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/familyactivitypicker(headertext:footertext:ispresented:selection:))*