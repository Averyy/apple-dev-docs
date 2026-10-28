# init(mtlDevice:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init  
**Role**: Initializer

Creates a device from a given Metal device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(mtlDevice metalDevice: any MTLDevice)
```

```objc
+ (instancetype) deviceWithMTLDevice:(id<MTLDevice>) metalDevice;
```

## Return Value

A valid device.

## Parameters

- `metalDevice`: `MTLDevice` to create an MPSGraphDevice from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphdevice/init(mtldevice:)-4ettd)*