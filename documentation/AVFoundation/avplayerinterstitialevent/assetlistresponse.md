# assetListResponse

**Framework**: AVFoundation  
**Kind**: property

The asset list JSON response as a dictionary.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
var assetListResponse: [AnyHashable : any Sendable]? { get }
```

#### Discussion

The value of this property is `nil` if there is no asset list loaded for the event. If this value is `nil` and the event’s [`templateItems`](avplayerinterstitialevent/templateitems.md) is empty, then an asset list read is expected. If this value is `nil` and [`templateItems`](avplayerinterstitialevent/templateitems.md) isn’t empty, an asset list read isn’t expected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/assetlistresponse)*