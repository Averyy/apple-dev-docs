# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An object that updates your app’s presentation and provides the session object for managing the interaction’s search.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UIFindInteractionDelegate)? { get }
```

```objc
@property (nonatomic, weak, readonly) id<UIFindInteractionDelegate> delegate;
```

## See Also

### Managing find interactions
- [func presentFindNavigator(showingReplace: Bool)](./presentfindnavigator%28showingreplace%29.md)
  Begins a search, displaying the find panel.
- [func dismissFindNavigator()](./dismissfindnavigator%28%29.md)
  Dismisses the find panel, if present.
- [func findNext()](./findnext%28%29.md)
  Highlights the next found result in the content, relative to the currently highlighted result.
- [func findPrevious()](./findprevious%28%29.md)
  Highlights the previously found result in the document, relative to the currently highlighted result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteraction/delegate)*