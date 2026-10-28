# websiteCookies

**Framework**: Safari Services  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- visionOS 2.2+

## Declaration

```swift
var websiteCookies: [HTTPCookie] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSHTTPCookie *> * websiteCookies;
```

## Discussion

An optional item for providing the website’s cookies. These will be copied to the Home Screen web app’s data store. This will only be used if the manifest is non-nil and a Home Screen web app is created, not a Home Screen Bookmark.

An array of cookies for the system to use when it accesses the web app.

## See Also

### Information about a web app
- [var manifest: BEWebAppManifest](./manifest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfaddtohomescreeninfo/websitecookies)*