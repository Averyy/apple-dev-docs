# FamilyActivityPicker

**Framework**: FamilyControls  
**Kind**: struct

A view in which users specify applications, web domains, and categories without revealing their choices to the app.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
@MainActor
@preconcurrency struct FamilyActivityPicker
```

#### Overview

To prompt the user for their selection, create a binding to a [`FamilyActivitySelection`](familyactivityselection.md) instance, and use the binding to create a [`FamilyActivityPicker`](familyactivitypicker.md) instance. You can then display the picker like any SwiftUI view.

```swift
struct ExampleView: View {
    @State var selection = FamilyActivitySelection()

    var body: some View {
        VStack {
            Image(systemName: "eye")
                .font(.system(size: 76.0))
                .padding()

            FamilyActivityPicker(selection: $selection)

            Image(systemName: "hourglass")
                .font(.system(size: 76.0))
                .padding()
        }
        .onChange(of: selection) { newSelection in
            let applications = selection.applications
            let categories = selection.categories
            let webDomains = selection.webDomains
        }
    }
}
```

> **Note**: A `FamilyActivityPicker` shown on a parent device only displays applications and websites from authorized child devices within the Family Sharing Group. A `FamilyActivityPicker` shown on an individually authorized device includes applications and websites from that same device.

To streamline this process, call  the [`familyActivityPicker(isPresented:selection:)`](https://developer.apple.com/documentation/SwiftUI/View/familyActivityPicker(isPresented:selection:)) modifier on a view in your user interface. This modifier displays the picker view as a sheet over your user interface when the `isPresented` binding is `true`.

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

When you present the `FamilyActivityPicker`, the system displays a view where the user can select categories, applications, and web domains. As soon as the user confirms their selection, the system updates the `FamilyActivitySelection` binding with the user’s selections. To protect the user’s privacy, the system uses opaque values to represent the selections.

Your app passes the selected values to the appropriate instances and methods from the [`ManagedSettings`](https://developer.apple.com/documentation/ManagedSettings) and [`DeviceActivity`](https://developer.apple.com/documentation/DeviceActivity) frameworks.

## Topics

### Creating activity pickers
- [init(selection: Binding<FamilyActivitySelection>)](familyactivitypicker/init(selection:).md)
  Creates a new activity picker.
### Accessing the content
- [var body: some View](familyactivitypicker/body.md)
  The content of this view.
### Adding view modifiers
- [View Modifiers](familyactivitypicker-view-modifiers.md)
  Apply standard modifiers to configure the family activity picker view and the views it contains.
### Initializers
- [init(headerText: String?, footerText: String?, selection: Binding<FamilyActivitySelection>)](familyactivitypicker/init(headertext:footertext:selection:).md)
  Creates a new activity picker with optional header and footer text.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct FamilyActivitySelection](familyactivityselection.md)
  A collection of applications, categories, and web domains selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker)*