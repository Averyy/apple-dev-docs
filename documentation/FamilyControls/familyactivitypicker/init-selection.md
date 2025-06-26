# init(selection:)

**Framework**: FamilyControls  
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

- [func familyActivityPicker(isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View](familyactivitypicker/familyactivitypicker(ispresented:selection:).md)
  Presents an activity picker view as a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/init(selection:))*