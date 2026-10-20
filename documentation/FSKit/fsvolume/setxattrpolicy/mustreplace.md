# FSVolume.SetXattrPolicy.mustReplace

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

Set the value, but fail if the extended attribute doesn’t already exist.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case mustReplace
```

```c
FSSetXattrPolicyMustReplace
```

## See Also

### Declaring a policy
- [FSVolume.SetXattrPolicy.alwaysSet](./alwaysset.md)
  Set the value, regardless of previous state.
- [FSVolume.SetXattrPolicy.mustCreate](./mustcreate.md)
  Set the value, but fail if the extended attribute already exists.
- [FSVolume.SetXattrPolicy.delete](./delete.md)
  Delete the value, failing if the extended attribute doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/setxattrpolicy/mustreplace)*