# debugDescription

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The filename, represented as a potentially lossy conversion to a string.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var debugDescription: String { get }
```

```objc
@property (copy, readonly) NSString * debugDescription;
```

#### Discussion

The exact details of the string conversion may change in the future.

## See Also

### Accessing filename properties
- [var data: Data](./data.md)
  The byte sequence of the filename, as a data object.
- [var string: String?](./string.md)
  The filename, represented as a Unicode string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilename/debugdescription)*