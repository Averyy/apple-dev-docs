# showSearchResults(forQueryString:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays a Spotlight search results window in Finder for the specified query string.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func showSearchResults(forQueryString queryString: String) -> Bool
```

```objc
- (BOOL) showSearchResultsForQueryString:(NSString *) queryString;
```

## Return Value

[`true`](../../Swift/true.md) if the method communicated successfully with Finder; otherwise, [`false`](../../Swift/false.md).

## Discussion

Finder becomes the active app, if possible. The user can further refine the search via the Finder user interface.

You can safely call this method from any thread of your app.

## Parameters

- `queryString`: The string to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/showsearchresults(forquerystring:))*