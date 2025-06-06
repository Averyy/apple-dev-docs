# websiteCookies

**Framework**: Safari Services  
**Kind**: property

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- visionOS 2.2+

## Declaration

```swift
var websiteCookies: [HTTPCookie] { get set }
```

#### Discussion

These will be copied to the Home Screen web app’s data store. This will only be used if the manifest is non-nil and a Home Screen web app is created, not a Home Screen Bookmark.

An array of cookies for the system to use when it accesses the web app.

## See Also

- [var manifest: BEWebAppManifest](sfaddtohomescreeninfo/manifest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfaddtohomescreeninfo/websitecookies)*