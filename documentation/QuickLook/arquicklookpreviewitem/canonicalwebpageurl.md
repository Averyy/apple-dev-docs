# canonicalWebPageURL

**Framework**: Quick Look  
**Kind**: property

An optional canonical web page URL for the 3D content that will be shared.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var canonicalWebPageURL: URL? { get set }
```

#### Discussion

If this is supplied, the URL to the canonical web page is shared instead of the 3D content file. For example, providing https://developer.apple.com/arkit/gallery/ as the canonical web page URL string will be shared via the Share button. If the web page URL string is malformed or not provided, then AR Quick Look will default to sharing the 3D content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/arquicklookpreviewitem/canonicalwebpageurl)*