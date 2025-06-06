# resources

**Framework**: RealityKit  
**Kind**: property

A dictionary of audio resources with user-defined names.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var resources: [String : AudioResource]
```

#### Discussion

The values can be any [`AudioResource`](audioresource.md) type, such as [`AudioFileResource`](audiofileresource.md) or [`AudioFileGroupResource`](audiofilegroupresource.md). In memory, you can also use [`AudioBufferResource`](audiobufferresource.md), but this type doesn’t support serializing to disk or sharing via network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiolibrarycomponent/resources)*