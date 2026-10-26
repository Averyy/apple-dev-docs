# AARandomAccessByteStreamProcess

**Framework**: Apple Archive  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```c
off_t AARandomAccessByteStreamProcess(AAByteStream istream, AAByteStream ostream, off_t max_offset, size_t block_size, AAFlagSet flags, int n_threads);
```

## See Also

### Functions
- [AAArchiveStreamAbort](./aaarchivestreamabort.md)
- [AAArchiveStreamCancel](./aaarchivestreamcancel.md)
- [AAArchiveStreamClose](./aaarchivestreamclose.md)
- [AAArchiveStreamProcess](./aaarchivestreamprocess.md)
- [AAArchiveStreamReadBlob](./aaarchivestreamreadblob.md)
- [AAArchiveStreamReadHeader](./aaarchivestreamreadheader.md)
- [AAArchiveStreamWriteBlob](./aaarchivestreamwriteblob.md)
- [AAArchiveStreamWriteHeader](./aaarchivestreamwriteheader.md)
- [AAArchiveStreamWritePathList](./aaarchivestreamwritepathlist.md)
- [AAByteStreamAbort](./aabytestreamabort.md)
- [AAByteStreamCancel](./aabytestreamcancel.md)
- [AAByteStreamClose](./aabytestreamclose.md)
- [AAByteStreamPRead](./aabytestreampread.md)
- [AAByteStreamPWrite](./aabytestreampwrite.md)
- [AAByteStreamProcess](./aabytestreamprocess.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/aarandomaccessbytestreamprocess)*