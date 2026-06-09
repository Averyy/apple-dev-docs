# init(contentsOf:options:)

**Framework**: Foundation  
**Kind**: init

Creates a data object from the data at the provided file URL using specific reading options.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(contentsOf url: URL, options readOptionsMask: NSData.ReadingOptions = []) throws
```

#### Discussion

> ❗ **Important**:  As this method runs synchronously and blocks the calling thread until it finishes, don’t invoke it from the main thread. Use file coordination or one of the nonblocking file-related APIs instead.

If the system can’t create an instance, the initializer may throw in Swift, or return `nil` in Objective-C.

## Parameters

- `url`: The location on disk of the data to read.
- `readOptionsMask`: The mask specifying the options to use when reading the data. For more information, see [`NSData.ReadingOptions`](nsdata/readingoptions.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/init(contentsof:options:))*