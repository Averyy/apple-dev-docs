# mediaGroups(forIdentifiers:)

**Framework**: Media Library  
**Kind**: method

Returns the media groups with the specified identifiers.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```swift
func mediaGroups(forIdentifiers mediaGroupIdentifiers: [String]) -> [String : MLMediaGroup]
```

#### Return Value

A dictionary of media groups matching the specified identifiers.

#### Discussion

The media source must have finished loading before this method returns valid data. Specifically, the root media group must be available before the lookup methods will succeed. Otherwise, the return value is undefined.

## Parameters

- `mediaGroupIdentifiers`: An array of media group identifiers to search for in the source.

## See Also

- [func mediaGroup(forIdentifier: String) -> MLMediaGroup?](mlmediasource/mediagroup(foridentifier:).md)
  Returns the media group with the specified identifier.
- [func mediaObject(forIdentifier: String) -> MLMediaObject?](mlmediasource/mediaobject(foridentifier:).md)
  Returns the media object with the specified identifier.
- [func mediaObjects(forIdentifiers: [String]) -> [String : MLMediaObject]](mlmediasource/mediaobjects(foridentifiers:).md)
  Returns the media objects with the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediasource/mediagroups(foridentifiers:))*