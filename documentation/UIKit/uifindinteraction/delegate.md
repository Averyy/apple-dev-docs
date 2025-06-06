# delegate

**Framework**: UIKit  
**Kind**: property

An object that updates your app’s presentation and provides the session object for managing the interaction’s search.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIFindInteractionDelegate)? { get }
```

## See Also

- [func presentFindNavigator(showingReplace: Bool)](uifindinteraction/presentfindnavigator(showingreplace:).md)
  Begins a search, displaying the find panel.
- [func dismissFindNavigator()](uifindinteraction/dismissfindnavigator.md)
  Dismisses the find panel, if present.
- [func findNext()](uifindinteraction/findnext.md)
  Highlights the next found result in the content, relative to the currently highlighted result.
- [func findPrevious()](uifindinteraction/findprevious.md)
  Highlights the previously found result in the document, relative to the currently highlighted result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteraction/delegate)*