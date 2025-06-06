# FSVolume.SetXattrPolicy.mustCreate

**Framework**: FSKit  
**Kind**: case

Set the value, but fail if the extended attribute already exists.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case mustCreate
```

## See Also

- [FSVolume.SetXattrPolicy.alwaysSet](fsvolume/setxattrpolicy/alwaysset.md)
  Set the value, regardless of previous state.
- [FSVolume.SetXattrPolicy.mustReplace](fsvolume/setxattrpolicy/mustreplace.md)
  Set the value, but fail if the extended attribute doesn’t already exist.
- [FSVolume.SetXattrPolicy.delete](fsvolume/setxattrpolicy/delete.md)
  Delete the value, failing if the extended attribute doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/setxattrpolicy/mustcreate)*