# modifyPixelData(_:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Modifies the contents of a mutable texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func modifyPixelData(_ block: @escaping @Sendable (UnsafeMutableRawPointer?, Int) -> Void)
```

```swift
func modifyPixelData() async -> (UnsafeMutableRawPointer?, Int)
```

```objc
- (void) modifyPixelDataWithBlock:(void (^)(void *pixelData, size_t lengthInBytes)) block;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func modifyPixelData() async -> (UnsafeMutableRawPointer?, Int)
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

The contents of the texture can be modified only at specific times when the graphics hardware permits it. When this method is called, it schedules a new background task to update the texture and then returns. Your block is called when the texture can be modified. Your block is called on an arbitrary queue. Your block should modify the texture’s contents and then return.

The texture bytes are assumed to be stored as tightly packed 32 bpp, 8bpc (unsigned integer) RGBA pixel data. The color components you provide should have already been multiplied by the alpha value.

## Parameters

- `block`: A block to be called when the texture can be safely modified. The block takes the following parameters:

  - **pixelData**: A pointer to the start of the current texture data.
  - **lengthInBytes**: The length of the texture data in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skmutabletexture/modifypixeldata(_:))*