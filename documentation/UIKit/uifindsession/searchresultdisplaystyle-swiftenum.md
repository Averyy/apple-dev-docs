# UIFindSession.SearchResultDisplayStyle

**Framework**: UIKit  
**Kind**: enum

Constants that describe the results summary the find panel UI includes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
enum SearchResultDisplayStyle
```

## Topics

### Constants
- [UIFindSession.SearchResultDisplayStyle.currentAndTotal](uifindsession/searchresultdisplaystyle-swift.enum/currentandtotal.md)
  The find panel includes the total number of results the session reports and the index of the target result.
- [UIFindSession.SearchResultDisplayStyle.total](uifindsession/searchresultdisplaystyle-swift.enum/total.md)
  The find panel includes the total number of results the session reports.
- [UIFindSession.SearchResultDisplayStyle.none](uifindsession/searchresultdisplaystyle-swift.enum/none.md)
  The find panel doesn’t include the number of results the session reports.
### Initializers
- [init?(rawValue: Int)](uifindsession/searchresultdisplaystyle-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIFindInteraction](uifindinteraction.md)
  An interaction that provides text finding and replacing operations using a system find panel.
- [protocol UIFindInteractionDelegate](uifindinteractiondelegate.md)
  A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/searchresultdisplaystyle-swift.enum)*