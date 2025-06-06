# canonicalWebPageURL

**Framework**: ARKit  
**Kind**: property

The web URL to share when the user invokes the share sheet.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var canonicalWebPageURL: URL? { get set }
```

#### Discussion

The default value is `nil`, which indicates that Quick Look shares the USDZ file when the user invokes the iOS share sheet. If you set this property to a web page URL, then Quick Look shares that web resource when the user invokes the share sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arquicklookpreviewitem/canonicalwebpageurl)*