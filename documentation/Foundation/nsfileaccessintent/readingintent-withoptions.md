# readingIntent(with:options:)

**Framework**: Foundation  
**Kind**: method

Returns a file access intent object for reading the given URL with the provided options.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func readingIntent(with url: URL, options: NSFileCoordinator.ReadingOptions = []) -> Self
```

#### Return Value

A newly instantiated and configured file access intent object.

#### Discussion

When calling a file coordinator’s [`coordinate(with:queue:byAccessor:)`](nsfilecoordinator/coordinate(with:queue:byaccessor:).md) method, you pass an array of file access intent objects. Each intent object represents a specific read or write operation on a single document or directory. Use `readingIntentWithURL:options:` to create an intent object suitable for reading.

## Parameters

- `url`: The URL of the document you intend to read from.
- `options`: The coordinated reading options. For a list of valid values, see   in the  .

## See Also

- [func coordinate(with: [NSFileAccessIntent], queue: OperationQueue, byAccessor: ((any Error)?) -> Void)](nsfilecoordinator/coordinate(with:queue:byaccessor:).md)
  Performs a number of coordinated-read or -write operations asynchronously.
- [class func writingIntent(with: URL, options: NSFileCoordinator.WritingOptions) -> Self](nsfileaccessintent/writingintent(with:options:).md)
  Returns a file access intent object for writing to the given URL with the provided options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileaccessintent/readingintent(with:options:))*