# filter(matching:memberOf:)

**Framework**: MusicKit  
**Kind**: method

Filters items by an optional property for an array of possible values.

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
mutating func filter<Value>(matching keyPath: KeyPath<MusicItemType.LibraryFilter, Value?>, memberOf values: [Value?]) where Value : MusicLibraryRequestFilterValueMembershipComparable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibraryrequest/filter(matching:memberof:)-2u2ia)*