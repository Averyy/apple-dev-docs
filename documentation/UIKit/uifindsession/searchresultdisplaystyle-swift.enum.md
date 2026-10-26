# UIFindSession.SearchResultDisplayStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UIFindSessionSearchResultDisplayStyle : NSInteger;
```

## Topics

### Constants
- [UIFindSession.SearchResultDisplayStyle.currentAndTotal](./searchresultdisplaystyle-swift.enum/currentandtotal.md)
  The find panel includes the total number of results the session reports and the index of the target result.
- [UIFindSession.SearchResultDisplayStyle.total](./searchresultdisplaystyle-swift.enum/total.md)
  The find panel includes the total number of results the session reports.
- [UIFindSession.SearchResultDisplayStyle.none](./searchresultdisplaystyle-swift.enum/none.md)
  The find panel doesn’t include the number of results the session reports.
### Initializers
- [init?(rawValue: Int)](./searchresultdisplaystyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Find and replace
- [class UIFindInteraction](../uifindinteraction.md)
  An interaction that provides text finding and replacing operations using a system find panel.
- [protocol UIFindInteractionDelegate](../uifindinteractiondelegate.md)
  A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.
- [class UIFindSession](../uifindsession.md)
  An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.
- [class UITextSearchingFindSession](../uitextsearchingfindsession.md)
  A find session object that wraps a searchable object implementing the text-searching protocol.
- [protocol UITextSearching](../uitextsearching-3wkjv.md)
  The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.
- [class UITextSearchOptions](../uitextsearchoptions.md)
  An object containing the configurable options for a text search.
- [enum UITextSearchFoundTextStyle](../uitextsearchfoundtextstyle.md)
  Constants that describe the style a find session uses to decorate the text.
- [UITextSearchOptions.WordMatchMethod](../uitextsearchoptions/wordmatchmethod-swift.enum.md)
  Constants that describe the method to use when searching text for words that match a string.
- [UITextSearching](../uitextsearching-53wjq.md)
  The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/searchresultdisplaystyle-swift.enum)*