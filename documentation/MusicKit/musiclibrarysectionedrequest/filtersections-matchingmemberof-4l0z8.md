# filterSections(matching:memberOf:)

**Framework**: MusicKit  
**Kind**: method

Filters sections by a property for an array of possible values.

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
mutating func filterSections<Value>(matching keyPath: KeyPath<SectionType.LibraryFilter, Value>, memberOf values: [Value]) where SectionType : MusicLibraryRequestable, Value : MusicLibraryRequestFilterValueMembershipComparable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrarysectionedrequest/filtersections(matching:memberof:)-4l0z8)*