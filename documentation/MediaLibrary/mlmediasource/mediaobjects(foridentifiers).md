# mediaObjects(forIdentifiers:)

**Framework**: Media Library  
**Kind**: method

Returns the media objects with the specified identifiers.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```swift
func mediaObjects(forIdentifiers mediaObjectIdentifiers: [String]) -> [String : MLMediaObject]
```

#### Return Value

A dictionary of media objects matching the specified identifiers.

#### Discussion

The media source must have finished loading before this method returns valid data. Specifically, the root media group must be available before the lookup methods will succeed. Otherwise, the return value is undefined.

## Parameters

- `mediaObjectIdentifiers`: An array of media object identifiers to search for in the source.

## See Also

- [func mediaGroup(forIdentifier: String) -> MLMediaGroup?](mlmediasource/mediagroup(foridentifier:).md)
  Returns the media group with the specified identifier.
- [func mediaGroups(forIdentifiers: [String]) -> [String : MLMediaGroup]](mlmediasource/mediagroups(foridentifiers:).md)
  Returns the media groups with the specified identifiers.
- [func mediaObject(forIdentifier: String) -> MLMediaObject?](mlmediasource/mediaobject(foridentifier:).md)
  Returns the media object with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediasource/mediaobjects(foridentifiers:))*