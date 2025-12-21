# shareURLs

**Framework**: CloudKit  
**Kind**: property

The URLs of the shares to request access to.

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
var shareURLs: [URL]? { get set }
```

#### Discussion

Include multiple URLs to request access to multiple shares simultaneously. The server processes each URL independently.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharerequestaccessoperation/shareurls)*