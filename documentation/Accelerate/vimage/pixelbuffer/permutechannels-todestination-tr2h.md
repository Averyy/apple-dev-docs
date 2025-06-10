# permuteChannels(to:destination:)

**Framework**: Accelerate  
**Kind**: method

Permutes the channels of an 8-bit-per-channel, 4-channel interleaved pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func permuteChannels(to permuteMap: (UInt8, UInt8, UInt8, UInt8), destination: vImage.PixelBuffer<Format>)
```

#### Discussion

For example, the following code reverses the channel ordering of a pixel buffer:

```swift
let buffer = vImage.PixelBuffer<vImage.Interleaved8x4>(
    pixelValues: [10, 20, 30, 40],
    size: vImage.Size(width: 1,
                      height: 1))

buffer.permuteChannels(to: (3, 2, 1, 0),
                       destination: buffer)

// Prints "[40, 30, 20, 10]"
print(buffer.array)
```

## Parameters

- `permuteMap`: A tuple of four 8-bit integers with the values 0, 1, 2, and 3, in some order.
- `destination`: The destination pixel buffer.

## See Also

- [func permuteChannels(to: (UInt8, UInt8, UInt8), destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/permutechannels(to:destination:)-4y4rh.md)
  Permutes the channels of an 8-bit-per-channel, 3-channel interleaved pixel buffer.
- [func permuteChannels(to: (UInt8, UInt8, UInt8, UInt8), destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/permutechannels(to:destination:)-8y213.md)
  Permutes the channels of an unsigned 16-bit-per-channel, 4-channel interleaved pixel buffer.
- [func permuteChannels(to: (UInt8, UInt8, UInt8, UInt8), destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/permutechannels(to:destination:)-74dmh.md)
  Permutes the channels of a floating-point 16-bit-per-channel, 4-channel interleaved pixel buffer.
- [func permuteChannels(to: (UInt8, UInt8, UInt8, UInt8), destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/permutechannels(to:destination:)-6n6yi.md)
  Permutes the channels of an 32-bit-per-channel, 4-channel interleaved pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/permutechannels(to:destination:)-tr2h)*