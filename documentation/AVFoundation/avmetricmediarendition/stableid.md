# stableID

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
var stableID: String? { get }
```

```objc
@property (readonly, nullable) NSString * stableID;
```

## Discussion

Provides ID corresponding to the rendition. This is equivalent to the STABLE-RENDITION-ID in the HLS playlist. If not available, value is nil.

## See Also

### Inspecting the rendition
- [var url: URL?](./url.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricmediarendition/stableid)*