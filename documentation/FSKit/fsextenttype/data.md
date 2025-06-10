# FSExtentType.data

**Framework**: FSKit  
**Kind**: case

An extent type to indicate valid data.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case data
```

#### Discussion

Use this type for all extents on a file system that doesn’t support sparse files.

> 💡 **Tip**: The kernel keeps track of the end of file, so it knows a range of `[EOF, allocated space]` is uninitialized. Because of this behavior, it’s valid to pass the data extent type for such a range.

## See Also

- [FSExtentType.zeroFill](fsextenttype/zerofill.md)
  An extent type to indicate uninitialized data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsextenttype/data)*