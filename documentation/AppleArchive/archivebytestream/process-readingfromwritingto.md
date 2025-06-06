# process(readingFrom:writingTo:)

**Framework**: Apple Archive  
**Kind**: method

Processes data between two byte streams.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
static func process(readingFrom input: ArchiveByteStream, writingTo output: ArchiveByteStream) throws -> Int64
```

#### Return Value

The number of processed bytes.

#### Discussion

This function reads data from `input` and writes it to `output` until it reaches end-of-file (EOF).

## Parameters

- `input`: The input stream.
- `output`: The output stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/process(readingfrom:writingto:))*