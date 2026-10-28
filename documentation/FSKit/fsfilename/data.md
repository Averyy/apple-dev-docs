# data

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The byte sequence of the filename, as a data object.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var data: Data { get }
```

```objc
@property (readonly) NSData * data;
```

## Discussion

This property always provides a value.

## See Also

### Accessing filename properties
- [var string: String?](./string.md)
  The filename, represented as a Unicode string.
- [var debugDescription: String](./debugdescription.md)
  The filename, represented as a potentially lossy conversion to a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilename/data)*