# redirectDestinationURL

**Framework**: BrowserKit  
**Kind**: property  
**Role**: Instance Property

A URL to which the visit redirects.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var redirectDestinationURL: URL? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSURL * redirectDestinationURL;
```

## See Also

### Managing redirect information
- [var redirectDestinationDateOfVisit: Date?](./redirectdestinationdateofvisit.md)
  The date of the redirect destination visit.
- [var redirectSourceDateOfVisit: Date?](./redirectsourcedateofvisit.md)
  The date of the redirect source visit.
- [var redirectSourceURL: URL?](./redirectsourceurl.md)
  A URL that redirects to the visited page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdatahistoryvisit/redirectdestinationurl)*