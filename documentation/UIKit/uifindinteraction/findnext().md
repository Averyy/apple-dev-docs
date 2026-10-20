# findNext()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Highlights the next found result in the content, relative to the currently highlighted result.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func findNext()
```

```objc
- (void) findNext;
```

## See Also

### Managing find interactions
- [var delegate: (any UIFindInteractionDelegate)?](./delegate.md)
  An object that updates your app’s presentation and provides the session object for managing the interaction’s search.
- [func presentFindNavigator(showingReplace: Bool)](./presentfindnavigator%28showingreplace%29.md)
  Begins a search, displaying the find panel.
- [func dismissFindNavigator()](./dismissfindnavigator%28%29.md)
  Dismisses the find panel, if present.
- [func findPrevious()](./findprevious%28%29.md)
  Highlights the previously found result in the document, relative to the currently highlighted result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteraction/findnext())*