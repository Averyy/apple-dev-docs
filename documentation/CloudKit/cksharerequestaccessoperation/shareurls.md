# shareURLs

**Framework**: CloudKit  
**Kind**: property

The share URLs for which access is being requested.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var shareURLs: [URL]? { get set }
```

#### Discussion

If requesting access to multiple shares, include multiple `NSURL` objects. The server processes them independently.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharerequestaccessoperation/shareurls)*