# preloadsEligibleContentKeys

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether content keys will be loaded as quickly as possible.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var preloadsEligibleContentKeys: Bool { get set }
```

#### Discussion

Set this property to `true` to load eligible keys. This may result in network activity. All work done as a result of setting this property to `true` is performed asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/preloadseligiblecontentkeys)*