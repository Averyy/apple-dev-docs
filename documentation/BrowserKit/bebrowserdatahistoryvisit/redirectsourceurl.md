# redirectSourceURL

**Framework**: BrowserKit  
**Kind**: property  
**Role**: Instance Property

A URL that redirects to the visited page.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var redirectSourceURL: URL? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSURL * redirectSourceURL;
```

## Mentions

- [Transferring browsing data to another browser](../transferring-browsing-data-to-another-browser.md)

## See Also

### Managing redirect information
- [var redirectDestinationDateOfVisit: Date?](./redirectdestinationdateofvisit.md)
  The date of the redirect destination visit.
- [var redirectDestinationURL: URL?](./redirectdestinationurl.md)
  A URL to which the visit redirects.
- [var redirectSourceDateOfVisit: Date?](./redirectsourcedateofvisit.md)
  The date of the redirect source visit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdatahistoryvisit/redirectsourceurl)*