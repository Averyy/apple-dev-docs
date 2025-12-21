# Displaying Activity Labels

**Framework**: FamilyControls

Provide users with a read-only, visual representation of an application, category, or web domain.

#### Overview

To display an application, category, or web domain, choose an [`ApplicationToken`](https://developer.apple.com/documentation/ManagedSettings/ApplicationToken), [`ActivityCategoryToken`](https://developer.apple.com/documentation/ManagedSettings/ActivityCategoryToken), or [`WebDomainToken`](https://developer.apple.com/documentation/ManagedSettings/WebDomainToken) that represents an item selected by the user. For example, you can access these tokens from the [`FamilyActivitySelection`](familyactivityselection.md) bound to a [`FamilyActivityPicker`](familyactivitypicker.md) view.

Use one of these tokens to create a [`Label`](https://developer.apple.com/documentation/SwiftUI/Label) instance by passing the token to its initializer. Display the activity item like any SwiftUI view.

```swift
struct ExampleView: View {
    @State var selection = FamilyActivitySelection()

    var body: some View {
        VStack {
            FamilyActivityPicker(selection: $selection)
            if let applicationToken = selection.applicationTokens.first {
                Label(applicationToken)
            }
        }
    }
}
```

## Topics

### Label constraints
- [struct FamilyActivityTitleView](familyactivitytitleview.md)
  A type-erased view representing the title of the family activity.
- [struct FamilyActivityIconView](familyactivityiconview.md)
  A type-erased view representing the icon of the family activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/displayingactivitylabels)*