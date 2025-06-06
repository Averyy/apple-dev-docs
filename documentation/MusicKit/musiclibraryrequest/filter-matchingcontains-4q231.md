# filter(matching:contains:)

**Framework**: MusicKit  
**Kind**: method

Filters items by a given optional property that contains a specific string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
mutating func filter(matching keyPath: KeyPath<MusicItemType.LibraryFilter, String?>, contains text: String)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibraryrequest/filter(matching:contains:)-4q231)*