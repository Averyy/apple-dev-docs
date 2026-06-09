# temporarySurface(withIdentifier:format:width:height:)

**Framework**: Core Image  
**Kind**: method  
**Required**: Yes

Returns a temporary IOSurface that your Core Image Processor Kernel can use as scratch storage during processing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func temporarySurface(withIdentifier identifier: String, format: OSType, width: Int, height: Int) -> IOSurface?
```

#### Return Value

 An autoreleased `IOSurface` of the requested size and format, or `nil` if the surface could not be created.

#### Discussion

Use this method when your processor needs an intermediate `IOSurface` to stash data between stages of its work. Core Image manages the lifetime of the returned surface and reuses the underlying allocation across multiple invocations when possible. This is more efficient than allocating a fresh `IOSurface` on each invocation of your processor.

The returned surface is valid only for the duration of the [`process(with:arguments:output:)`](ciimageprocessorkernel/process(with:arguments:output:).md) call that requested it. Don’t retain it beyond the scope of that method or use it after the method returns.

Calling this method multiple times within the same processor invocation with the same `identifier`, `format`, `width`, and `height` returns the same surface. Otherwise it returns a distinct surface. This lets a processor request several independent surfaces by giving each one a unique name.

## Parameters

- `identifier`: A name that uniquely identifies this scratch surface within the processor invocation.
- `format`: The pixel format for the surface. Must be a non-zero `OSType` pixel format constant.
- `width`: The width of the surface in pixels. Must be greater than zero.
- `height`: The height of the surface in pixels. Must be greater than zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/temporarysurface(withidentifier:format:width:height:))*