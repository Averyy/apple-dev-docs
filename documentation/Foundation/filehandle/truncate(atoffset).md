# truncate(atOffset:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func truncate(atOffset offset: UInt64) throws
```

```objc
- (BOOL) truncateAtOffset:(unsigned long long) offset error:(NSError **) error;
```

## Discussion

If the file is extended (if `offset` is beyond the current end of file), the added characters are null bytes.

## Parameters

- `offset`: The offset within the file that marks the new end of the file.

## See Also

### Operating on a file
- [func close() throws](./close%28%29.md)
  Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing.
- [func synchronize() throws](./synchronize%28%29.md)
  Causes all in-memory data and attributes of the file represented by the file handle to write to permanent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/truncate(atoffset:))*