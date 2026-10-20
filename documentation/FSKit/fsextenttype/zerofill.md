# FSExtentType.zeroFill

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

An extent type to indicate uninitialized data.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case zeroFill
```

```c
FSExtentTypeZeroFill
```

#### Discussion

Only use this extent type in file systems that support sparse files, and only then to represent ranges in the file that aren’t allocated yet.

## See Also

### Working with extent types
- [FSExtentType.data](./data.md)
  An extent type to indicate valid data.
- [FSExtentType.readOnly](./readonly.md)
  An extent type to indicate read-only data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsextenttype/zerofill)*