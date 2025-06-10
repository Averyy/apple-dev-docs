# completer(_:didFailWithError:)

**Framework**: MapKit  
**Kind**: method

Tells the method when the specified search completer is unable to generate a list of search results.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.4+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func completer(_ completer: MKLocalSearchCompleter, didFailWithError error: any Error)
```

#### Discussion

Use this object to process any errors that occur while generating search results. Even when an error occurs, the search completer starts a new search if it already has a new search string. Depending on the error, you might do nothing or let the user know that you were unable to obtain a list of search completions.

## Parameters

- `completer`: The search completer object reporting the error.
- `error`: The error object containing the reason for the failure.

## See Also

- [func completerDidUpdateResults(MKLocalSearchCompleter)](mklocalsearchcompleterdelegate/completerdidupdateresults(_:).md)
  Tells the method when the specified search completer updates its array of search completions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleterdelegate/completer(_:didfailwitherror:))*