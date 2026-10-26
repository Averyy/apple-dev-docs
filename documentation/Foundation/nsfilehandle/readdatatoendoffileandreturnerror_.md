# readDataToEndOfFileAndReturnError:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Reads the available data synchronously up to the end of file or maximum number of bytes.

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
- (NSData *) readDataToEndOfFileAndReturnError:(NSError **) error;
```

#### Return Value

The data available through the file handle up to the maximum size that can be represented by an [`NSData`](../nsdata.md) object or, if a communications channel, until an end-of-file indicator is returned.

#### Discussion

This method invokes [`readData(ofLength:)`](../filehandle/readdata%28oflength%29.md) as part of its implementation.

## Parameters

- `error`: When the return value is `nil`, this provides an [`NSError`](../nserror.md) indicating why the read operation failed.

## See Also

### Reading from a file handle synchronously
- [var availableData: Data](../filehandle/availabledata.md)
  The data currently available in the receiver.
- [- readDataUpToLength:error:](./readdatauptolength_error_.md)
  Reads data synchronously up to the specified number of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilehandle/readdatatoendoffileandreturnerror:)*