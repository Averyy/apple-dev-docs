# read

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

A flag that describes a read operation.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var read: FSCompleteIOFlags { get }
```

```c
FSCompleteIOFlagsRead
```

## See Also

### Declaring I/O completion behaviors
- [static var write: FSCompleteIOFlags](./write.md)
  A flag that describes a write operation.
- [static var async: FSCompleteIOFlags](./async.md)
  A flag that requests that the file system module flush metadata I/O asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscompleteioflags/read)*