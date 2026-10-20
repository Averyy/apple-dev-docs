# visitCount

**Framework**: BrowserKit  
**Kind**: property  
**Role**: Instance Property

A count of how many visits the page received.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var visitCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger visitCount;
```

## See Also

### Accessing visit properties
- [var dateOfLastVisit: Date](./dateoflastvisit.md)
  The date of the person’s last page visit.
- [var httpGet: Bool](./httpget.md)
  A Boolean value that indicates whether the visit is an HTTP GET request.
- [var loadedSuccessfully: Bool](./loadedsuccessfully.md)
  A Boolean value that indicates whether the page loads without errors.
- [var title: String?](./title.md)
  A localized title for a visited page.
- [var url: URL](./url.md)
  A URL for the visited page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdatahistoryvisit/visitcount)*