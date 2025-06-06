# httpSessionIdentifier

**Framework**: AVFoundation  
**Kind**: property

A session identifier that the asset sends in HTTP requests that it makes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var httpSessionIdentifier: UUID { get }
```

#### Discussion

The asset uses this value to set as the `X-Playback-Session-Id` header of HTTP requests that it creates.

> **Note**:  Copies of an [`AVURLAsset`](avurlasset.md) have the same session identifier as the original asset.

 Copies of an [`AVURLAsset`](avurlasset.md) have the same session identifier as the original asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/httpsessionidentifier)*