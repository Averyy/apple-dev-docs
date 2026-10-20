# init(volumeID:volumeName:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Creates a volume with the given identifier and name.

**Availability**:
- macOS 15.4+

## Declaration

```swift
init(volumeID: FSVolume.Identifier, volumeName: FSFileName)
```

```objc
- (instancetype) initWithVolumeID:(FSVolumeIdentifier *) volumeID volumeName:(FSFileName *) volumeName;
```

## Parameters

- `volumeID`: An [`FSVolume.Identifier`](./identifier.md) to uniquely identify the volume. For a network file system that supports multiple authenticated users, disambiguate the users by using qualifying data in the identifier.
- `volumeName`: A name for the volume.

## See Also

### Creating a volume
- [FSVolume.Identifier](./identifier.md)
  A type that identifies a volume.
- [class FSFileName](../fsfilename.md)
  The name of a file, expressed as a data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/init(volumeid:volumename:))*