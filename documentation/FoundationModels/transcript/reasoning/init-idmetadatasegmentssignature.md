# init(id:metadata:segments:signature:)

**Framework**: Foundation Models  
**Kind**: init

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(id: String = UUID().uuidString, metadata: [String : any Sendable & Codable & Equatable] = [:], segments: [Transcript.Segment], signature: Data? = nil)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/reasoning/init(id:metadata:segments:signature:))*