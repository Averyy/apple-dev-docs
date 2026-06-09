# init(device:conversion:functionName:sourceRange:options:)

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
init(device: any MTLDevice, conversion: CGColorConversionInfo?, functionName name: String, sourceRange: UnsafePointer<MPSFunctions_AABB>?, options: MPSFColorConversionOptions = []) throws
```

#### Return Value

On success, a valid MPSFunctionsConversion object. If the conversion can’t be done, for example because it consumes or produces more than four channels, nil will be returned, and an appropriate error code created.

#### Discussion

Initialize a new MPSFunctionsConversion object

Reads the CGColorConversionInfoRef and creates an internal representation Kicks off an asynchronous compilation task to build a MTLFunction appropriate for the device.  Calling the .function or .error properties will stop and wait for it. Since the compilation task may take a few milliseconds, your application should create the MPSFunctionsConversion object as soon as it knows the conversion will be needed.

## Parameters

- `device`: A valid MTLDevice where the conversion will be used
- `conversion`: A CGColorConversionInfoRef to represent the conversion. If NULL, a conversion function that returns its argument will be returned.
- `name`: The name of the Metal Shading Language function to build.
- `sourceRange`: If not NULL, the range limit guarantees that the input texels to the MTLFunction will not appear outside the given axis aligned bounding box. This, in combination with precision limits (see options), may allow for a faster conversion calculation.  If a rangeLimit is provided, the result of the conversion involving out of range inputs is undefined.
- `options`: Options to use when building the conversion CAUTION: when conversion is NULL, MPSFunctions has no information about the number of channels in the result texel, and so can not intelligently handle MPSFColorConversionOptionsReturnGrayscaleAsRGB.  In this case, it will assume the output content is grayscale and remap it to {Y,Y,Y,A} as requested.  Your application should either intelligently set the option only for grayscale content, or call the other -init method that consumes two colorspaces which can manage this detail itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsfcolorconversion/init(device:conversion:functionname:sourcerange:options:))*