# filterItems(matching:equalTo:)

**Framework**: MusicKit  
**Kind**: method

Filters items by a given property that matches a specific value.

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
mutating func filterItems<Value>(matching keyPath: KeyPath<MusicItemType.LibraryFilter, Value>, equalTo value: Value) where Value : MusicLibraryRequestFilterValueEquatable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrarysectionedrequest/filteritems(matching:equalto:)-3zn4r)*