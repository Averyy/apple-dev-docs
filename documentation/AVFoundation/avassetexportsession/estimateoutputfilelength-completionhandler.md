# estimateOutputFileLength(completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Starts estimating the output file length of the export while considering the asset, preset, and time range configuration of the export session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var estimatedOutputFileLengthInBytes: Int64 { get async throws }
```

## Parameters

- `handler`: A callback the system invokes when it finishes its estimation. It passes the callback the following parameters:

## See Also

- [var estimatedOutputFileLength: Int64](avassetexportsession/estimatedoutputfilelength.md)
  The estimated length of the exported file, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/estimateoutputfilelength(completionhandler:))*