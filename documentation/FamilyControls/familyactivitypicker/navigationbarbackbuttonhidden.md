# navigationBarBackButtonHidden(_:)

**Framework**: FamilyControls  
**Kind**: method

Hides the navigation bar back button for the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 13.0+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func navigationBarBackButtonHidden(_ hidesBackButton: Bool = true) -> some View
```

#### Discussion

Use `navigationBarBackButtonHidden(_:)` to hide the back button for this view.

This modifier only takes effect when this view is inside of and visible within a `NavigationView`.

## Parameters

- `hidesBackButton`: A Boolean value that indicates whether to   hide the back button. The default value is  .

## See Also

- [func navigationBarHidden(Bool) -> some View](familyactivitypicker/navigationbarhidden(_:).md)
  Hides the navigation bar for this view.
- [func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) -> some View](familyactivitypicker/navigationbartitledisplaymode(_:).md)
  Configures the title display mode for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/navigationbarbackbuttonhidden(_:))*