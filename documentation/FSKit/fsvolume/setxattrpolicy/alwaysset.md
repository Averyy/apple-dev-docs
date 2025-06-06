# FSVolume.SetXattrPolicy.alwaysSet

**Framework**: FSKit  
**Kind**: case

Set the value, regardless of previous state.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case alwaysSet
```

## See Also

- [FSVolume.SetXattrPolicy.mustCreate](fsvolume/setxattrpolicy/mustcreate.md)
  Set the value, but fail if the extended attribute already exists.
- [FSVolume.SetXattrPolicy.mustReplace](fsvolume/setxattrpolicy/mustreplace.md)
  Set the value, but fail if the extended attribute doesn’t already exist.
- [FSVolume.SetXattrPolicy.delete](fsvolume/setxattrpolicy/delete.md)
  Delete the value, failing if the extended attribute doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/setxattrpolicy/alwaysset)*