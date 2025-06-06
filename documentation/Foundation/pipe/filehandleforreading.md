# fileHandleForReading

**Framework**: Foundation  
**Kind**: property

The receiver’s read file handle.

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
var fileHandleForReading: FileHandle { get }
```

#### Discussion

The descriptor represented by this object is deleted, and the object itself is automatically deallocated when the receiver is deallocated.

You use the returned file handle to read from the pipe using `NSFileHandle`’s read methods—[`availableData`](filehandle/availabledata.md), [`readDataToEndOfFile()`](filehandle/readdatatoendoffile().md), and [`readData(ofLength:)`](filehandle/readdata(oflength:).md).

You don’t need to send [`closeFile()`](filehandle/closefile().md) to this object or explicitly release the object after you have finished using it.

## See Also

- [var fileHandleForWriting: FileHandle](pipe/filehandleforwriting.md)
  The receiver’s write file handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/pipe/filehandleforreading)*