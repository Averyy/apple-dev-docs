# UIFindSession

**Framework**: UIKit  
**Kind**: class

An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIFindSession
```

#### Overview

You return a session object from the delegate of a [`UIFindInteraction`](uifindinteraction.md) to manage the state, presentation, and behavior for a given search. The session object responds to navigation and replacement requests through its [`highlightNextResult(in:)`](uifindsession/highlightnextresult(in:).md) and [`performSingleReplacement(query:replacementString:options:)`](uifindsession/performsinglereplacement(query:replacementstring:options:).md) methods. It also provides presentation information to the system find panel through [`resultCount`](uifindsession/resultcount.md) and [`highlightedResultIndex`](uifindsession/highlightedresultindex.md).

UIKit can manage the state when you implement the [`UITextSearching`](uitextsearching-53wjq.md) protocol on a class that encapsulates the searchable content. To do this, create an instance of [`UITextSearchingFindSession`](uitextsearchingfindsession.md) and provide it a [`searchableObject`](uitextsearchingfindsession/searchableobject.md) using an instance of your class.

If you want to manage the state yourself or already have a class that implements find and replace for your app, you can subclass [`UIFindSession`](uifindsession.md) to bridge your custom implementation to the system UI.

## Topics

### Getting session information
- [var resultCount: Int](uifindsession/resultcount.md)
  The total number of results the search matches.
- [var highlightedResultIndex: Int](uifindsession/highlightedresultindex.md)
  The index of the result the find panel highlights.
- [var supportsReplacement: Bool](uifindsession/supportsreplacement.md)
  A Boolean value that indicates whether to allow replacing find panel results.
- [var allowsReplacementForCurrentlyHighlightedResult: Bool](uifindsession/allowsreplacementforcurrentlyhighlightedresult.md)
  A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.
- [var searchResultDisplayStyle: UIFindSession.SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.property.md)
  The information the find panel includes in the summary of found results.
- [UIFindSession.SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md)
  Constants that describe the results summary the find panel UI includes.
### Managing session interactions
- [func performSearch(query: String, options: UITextSearchOptions?)](uifindsession/performsearch(query:options:).md)
  Initiates a search for the query string you provide.
- [func performSingleReplacement(query: String, replacementString: String, options: UITextSearchOptions?)](uifindsession/performsinglereplacement(query:replacementstring:options:).md)
  Replaces a single instance of the query string with the replacement string you provide.
- [func replaceAll(searchQuery: String, replacementString: String, options: UITextSearchOptions?)](uifindsession/replaceall(searchquery:replacementstring:options:).md)
  Replaces all matching instances of the query string with the replacement string you provide.
- [func highlightNextResult(in: UITextStorageDirection)](uifindsession/highlightnextresult(in:).md)
  Updates the highlighted result to the next or previous match.
- [func invalidateFoundResults()](uifindsession/invalidatefoundresults.md)
  Invalidates the found ranges and updates the system find panel.
### Deprecated
- [var allowsReplacement: Bool](uifindsession/allowsreplacement.md)
  A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UITextSearchingFindSession](uitextsearchingfindsession.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIFindInteraction](uifindinteraction.md)
  An interaction that provides text finding and replacing operations using a system find panel.
- [protocol UIFindInteractionDelegate](uifindinteractiondelegate.md)
  A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession)*