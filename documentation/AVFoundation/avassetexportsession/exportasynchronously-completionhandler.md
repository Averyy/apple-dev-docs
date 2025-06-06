# exportAsynchronously(completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Starts the asynchronous execution of an export session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func export() async
```

## Parameters

- `handler`: A callback the system invokes when it finishes successfully, or in the event of writing failure.

## See Also

- [func export(to: URL, as: AVFileType, isolation: isolated (any Actor)?) async throws](avassetexportsession/export(to:as:isolation:).md)
  Exports the asset to the output location in the specified file type.
- [func cancelExport()](avassetexportsession/cancelexport.md)
  Cancels the execution of an export session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/exportasynchronously(completionhandler:))*