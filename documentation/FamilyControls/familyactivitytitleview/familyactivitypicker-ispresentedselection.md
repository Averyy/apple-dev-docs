# familyActivityPicker(isPresented:selection:)

**Framework**: FamilyControls  
**Kind**: method

Presents an activity picker view as a sheet.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
@MainActor
@preconcurrency func familyActivityPicker(isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View
```

#### Discussion

Use this view modifier to present a [`FamilyActivityPicker`](familyactivitypicker.md).

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/familyactivitypicker(ispresented:selection:))*