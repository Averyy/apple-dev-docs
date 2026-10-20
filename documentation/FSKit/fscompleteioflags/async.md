# async

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

A flag that requests that the file system module flush metadata I/O asynchronously.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var async: FSCompleteIOFlags { get }
```

```c
FSCompleteIOFlagsAsync
```

## See Also

### Declaring I/O completion behaviors
- [static var read: FSCompleteIOFlags](./read.md)
  A flag that describes a read operation.
- [static var write: FSCompleteIOFlags](./write.md)
  A flag that describes a write operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscompleteioflags/async)*