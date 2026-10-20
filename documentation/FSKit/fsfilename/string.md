# string

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The filename, represented as a Unicode string.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var string: String? { get }
```

```objc
@property (readonly, nullable) NSString * string;
```

#### Discussion

If the value of the filename’s [`data`](./data.md) is not a valid UTF-8 byte sequence, this property is empty.

## See Also

### Accessing filename properties
- [var data: Data](./data.md)
  The byte sequence of the filename, as a data object.
- [var debugDescription: String](./debugdescription.md)
  The filename, represented as a potentially lossy conversion to a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilename/string)*