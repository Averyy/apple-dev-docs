# copy(with:device:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func copy(with zone: NSZone? = nil, device: (any MTLDevice)?) -> Self
```

#### Return Value

A pointer to a copy of this MPSKernel. This will fail, returning nil if the device is not supported. Devices must be MTLFeatureSet_iOS_GPUFamily2_v1 or later.

#### Discussion

Make a copy of this MPSFunction for a new device

-copyWithZone: will call this API to make a copy of the MPSKernel on the same device.  This interface may also be called directly to make a copy of the MPSFunction on a new device.

## Parameters

- `zone`: The NSZone in which to allocate the object
- `device`: The device for the new MPSKernel. If nil, then use self.device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsfunction/copy(with:device:))*