# serializedRepresentation

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The contents of the file wrapper as an opaque data object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var serializedRepresentation: Data? { get }
```

```objc
@property (copy, readonly, nullable) NSData * serializedRepresentation;
```

## Discussion

This property contains a data object in the format used by the [`fileContents`](../../AppKit/nspasteboard/pasteboardtype/filecontents.md) pasteboard type. This data object is also suitable for passing to [`init(serializedRepresentation:)`](./init%28serializedrepresentation%29.md).

This property may be `nil` if the user modifies the contents of the file system node after you call [`read(from:options:)`](./read%28from,options%29.md) or [`init(url:options:)`](./init%28url,options%29-70161.md), but before [`FileWrapper`](../filewrapper.md) has read the contents of the file.  You can use the [`immediate`](./readingoptions/immediate.md) reading option to reduce the likelihood of this problem.

## See Also

### Related Documentation
- [init?(serializedRepresentation: Data)](./init%28serializedrepresentation%29.md)
  Initializes the receiver as a regular-file file wrapper from given serialized data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/serializedrepresentation)*