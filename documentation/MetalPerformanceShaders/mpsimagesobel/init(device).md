# init(device:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Initializes a Sobel filter on a given device using the default color transform.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(device: any MTLDevice)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device;
```

#### Return Value

An initialized Sobel filter object.

#### Discussion

The default color transform matrix is an array of 3 floats set to the *BT.601/JPEG* standard: `{0.299f, 0.587f, 0.114f}`.

## Parameters

- `device`: The Metal device the filter will run on.

## See Also

### Methods
- [init(device: any MTLDevice, linearGrayColorTransform: UnsafePointer<Float>)](./init%28device,lineargraycolortransform%29.md)
  Initializes a Sobel filter on a given device using a specific color transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagesobel/init(device:))*