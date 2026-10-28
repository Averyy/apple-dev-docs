# dataWithContentsOfURL:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a data object from the data at the specified file URL.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) dataWithContentsOfURL:(NSURL *) url;
```

## Return Value

A data object that contains the file’s data, or `nil` if the system can’t create one.

## Discussion

> ❗ **Important**:  As this method runs synchronously and blocks the calling thread until it finishes, don’t invoke it from the main thread. Use file coordination or one of the nonblocking file-related APIs instead.

If you specify a malformed URL or the referenced location doesn’t exist on disk, the initializer fails and returns `nil`. To handle such errors, use `NSData/init(contentsOfURL:options:)-95rht` instead.

## Parameters

- `url`: The location on disk of the data to read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/datawithcontentsofurl:)*