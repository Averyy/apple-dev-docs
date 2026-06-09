# assumesHTTP3Capable

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the server is assumed to support HTTP/3.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.4+

## Declaration

```swift
var assumesHTTP3Capable: Bool { get set }
```

#### Discussion

When `YES`, enables QUIC racing without HTTP/3 service discovery. Defaults to `NO`. The default may be `YES` in a future OS update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/assumeshttp3capable)*