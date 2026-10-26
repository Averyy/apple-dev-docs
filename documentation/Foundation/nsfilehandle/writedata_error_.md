# writeData:error:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Writes the specified data synchronously to the file handle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (BOOL) writeData:(NSData *) data error:(NSError **) error;
```

#### Return Value

Returns [`true`](../../Swift/true.md) when the data is successfullly written to the file handle.

#### Discussion

If the handle represents a file, writing takes place at the file pointer’s current position. After it writes the data, the method advances the file pointer by the number of bytes written. This method provides an error if the file descriptor is closed or isn’t valid, if the handle represents an unconnected pipe or socket endpoint, if there isn’t any free space on the file system, or if any other writing error occurs.

## Parameters

- `data`: The data to write to the file handle.
- `error`: When the return value is [`false`](../../Swift/false.md), this provides an [`NSError`](../nserror.md) indicating why the write operation failed.

## See Also

### Related Documentation
- [var availableData: Data](../filehandle/availabledata.md)
  The data currently available in the receiver.
- [- readDataUpToLength:error:](./readdatauptolength_error_.md)
  Reads data synchronously up to the specified number of bytes.
- [- readDataToEndOfFileAndReturnError:](./readdatatoendoffileandreturnerror_.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilehandle/writedata:error:)*