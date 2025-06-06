# string

**Framework**: FSKit  
**Kind**: property

The filename, represented as a Unicode string.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var string: String? { get }
```

#### Discussion

If the value of the filename’s [`data`](fsfilename/data.md) is not a valid UTF-8 byte sequence, this property is empty.

## See Also

- [var data: Data](fsfilename/data.md)
  The byte sequence of the filename, as a data object.
- [var debugDescription: String](fsfilename/debugdescription.md)
  The filename, represented as a potentially lossy conversion to a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilename/string)*