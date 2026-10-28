# isDirectoryKey

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A key for determining whether the resource is a directory.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let isDirectoryKey: URLResourceKey
```

```c
extern NSURLResourceKey const NSURLIsDirectoryKey;
```

## Discussion

The corresponding value is a read-only Boolean `NSNumber` object.

## See Also

### Directory keys
- [static let parentDirectoryURLKey: URLResourceKey](./parentdirectoryurlkey.md)
  The container directory of the resource.
- [static let directoryEntryCountKey: URLResourceKey](./directoryentrycountkey.md)
  The key for a count of items in the directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcekey/isdirectorykey)*