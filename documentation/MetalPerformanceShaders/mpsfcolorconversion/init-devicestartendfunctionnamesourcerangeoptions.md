# init(device:start:end:functionName:sourceRange:options:)

**Framework**: Metal Performance Shaders  
**Kind**: init

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(device: any MTLDevice, start: CGColorSpace, end: CGColorSpace, functionName name: String, sourceRange: UnsafePointer<MPSFunctions_AABB>?, options: MPSFColorConversionOptions = []) throws
```

#### Return Value

On success, a valid MPSFunctionsConversion object. If the conversion can’t be done, for example because it consumes or produces more than four channels, nil will be returned, and an appropriate error code created.

#### Discussion

Initialize a new MPSFunctionsConversion object

Builds a MPSFunctionsConverison object from a starting and ending colorspace. Kicks off an asynchronous compilation task to build a MTLFunction appropriate for the device. Calling the .function or .error propertywill stop and wait for it. Since the compilation task may take a few milliseconds, your application should create the MPSFunctionsConversion object as soon as it knows the conversion will be needed.

```None
         If you would like to make use of  sRGB, PQ and HLG, MTLPixelFormat
         variants to take advantage of hardware features to produce linear color
         from these colorspaces, use the result of CGColorSpaceCreateLinearized(start)
         here instead and configure your MTLTexture to the appropriate variant MTLPixelFormat,
         using a texture view or new base pixel format.
```

## Parameters

- `device`: A valid MTLDevice where the conversion will be used
- `start`: The CGColorSpaceRef for the input data to the conversion
- `end`: The CGColorSpaceRef for the output data from the conversion
- `name`: The name of the Metal Shading Language function to build.
- `sourceRange`: If not NULL, the range limit guarantees that the input texels to the MTLFunction will not appear outside the given axis aligned bounding box. This, in combination with precision limits (see options), may allow for a faster conversion calculation.  If a rangeLimit is provided, the result of the conversion involving out of range inputs is undefined.
- `options`: Options to use when building the conversion


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsfcolorconversion/init(device:start:end:functionname:sourcerange:options:))*