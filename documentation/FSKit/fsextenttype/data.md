# FSExtentType.data

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

An extent type to indicate valid data.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case data
```

```c
FSExtentTypeData
```

#### Discussion

Use this type for all extents on a file system that doesn’t support sparse files.

> 💡 **Tip**: The kernel keeps track of the end of file, so it knows a range of `[EOF, allocated space]` is uninitialized. Because of this behavior, it’s valid to pass the data extent type for such a range.

## See Also

### Working with extent types
- [FSExtentType.zeroFill](./zerofill.md)
  An extent type to indicate uninitialized data.
- [FSExtentType.readOnly](./readonly.md)
  An extent type to indicate read-only data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsextenttype/data)*