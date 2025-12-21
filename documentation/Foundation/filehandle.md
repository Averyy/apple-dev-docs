# FileHandle

**Framework**: Foundation  
**Kind**: class

An object-oriented wrapper for a file descriptor.

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
class FileHandle
```

## Mentions

- [About Apple File System](about-apple-file-system.md)

#### Overview

You use file handle objects to access data associated with files, sockets, pipes, and devices. For files, you can read, write, and seek within the file. For sockets, pipes, and devices, you can use a file handle object to monitor the device and process data asynchronously.

Most creation methods for [`FileHandle`](filehandle.md) cause the file handle object to take ownership of the associated file descriptor. This means that the file handle object both creates the file descriptor and is responsible for closing it later, usually when the system deallocates the file handle object. If you want to use a file handle object with a file descriptor that you created, use the [`init(fileDescriptor:)`](filehandle/init(filedescriptor:).md) method or use the [`init(fileDescriptor:closeOnDealloc:)`](filehandle/init(filedescriptor:closeondealloc:).md) method and pass [`false`](https://developer.apple.com/documentation/Swift/false) for the `flag` parameter.

##### Run Loop Considerations

When using a file handle object to communicate asynchronously with a socket, you must initiate the corresponding operations from a thread with an active run loop. Although the read, accept, and wait operations themselves are performed asynchronously on background threads, the file handle uses a run loop source to monitor the operations and notify your code appropriately. Therefore, you must call those methods from your application’s main thread or from any thread where you’ve configured a run loop and are using it to process events.

## Topics

### Creating a File Handle
- [convenience init(fileDescriptor: Int32)](filehandle/init(filedescriptor:).md)
  Creates and returns a file handle object associated with the specified file descriptor.
- [init(fileDescriptor: Int32, closeOnDealloc: Bool)](filehandle/init(filedescriptor:closeondealloc:).md)
  Creates and returns a file handle object associated with the specified file descriptor and deallocation policy.
- [convenience init?(forReadingAtPath: String)](filehandle/init(forreadingatpath:).md)
  Returns a file handle initialized for reading the file, device, or named socket at the specified path.
- [convenience init(forReadingFromURL: URL) throws](filehandle/init(forreadingfromurl:).md)
  Returns a file handle initialized for reading the file, device, or named socket at the specified URL.
- [convenience init?(forWritingAtPath: String)](filehandle/init(forwritingatpath:).md)
  Returns a file handle initialized for writing to the file, device, or named socket at the specified path.
- [convenience init(forWritingToURL: URL) throws](filehandle/init(forwritingtourl:).md)
  Returns a file handle initialized for writing to the file, device, or named socket at the specified URL.
- [convenience init?(forUpdatingAtPath: String)](filehandle/init(forupdatingatpath:).md)
  Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified path.
- [convenience init(forUpdatingURL: URL) throws](filehandle/init(forupdatingurl:).md)
  Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified URL.
- [init?(coder: NSCoder)](filehandle/init(coder:).md)
  Returns a file handle initialized from data in an unarchiver.
### Getting a File Handle
- [class var standardError: FileHandle](filehandle/standarderror.md)
  The file handle associated with the standard error file.
- [class var standardInput: FileHandle](filehandle/standardinput.md)
  The file handle associated with the standard input file.
- [class var standardOutput: FileHandle](filehandle/standardoutput.md)
  The file handle associated with the standard output file.
- [class var nullDevice: FileHandle](filehandle/nulldevice.md)
  The file handle associated with a null device.
### Getting a File Descriptor
- [var fileDescriptor: Int32](filehandle/filedescriptor.md)
  The POSIX file descriptor associated with the receiver.
### Reading from a File Handle Asynchronously
- [var bytes: FileHandle.AsyncBytes](filehandle/bytes.md)
  The file’s contents, as an asynchronous sequence of bytes.
- [FileHandle.AsyncBytes](filehandle/asyncbytes.md)
  An asynchronous sequence of bytes.
### Reading from a File Handle Synchronously
- [var availableData: Data](filehandle/availabledata.md)
  The data currently available in the receiver.
- [func readToEnd() throws -> Data?](filehandle/readtoend.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.
- [func read(upToCount: Int) throws -> Data?](filehandle/read(uptocount:).md)
  Reads data synchronously up to the specified number of bytes.
### Reading Asynchronously with Notifications
- [func acceptConnectionInBackgroundAndNotify()](filehandle/acceptconnectioninbackgroundandnotify.md)
  Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
- [func acceptConnectionInBackgroundAndNotify(forModes: [RunLoop.Mode]?)](filehandle/acceptconnectioninbackgroundandnotify(formodes:).md)
  Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
- [func readInBackgroundAndNotify()](filehandle/readinbackgroundandnotify.md)
  Reads from the file or communications channel in the background and posts a notification when finished.
- [func readInBackgroundAndNotify(forModes: [RunLoop.Mode]?)](filehandle/readinbackgroundandnotify(formodes:).md)
  Reads from the file or communications channel in the background and posts a notification when finished.
- [func readToEndOfFileInBackgroundAndNotify()](filehandle/readtoendoffileinbackgroundandnotify.md)
  Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [func readToEndOfFileInBackgroundAndNotify(forModes: [RunLoop.Mode]?)](filehandle/readtoendoffileinbackgroundandnotify(formodes:).md)
  Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [func waitForDataInBackgroundAndNotify()](filehandle/waitfordatainbackgroundandnotify.md)
  Asynchronously checks to see if data is available.
- [func waitForDataInBackgroundAndNotify(forModes: [RunLoop.Mode]?)](filehandle/waitfordatainbackgroundandnotify(formodes:).md)
  Asynchronously checks to see if data is available.
### Writing to a File Handle
- [func write<T>(contentsOf: T) throws](filehandle/write(contentsof:).md)
  Writes the specified data synchronously to the file handle.
### Seeking Within a File
- [func offset() throws -> UInt64](filehandle/offset.md)
  Gets the position of the file pointer within the file.
- [func seekToEnd() throws -> UInt64](filehandle/seektoend.md)
  Places the file pointer at the end of the file referenced by the file handle and returns the new file offset.
- [func seek(toOffset: UInt64) throws](filehandle/seek(tooffset:).md)
  Moves the file pointer to the specified offset within the file.
### Operating on a File
- [func close() throws](filehandle/close.md)
  Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing.
- [func synchronize() throws](filehandle/synchronize.md)
  Causes all in-memory data and attributes of the file represented by the file handle to write to permanent storage.
- [func truncate(atOffset: UInt64) throws](filehandle/truncate(atoffset:).md)
  Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position.
### Monitoring for Readability and Writability
- [var readabilityHandler: ((FileHandle) -> Void)?](filehandle/readabilityhandler.md)
  The block to use for reading the contents of the file handle asynchronously.
- [var writeabilityHandler: ((FileHandle) -> Void)?](filehandle/writeabilityhandler.md)
  The block to use for writing the contents of the file handle asynchronously.
### Constants
- [Keys for Notification UserInfo Dictionary](keys-for-notification-userinfo-dictionary.md)
  Strings that the system uses as keys in a userinfo dictionary during a file handle notification.
- [Exception Names](exception-names.md)
  Constant that defines the name of a file operation exception.
### Notifications
- [static let NSFileHandleConnectionAccepted: NSNotification.Name](nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md)
  Posted when a file handle object establishes a socket connection between two processes, creates a file handle object for one end of the connection, and makes this object available to observers.
- [static let NSFileHandleDataAvailable: NSNotification.Name](nsnotification/name-swift.struct/nsfilehandledataavailable.md)
  Posted when the file handle determines that data is currently available for reading in a file or at a communications channel.
- [class let readCompletionNotification: NSNotification.Name](filehandle/readcompletionnotification.md)
  Posted when the file handle reads the data currently available in a file or at a communications channel.
- [static let NSFileHandleReadToEndOfFileCompletion: NSNotification.Name](nsnotification/name-swift.struct/nsfilehandlereadtoendoffilecompletion.md)
  Posted when the file handle reads all data in the file or, in a communications channel, until the other process signals the end of data.
### Deprecated
- [func readDataToEndOfFile() -> Data](filehandle/readdatatoendoffile.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.
- [func readData(ofLength: Int) -> Data](filehandle/readdata(oflength:).md)
  Reads data synchronously up to the specified number of bytes.
- [func write(Data)](filehandle/write(_:).md)
  Writes the specified data synchronously to the file handle.
- [var offsetInFile: UInt64](filehandle/offsetinfile.md)
  The position of the file pointer within the file represented by the file handle.
- [func seekToEndOfFile() -> UInt64](filehandle/seektoendoffile.md)
  Places the file pointer at the end of the file referenced by the file handle and returns the new file offset.
- [func seek(toFileOffset: UInt64)](filehandle/seek(tofileoffset:).md)
  Moves the file pointer to the specified offset within the file represented by the receiver.
- [func closeFile()](filehandle/closefile.md)
  Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing.
- [func synchronizeFile()](filehandle/synchronizefile.md)
  Causes all in-memory data and attributes of the file represented by the handle to write to permanent storage.
- [func truncateFile(atOffset: UInt64)](filehandle/truncatefile(atoffset:).md)
  Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position.
- [let NSFileHandleNotificationMonitorModes: String](nsfilehandlenotificationmonitormodes.md)
  Currently unused.
### Structures
- [FileHandle.ConnectionAcceptedMessage](filehandle/connectionacceptedmessage.md)
- [FileHandle.DataAvailableMessage](filehandle/dataavailablemessage.md)
- [FileHandle.ReadCompletionMessage](filehandle/readcompletionmessage.md)
- [FileHandle.ReadToEndOfFileCompletionMessage](filehandle/readtoendoffilecompletionmessage.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSFileSecurity](nsfilesecurity.md)
  A stub class that encapsulates security information about a file.
- [class NSFileVersion](nsfileversion.md)
  A snapshot of a file at a specific point in time.
- [class FileWrapper](filewrapper.md)
  A representation of a node (a file, directory, or symbolic link) in the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle)*