# title

**Framework**: BrowserKit  
**Kind**: property  
**Role**: Instance Property

A localized title for a visited page.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var title: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * title;
```

## See Also

### Accessing visit properties
- [var dateOfLastVisit: Date](./dateoflastvisit.md)
  The date of the person’s last page visit.
- [var httpGet: Bool](./httpget.md)
  A Boolean value that indicates whether the visit is an HTTP GET request.
- [var loadedSuccessfully: Bool](./loadedsuccessfully.md)
  A Boolean value that indicates whether the page loads without errors.
- [var url: URL](./url.md)
  A URL for the visited page.
- [var visitCount: Int](./visitcount.md)
  A count of how many visits the page received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdatahistoryvisit/title)*