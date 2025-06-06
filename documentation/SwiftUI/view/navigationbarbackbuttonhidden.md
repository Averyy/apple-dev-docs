# navigationBarBackButtonHidden(_:)

**Framework**: SwiftUI  
**Kind**: method

Hides the navigation bar back button for the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func navigationBarBackButtonHidden(_ hidesBackButton: Bool = true) -> some View
```

#### Discussion

Use `navigationBarBackButtonHidden(_:)` to hide the back button for this view.

This modifier only takes effect when this view is inside of and visible within a [`NavigationView`](navigationview.md).

## Parameters

- `hidesBackButton`: A Boolean value that indicates whether to   hide the back button. The default value is  .

## See Also

- [func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) -> some View](view/navigationbartitledisplaymode(_:).md)
  Configures the title display mode for this view.
- [struct NavigationBarItem](navigationbaritem.md)
  A configuration for a navigation bar that represents a view at the top of a navigation stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationbarbackbuttonhidden(_:))*