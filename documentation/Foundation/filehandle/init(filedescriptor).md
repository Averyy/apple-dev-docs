# init(fileDescriptor:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates and returns a file handle object associated with the specified file descriptor.

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
convenience init(fileDescriptor fd: Int32)
```

```objc
- (instancetype) initWithFileDescriptor:(int) fd;
```

## Return Value

A file handle initialized with `fileDescriptor`.

## Discussion

The file descriptor you pass in to this method isn’t owned by the file handle object. Therefore, you’re responsible for closing the file descriptor at some point after disposing of the file handle object.

You can create a file handle for a socket by using the result of a `socket` call as `fileDescriptor`.

## Parameters

- `fd`: The POSIX file descriptor with which to initialize the file handle. This descriptor represents an open file or socket that you created previously. For example, when creating a file handle for a socket, you’d pass the value returned by the socket function.

## See Also

### Related Documentation
- [func closeFile()](./closefile%28%29.md)
  Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing.
### Creating a file handle
- [init(fileDescriptor: Int32, closeOnDealloc: Bool)](./init%28filedescriptor,closeondealloc%29.md)
  Creates and returns a file handle object associated with the specified file descriptor and deallocation policy.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/init(filedescriptor:))*