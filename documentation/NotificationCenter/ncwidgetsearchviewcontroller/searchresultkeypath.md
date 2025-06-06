# searchResultKeyPath

**Framework**: Notification Center  
**Kind**: property

A key path for the string property to display for each object in the search results array.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var searchResultKeyPath: String? { get set }
```

#### Discussion

The search view controller uses the key path to find the textual description of each object in [`searchResults`](ncwidgetsearchviewcontroller/searchresults.md). The default value of this property is “description”.

## See Also

- [var searchResults: [Any]?](ncwidgetsearchviewcontroller/searchresults.md)
  An array of search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller/searchresultkeypath)*