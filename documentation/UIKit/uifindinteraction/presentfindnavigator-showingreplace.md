# presentFindNavigator(showingReplace:)

**Framework**: UIKit  
**Kind**: method

Begins a search, displaying the find panel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func presentFindNavigator(showingReplace: Bool)
```

#### Discussion

You use this method to begin a search and display the find panel. The method calls [`findInteraction(_:sessionFor:)`](uifindinteractiondelegate/findinteraction(_:sessionfor:).md) on the interaction object’s delegate and updates the UI using the session object the delegate returns.

The following example presents the find panel from a bar button item.

```swift
@objc func findButtonTapped(sender: UIBarButtonItem) {
    self.findInteraction!.presentFindNavigator(showingReplace: false)
}
```

The method has no effect if the find navigator panel is already present.

## Parameters

- `showingReplace`:   to display a replace text field in the panel if the delegate supports text replacement.   to avoid displaying the replace text field.

## See Also

- [var delegate: (any UIFindInteractionDelegate)?](uifindinteraction/delegate.md)
  An object that updates your app’s presentation and provides the session object for managing the interaction’s search.
- [func dismissFindNavigator()](uifindinteraction/dismissfindnavigator.md)
  Dismisses the find panel, if present.
- [func findNext()](uifindinteraction/findnext.md)
  Highlights the next found result in the content, relative to the currently highlighted result.
- [func findPrevious()](uifindinteraction/findprevious.md)
  Highlights the previously found result in the document, relative to the currently highlighted result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteraction/presentfindnavigator(showingreplace:))*