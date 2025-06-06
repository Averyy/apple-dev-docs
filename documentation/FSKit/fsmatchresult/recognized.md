# FSMatchResult.recognized

**Framework**: FSKit  
**Kind**: case

The probe recognizes the resource but can’t use it.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case recognized
```

#### Discussion

This match result is appropriate when the file system module identifies the resource’s format but can’t use it. For example, if the resource uses a newer version than the module supports, the module can name the resource but can’t safely do anything with it.

## See Also

- [FSMatchResult.usable](fsmatchresult/usable.md)
  The probe recognizes the resource and is ready to use it.
- [FSMatchResult.usableButLimited](fsmatchresult/usablebutlimited.md)
  The probe recognizes the resource and is ready to use it, but only in a limited capacity.
- [FSMatchResult.notRecognized](fsmatchresult/notrecognized.md)
  The probe doesn’t recognize the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmatchresult/recognized)*