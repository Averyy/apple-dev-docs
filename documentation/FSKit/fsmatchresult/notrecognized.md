# FSMatchResult.notRecognized

**Framework**: FSKit  
**Kind**: case

The probe doesn’t recognize the resource.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case notRecognized
```

#### Discussion

This match result is appropriate when the file system module determines that the resource uses a completely different format.

## See Also

- [FSMatchResult.usable](fsmatchresult/usable.md)
  The probe recognizes the resource and is ready to use it.
- [FSMatchResult.usableButLimited](fsmatchresult/usablebutlimited.md)
  The probe recognizes the resource and is ready to use it, but only in a limited capacity.
- [FSMatchResult.recognized](fsmatchresult/recognized.md)
  The probe recognizes the resource but can’t use it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmatchresult/notrecognized)*