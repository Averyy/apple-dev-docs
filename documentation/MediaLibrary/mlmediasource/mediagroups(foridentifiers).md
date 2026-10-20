# mediaGroups(forIdentifiers:)

**Framework**: Media Library  
**Kind**: method  
**Role**: Instance Method

Returns the media groups with the specified identifiers.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
func mediaGroups(forIdentifiers mediaGroupIdentifiers: [String]) -> [String : MLMediaGroup]
```

```objc
- (NSDictionary<NSString *,MLMediaGroup *> *) mediaGroupsForIdentifiers:(NSArray<NSString *> *) mediaGroupIdentifiers;
```

#### Return Value

A dictionary of media groups matching the specified identifiers.

#### Discussion

The media source must have finished loading before this method returns valid data. Specifically, the root media group must be available before the lookup methods will succeed. Otherwise, the return value is undefined.

## Parameters

- `mediaGroupIdentifiers`: An array of media group identifiers to search for in the source.

## See Also

### Accessing Media
- [func mediaGroup(forIdentifier: String) -> MLMediaGroup?](./mediagroup%28foridentifier%29.md)
  Returns the media group with the specified identifier.
- [func mediaObject(forIdentifier: String) -> MLMediaObject?](./mediaobject%28foridentifier%29.md)
  Returns the media object with the specified identifier.
- [func mediaObjects(forIdentifiers: [String]) -> [String : MLMediaObject]](./mediaobjects%28foridentifiers%29.md)
  Returns the media objects with the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediasource/mediagroups(foridentifiers:))*