# SearchResponse.Links

**Framework**: AppleNewsAPI  
**Kind**: dictionary  
**Role**: Object

See the links the search article endpoints returned.

**Availability**:
- Apple News API 1.0+

## Declaration

```
object SearchResponse.Links
```

## Properties

- `self` (string): The URL for the current page of search results.
- `next` (string): The URL for the next page of search results. If `next` is null, there are no more pages. The `next` link may occasionally return an empty page of results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsapi/searchresponse/links-data.dictionary)*