# sortSections(by:ascending:)

**Framework**: MusicKit  
**Kind**: method

Sorts sections by a specified property.

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
mutating func sortSections<Value>(by keyPath: KeyPath<SectionType.LibrarySortProperties, Value>, ascending: Bool) where SectionType : MusicLibraryRequestable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrarysectionedrequest/sortsections(by:ascending:))*