# init()

**Framework**: Accelerate  
**Kind**: init

Creates an empty vImage buffer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init()
```

#### Discussion

Use this initializer to create an empty vImage buffer that you pass to a subsequent function that allocates and initializes the buffer’s storage and properties. For example, the following code creates an empty buffer and initializes it using the [`vImageBuffer_Init(_:_:_:_:_:)`](vimagebuffer_init(_:_:_:_:_:).md) function:

```swift
var buffer = vImage_Buffer()

vImageBuffer_Init(&buffer,
                  5,    // height
                  10,   // width
                  8,    // bits per pixel
                  vImage_Flags(kvImageNoFlags))

```

## See Also

- [init(width: Int, height: Int, bitsPerPixel: UInt32) throws](vimage_buffer/init(width:height:bitsperpixel:).md)
  Creates a new buffer with the specified width, height, and bits per pixel.
- [init(size: CGSize, bitsPerPixel: UInt32) throws](vimage_buffer/init(size:bitsperpixel:).md)
  Creates a new buffer with the specified size and bits per pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_buffer/init())*