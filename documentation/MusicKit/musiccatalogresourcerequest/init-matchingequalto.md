# init(matching:equalTo:)

**Framework**: MusicKit  
**Kind**: init

Creates a request to fetch items using a filter that matches a specific value.

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
init<Value>(matching keyPath: KeyPath<MusicItemType.FilterType, Value>, equalTo value: Value) where MusicItemType : FilterableMusicItem
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogresourcerequest/init(matching:equalto:))*