# init(volumeID:volumeName:)

**Framework**: FSKit  
**Kind**: init

Creates a volume with the given identifier and name.

**Availability**:
- macOS 15.4+

## Declaration

```swift
init(volumeID: FSVolume.Identifier, volumeName: FSFileName)
```

## Parameters

- `volumeID`: An   to uniquely identify the volume. For a network file system that supports multiple authenticated users, disambiguate the users by using qualifying data in the identifier.
- `volumeName`: A name for the volume.

## See Also

- [FSVolume.Identifier](fsvolume/identifier.md)
  A type that identifies a volume.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/init(volumeid:volumename:))*