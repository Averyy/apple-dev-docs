# FSVolume.SetXattrPolicy.delete

**Framework**: FSKit  
**Kind**: case

Delete the value, failing if the extended attribute doesn’t exist.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case delete
```

## See Also

- [FSVolume.SetXattrPolicy.alwaysSet](fsvolume/setxattrpolicy/alwaysset.md)
  Set the value, regardless of previous state.
- [FSVolume.SetXattrPolicy.mustCreate](fsvolume/setxattrpolicy/mustcreate.md)
  Set the value, but fail if the extended attribute already exists.
- [FSVolume.SetXattrPolicy.mustReplace](fsvolume/setxattrpolicy/mustreplace.md)
  Set the value, but fail if the extended attribute doesn’t already exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/setxattrpolicy/delete)*