# isFileURL

**Framework**: Foundation  
**Kind**: property

A boolean value that determines whether the receiver is a file URL.

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
var isFileURL: Bool { get }
```

#### Discussion

The property’s value is  [`true`](https://developer.apple.com/documentation/Swift/true) if the receiver uses the file scheme, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise. Both file path and file reference URLs are considered to be file URLs.

If this property’s value is [`true`](https://developer.apple.com/documentation/Swift/true), then the receiver’s [`path`](nsurl/path.md) property contains a suitable value for input into [`FileManager`](filemanager.md) or `NSPathUtilities`.

## See Also

- [func checkResourceIsReachableAndReturnError(NSErrorPointer) -> Bool](nsurl/checkresourceisreachableandreturnerror(_:).md)
  Returns whether the resource pointed to by a file URL can be reached.
- [func isFileReferenceURL() -> Bool](nsurl/isfilereferenceurl.md)
  Returns whether the URL is a file reference URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/isfileurl)*