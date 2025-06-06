# FSMatchResult.usableButLimited

**Framework**: FSKit  
**Kind**: case

The probe recognizes the resource and is ready to use it, but only in a limited capacity.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case usableButLimited
```

#### Discussion

This match result is appropriate when the file system module identifies the resource’s format but also identifies incompatibilities. For example, if the module determines the resource uses new features that the module doesn’t support, the module may only offer read-only access.

## See Also

- [FSMatchResult.usable](fsmatchresult/usable.md)
  The probe recognizes the resource and is ready to use it.
- [FSMatchResult.recognized](fsmatchresult/recognized.md)
  The probe recognizes the resource but can’t use it.
- [FSMatchResult.notRecognized](fsmatchresult/notrecognized.md)
  The probe doesn’t recognize the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmatchresult/usablebutlimited)*