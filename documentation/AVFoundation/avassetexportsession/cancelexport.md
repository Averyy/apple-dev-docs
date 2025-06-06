# cancelExport()

**Framework**: AVFoundation  
**Kind**: method

Cancels the execution of an export session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func cancelExport()
```

#### Discussion

Apple discourages the use of this symbol. Use [`cancel()`](https://developer.apple.com/documentation/Swift/Task/cancel()) on the [`Task`](https://developer.apple.com/documentation/Swift/Task) or parent task that initiated the export instead.

## See Also

- [func export(to: URL, as: AVFileType, isolation: isolated (any Actor)?) async throws](avassetexportsession/export(to:as:isolation:).md)
  Exports the asset to the output location in the specified file type.
- [func exportAsynchronously(completionHandler: () -> Void)](avassetexportsession/exportasynchronously(completionhandler:).md)
  Starts the asynchronous execution of an export session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/cancelexport())*