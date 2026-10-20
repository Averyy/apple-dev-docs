# isSparse

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this is a sparse texture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
var isSparse: Bool { get }
```

*Mac Catalyst, macOS*

```swift
optional var isSparse: Bool { get }
```

```objc
@property (readonly) BOOL isSparse;
```

## See Also

### Querying sparse properties
- [var firstMipmapInTail: Int](./firstmipmapintail.md)
  The index of the first mipmap in the tail.
- [var tailSizeInBytes: Int](./tailsizeinbytes.md)
  The size of the sparse texture tail, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/issparse)*