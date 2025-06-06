# mediaGroup(forIdentifier:)

**Framework**: Media Library  
**Kind**: method

Returns the media group with the specified identifier.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```swift
func mediaGroup(forIdentifier mediaGroupIdentifier: String) -> MLMediaGroup?
```

#### Discussion

The media source must have finished loading before this method returns valid data. Specifically, the root media group must be available before the lookup methods will succeed. Otherwise, the return value is undefined.

## Parameters

- `mediaGroupIdentifier`: The media group identifier to search for in the source.

## See Also

- [func mediaGroups(forIdentifiers: [String]) -> [String : MLMediaGroup]](mlmediasource/mediagroups(foridentifiers:).md)
  Returns the media groups with the specified identifiers.
- [func mediaObject(forIdentifier: String) -> MLMediaObject?](mlmediasource/mediaobject(foridentifier:).md)
  Returns the media object with the specified identifier.
- [func mediaObjects(forIdentifiers: [String]) -> [String : MLMediaObject]](mlmediasource/mediaobjects(foridentifiers:).md)
  Returns the media objects with the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediasource/mediagroup(foridentifier:))*