# tailSizeInBytes

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The size of the sparse texture tail, in bytes.

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
var tailSizeInBytes: Int { get }
```

*Mac Catalyst, macOS*

```swift
optional var tailSizeInBytes: Int { get }
```

```objc
@property (readonly) NSUInteger tailSizeInBytes;
```

## See Also

### Querying sparse properties
- [var isSparse: Bool](./issparse.md)
  A Boolean value that indicates whether this is a sparse texture.
- [var firstMipmapInTail: Int](./firstmipmapintail.md)
  The index of the first mipmap in the tail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/tailsizeinbytes)*