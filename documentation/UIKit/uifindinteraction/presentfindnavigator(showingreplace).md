# presentFindNavigator(showingReplace:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Begins a search, displaying the find panel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func presentFindNavigator(showingReplace: Bool)
```

```objc
- (void) presentFindNavigatorShowingReplace:(BOOL) showingReplace;
```

## Discussion

You use this method to begin a search and display the find panel. The method calls [`findInteraction(_:sessionFor:)`](../uifindinteractiondelegate/findinteraction%28_,sessionfor%29.md) on the interaction object’s delegate and updates the UI using the session object the delegate returns.

The following example presents the find panel from a bar button item.

```swift
@objc func findButtonTapped(sender: UIBarButtonItem) {
    self.findInteraction!.presentFindNavigator(showingReplace: false)
}
```

The method has no effect if the find navigator panel is already present.

## Parameters

- `showingReplace`: `YES` to display a replace text field in the panel if the delegate supports text replacement. `No` to avoid displaying the replace text field.

## See Also

### Managing find interactions
- [var delegate: (any UIFindInteractionDelegate)?](./delegate.md)
  An object that updates your app’s presentation and provides the session object for managing the interaction’s search.
- [func dismissFindNavigator()](./dismissfindnavigator%28%29.md)
  Dismisses the find panel, if present.
- [func findNext()](./findnext%28%29.md)
  Highlights the next found result in the content, relative to the currently highlighted result.
- [func findPrevious()](./findprevious%28%29.md)
  Highlights the previously found result in the document, relative to the currently highlighted result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteraction/presentfindnavigator(showingreplace:))*