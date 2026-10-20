# init(fileDescriptor:closeOnDealloc:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates and returns a file handle object associated with the specified file descriptor and deallocation policy.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(fileDescriptor fd: Int32, closeOnDealloc closeopt: Bool)
```

```objc
- (instancetype) initWithFileDescriptor:(int) fd closeOnDealloc:(BOOL) closeopt;
```

#### Return Value

An initialized file handle object.

#### Discussion

If `flag` is [`false`](../../Swift/false.md), the file descriptor you pass in to this method isn’t owned by the file handle object. In such a case, you’re responsible for closing the file descriptor at some point after disposing of the file handle object. If you want the file handle object to close the descriptor for you automatically, pass [`true`](../../Swift/true.md) for the `flag` parameter.

## Parameters

- `fd`: The POSIX file descriptor with which to initialize the file handle.
- `closeopt`: [`true`](../../Swift/true.md) if the returned file handle object should take ownership of the file descriptor and close it for you or [`false`](../../Swift/false.md) if you want to maintain ownership of the file descriptor.

## See Also

### Related Documentation
- [func closeFile()](./closefile%28%29.md)
  Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing.
### Creating a file handle
- [convenience init(fileDescriptor: Int32)](./init%28filedescriptor%29.md)
  Creates and returns a file handle object associated with the specified file descriptor.
- [convenience init?(forReadingAtPath: String)](./init%28forreadingatpath%29.md)
  Returns a file handle initialized for reading the file, device, or named socket at the specified path.
- [convenience init(forReadingFromURL: URL) throws](./init%28forreadingfromurl%29.md)
  Returns a file handle initialized for reading the file, device, or named socket at the specified URL.
- [convenience init?(forWritingAtPath: String)](./init%28forwritingatpath%29.md)
  Returns a file handle initialized for writing to the file, device, or named socket at the specified path.
- [convenience init(forWritingToURL: URL) throws](./init%28forwritingtourl%29.md)
  Returns a file handle initialized for writing to the file, device, or named socket at the specified URL.
- [convenience init?(forUpdatingAtPath: String)](./init%28forupdatingatpath%29.md)
  Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified path.
- [convenience init(forUpdatingURL: URL) throws](./init%28forupdatingurl%29.md)
  Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified URL.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Returns a file handle initialized from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/init(filedescriptor:closeondealloc:))*