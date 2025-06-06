# UIFindInteractionDelegate

**Framework**: UIKit  
**Kind**: protocol

A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIFindInteractionDelegate : NSObjectProtocol
```

## Topics

### Beginning the search
- [func findInteraction(UIFindInteraction, sessionFor: UIView) -> UIFindSession?](uifindinteractiondelegate/findinteraction(_:sessionfor:).md)
  Provides the object for managing the state, presentation, and behavior of the search.
### Decorating the searched content
- [func findInteraction(UIFindInteraction, didBegin: UIFindSession)](uifindinteractiondelegate/findinteraction(_:didbegin:).md)
  Informs the delegate when the interaction is about to present the find panel.
- [func findInteraction(UIFindInteraction, didEnd: UIFindSession)](uifindinteractiondelegate/findinteraction(_:didend:).md)
  Informs the delegate when the interaction is about to dismiss the find panel.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UITextView](uitextview.md)

## See Also

- [class UIFindInteraction](uifindinteraction.md)
  An interaction that provides text finding and replacing operations using a system find panel.
- [class UIFindSession](uifindsession.md)
  An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.
- [class UITextSearchingFindSession](uitextsearchingfindsession.md)
  A find session object that wraps a searchable object implementing the text-searching protocol.
- [protocol UITextSearching](uitextsearching-3wkjv.md)
  The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.
- [class UITextSearchOptions](uitextsearchoptions.md)
  An object containing the configurable options for a text search.
- [enum UITextSearchFoundTextStyle](uitextsearchfoundtextstyle.md)
  Constants that describe the style a find session uses to decorate the text.
- [UITextSearchOptions.WordMatchMethod](uitextsearchoptions/wordmatchmethod-swift.enum.md)
  Constants that describe the method to use when searching text for words that match a string.
- [UIFindSession.SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md)
  Constants that describe the results summary the find panel UI includes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteractiondelegate)*