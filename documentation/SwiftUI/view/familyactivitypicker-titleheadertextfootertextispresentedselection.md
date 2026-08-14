# familyActivityPicker(title:headerText:footerText:isPresented:selection:)

**Framework**: SwiftUI  
**Kind**: method

Present an activity picker sheet for selecting apps and websites to manage.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
@MainActor
@preconcurrency func familyActivityPicker(title: String?, headerText: String? = nil, footerText: String? = nil, isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View
```

#### Discussion

Use this view modifier to present a `FamilyControls/FamilyActivityPicker` with a custom title.

```swift
struct ContentView: View {
    @State private var selection = FamilyActivitySelection()
    @State private var isPresented = false

    var body: some View {
        Button("Select Activities") {
            isPresented = true
        }
        .familyActivityPicker(
            title: "Choose Apps to Limit",
            headerText: "Select apps and websites to manage",
            footerText: "These selections will be used for screen time limits",
            isPresented: $isPresented,
            selection: $selection
        )
        .onChange(of: selection) { newSelection in
            // Handle the selected activities
            print("Selected \(newSelection.applications.count) apps")
        }
    }
}
```

## Parameters

- `title`: An optional string that provides a title for the picker view.
- `headerText`: An optional string that provides text for the header of the picker view.
- `footerText`: An optional string that provides text for the footer of the picker view.
- `isPresented`: A binding that indicates whether the app presents the picker view.
- `selection`: A binding that manages the selected categories, apps, and web domains.

## See Also

- [struct FamilyActivityPicker](../familycontrols/familyactivitypicker.md)
  A view in which users specify applications, web domains, and categories without revealing their choices to the app.
- [func familyActivityPicker(isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View](view/familyactivitypicker(ispresented:selection:).md)
  Presents an activity picker view as a sheet.
- [func familyActivityPicker(headerText: String?, footerText: String?, isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View](view/familyactivitypicker(headertext:footertext:ispresented:selection:).md)
  Presents an activity picker view as a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/familyactivitypicker(title:headertext:footertext:ispresented:selection:))*