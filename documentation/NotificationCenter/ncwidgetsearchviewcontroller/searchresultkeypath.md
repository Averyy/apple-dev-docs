# searchResultKeyPath

**Framework**: Notification Center  
**Kind**: property  
**Role**: Instance Property

A key path for the string property to display for each object in the search results array.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
var searchResultKeyPath: String? { get set }
```

```objc
@property (copy, nullable) NSString * searchResultKeyPath;
```

#### Discussion

The search view controller uses the key path to find the textual description of each object in [`searchResults`](./searchresults.md). The default value of this property is “description”.

## See Also

### Displaying Search Results
- [var searchResults: [Any]?](./searchresults.md)
  An array of search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller/searchresultkeypath)*