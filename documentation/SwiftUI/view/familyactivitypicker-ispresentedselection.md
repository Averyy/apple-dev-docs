# familyActivityPicker(isPresented:selection:)

**Framework**: SwiftUI  
**Kind**: method

Presents an activity picker view as a sheet.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
@MainActor
@preconcurrency func familyActivityPicker(isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View
```

#### Discussion

Use this view modifier to present a `FamilyControls/FamilyActivityPicker`.

```swift
struct ExampleView: View {
    @State var selection = FamilyActivitySelection()
    @State var isPresented = false

   var body: some View {
       Button("Present FamilyActivityPicker") { isPresented = true }
       .familyActivityPicker(isPresented: $isPresented,
                             selection: $selection)
       .onChange(of: selection) { newSelection in
           let applications = selection.applications
           let categories = selection.categories
           let webDomains = selection.webDomains
       }
   }
}
```

## Parameters

- `isPresented`: A binding that indicates whether the app presents the picker view.
- `selection`: A binding that manages the user-selected categories, apps, and web domains.

## See Also

- [struct FamilyActivityPicker](../FamilyControls/FamilyActivityPicker.md)
  A view in which users specify applications, web domains, and categories without revealing their choices to the app.
- [func familyActivityPicker(headerText: String?, footerText: String?, isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View](view/familyactivitypicker(headertext:footertext:ispresented:selection:).md)
  Presents an activity picker view as a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/familyactivitypicker(ispresented:selection:))*