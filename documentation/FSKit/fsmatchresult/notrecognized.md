# FSMatchResult.notRecognized

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

The probe doesn’t recognize the resource.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case notRecognized
```

```c
FSMatchResultNotRecognized
```

## Discussion

This match result is appropriate when the file system module determines that the resource uses a completely different format.

## See Also

### Working with match results
- [FSMatchResult.usable](./usable.md)
  The probe recognizes the resource and is ready to use it.
- [FSMatchResult.usableButLimited](./usablebutlimited.md)
  The probe recognizes the resource and is ready to use it, but only in a limited capacity.
- [FSMatchResult.recognized](./recognized.md)
  The probe recognizes the resource but can’t use it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmatchresult/notrecognized)*