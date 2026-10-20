# isFileURL

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isFileURL) BOOL fileURL;
```

#### Discussion

The property’s value is  [`true`](../../Swift/true.md) if the receiver uses the file scheme, [`false`](../../Swift/false.md) otherwise. Both file path and file reference URLs are considered to be file URLs.

If this property’s value is [`true`](../../Swift/true.md), then the receiver’s [`path`](./path.md) property contains a suitable value for input into [`FileManager`](../filemanager.md) or `NSPathUtilities`.

## See Also

### Querying an NSURL
- [func checkResourceIsReachableAndReturnError(NSErrorPointer) -> Bool](./checkresourceisreachableandreturnerror%28_%29.md)
  Returns whether the resource pointed to by a file URL can be reached.
- [func isFileReferenceURL() -> Bool](./isfilereferenceurl%28%29.md)
  Returns whether the URL is a file reference URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/isfileurl)*