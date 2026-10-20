# httpGet

**Framework**: BrowserKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the visit is an HTTP GET request.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var httpGet: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL httpGet;
```

## See Also

### Accessing visit properties
- [var dateOfLastVisit: Date](./dateoflastvisit.md)
  The date of the person’s last page visit.
- [var loadedSuccessfully: Bool](./loadedsuccessfully.md)
  A Boolean value that indicates whether the page loads without errors.
- [var title: String?](./title.md)
  A localized title for a visited page.
- [var url: URL](./url.md)
  A URL for the visited page.
- [var visitCount: Int](./visitcount.md)
  A count of how many visits the page received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdatahistoryvisit/httpget)*