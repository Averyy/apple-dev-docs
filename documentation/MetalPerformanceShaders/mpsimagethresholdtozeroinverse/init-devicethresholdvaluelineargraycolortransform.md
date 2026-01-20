# init(device:thresholdValue:linearGrayColorTransform:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes the kernel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, thresholdValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>?)
```

#### Return Value

An initialized kernel object.

## Parameters

- `device`: The Metal device the filter will run on.
- `thresholdValue`: The threshold value to use.
- `transform`: The color transform to use. This matrix is an array of 3 floats that defaults to the   standard: 


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtozeroinverse/init(device:thresholdvalue:lineargraycolortransform:))*