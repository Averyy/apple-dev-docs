# firstMipmapInTail

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The index of the first mipmap in the tail.

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
var firstMipmapInTail: Int { get }
```

*Mac Catalyst, macOS*

```swift
optional var firstMipmapInTail: Int { get }
```

```objc
@property (readonly) NSUInteger firstMipmapInTail;
```

#### Discussion

In a sparse texture, the *tail* is a collection of mipmaps at higher index values that are mapped as a single block of memory. When you map this mipmap into your sparse texture, Metal also maps mipmap levels with larger index values.

## See Also

### Querying sparse properties
- [var isSparse: Bool](./issparse.md)
  A Boolean value that indicates whether this is a sparse texture.
- [var tailSizeInBytes: Int](./tailsizeinbytes.md)
  The size of the sparse texture tail, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/firstmipmapintail)*