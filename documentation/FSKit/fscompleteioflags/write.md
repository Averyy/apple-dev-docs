# write

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

A flag that describes a write operation.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var write: FSCompleteIOFlags { get }
```

```c
FSCompleteIOFlagsWrite
```

## See Also

### Declaring I/O completion behaviors
- [static var read: FSCompleteIOFlags](./read.md)
  A flag that describes a read operation.
- [static var async: FSCompleteIOFlags](./async.md)
  A flag that requests that the file system module flush metadata I/O asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscompleteioflags/write)*