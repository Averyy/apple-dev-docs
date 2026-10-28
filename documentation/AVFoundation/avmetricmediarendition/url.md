# url

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var url: URL? { get }
```

```objc
@property (readonly, nullable) NSURL * URL;
```

## Discussion

Provides URL corresponding to the rendition’s HLS playlist. If not available, value is nil.

## See Also

### Inspecting the rendition
- [var stableID: String?](./stableid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricmediarendition/url)*