# parentDirectoryURLKey

**Framework**: Foundation  
**Kind**: property

The container directory of the resource.

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
static let parentDirectoryURLKey: URLResourceKey
```

#### Discussion

The corresponding value is a read-only `NSURL` object, or `nil` if the resource is the root directory of its volume.

## See Also

- [static let isDirectoryKey: URLResourceKey](urlresourcekey/isdirectorykey.md)
  A key for determining whether the resource is a directory.
- [static let directoryEntryCountKey: URLResourceKey](urlresourcekey/directoryentrycountkey.md)
  The key for a count of items in the directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcekey/parentdirectoryurlkey)*