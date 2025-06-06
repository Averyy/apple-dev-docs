# nextBatch(limit:)

**Framework**: MusicKit  
**Kind**: method

Fetches the next batch of items asynchronously.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func nextBatch(limit: Int? = nil) async throws -> MusicItemCollection<MusicItemType>? where MusicItemType : Decodable
```

#### Discussion

This method returns the next batch of items as another collection of music items of the same type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicitemcollection/nextbatch(limit:)-432i0)*