# DISPATCH_IO_STREAM

**Framework**: Dispatch  
**Kind**: var

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var DISPATCH_IO_STREAM: Int32 { get }
```

#### Discussion

The channel represents a linear stream of bytes. Read and write operations are performed serially in the order they were started. Operations always read or write data at the file pointer position that is current when the read or write begins. Read and write operations may be performed simultaneously on the same channel.

Offset values are ignored for channels of this type.

## See Also

- [var DISPATCH_IO_RANDOM: Int32](dispatch_io_random.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_io_stream)*