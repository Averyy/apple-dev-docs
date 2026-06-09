# FSExtentType.zeroFill

**Framework**: FSKit  
**Kind**: case

An extent type to indicate uninitialized data.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case zeroFill
```

#### Discussion

Only use this extent type in file systems that support sparse files, and only then to represent ranges in the file that aren’t allocated yet.

## See Also

- [FSExtentType.data](fsextenttype/data.md)
  An extent type to indicate valid data.
- [FSExtentType.readOnly](fsextenttype/readonly.md)
  An extent type to indicate read-only data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsextenttype/zerofill)*