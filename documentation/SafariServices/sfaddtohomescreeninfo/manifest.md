# manifest

**Framework**: Safari Services  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- visionOS 2.2+

## Declaration

```swift
@NSCopying
var manifest: BEWebAppManifest { get }
```

```objc
@property (nonatomic, copy, readonly) BEWebAppManifest * manifest;
```

## Discussion

A property for the web app manifest. This is only available to apps that can use BrowserEngineKit.

The web app manifest for the bookmark.

## See Also

### Information about a web app
- [var websiteCookies: [HTTPCookie]](./websitecookies.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfaddtohomescreeninfo/manifest)*