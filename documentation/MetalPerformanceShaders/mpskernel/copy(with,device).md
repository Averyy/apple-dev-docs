# copy(with:device:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

Makes a copy of this kernel object for a new device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func copy(with zone: NSZone? = nil, device: (any MTLDevice)?) -> Self
```

```objc
- (instancetype) copyWithZone:(NSZone *) zone device:(id<MTLDevice>) device;
```

## Mentions

- [The MPSKernel Class](../the-mpskernel-class.md)

#### Return Value

A copy of this kernel object.

#### Discussion

The same kernel objects should not be used to encode separate kernel operations on multiple command buffers from multiple threads. Many kernels have mutable properties that might be changed by another thread while the kernel is being encoded. If you need to use a kernel from multiple threads, make a copy of it for each additional thread using [`copy(with:)`](../../Foundation/nscopying/copy%28with%29.md) or [`copy(with:device:)`](./copy%28with,device%29.md). Note that the [`copy(with:)`](../../Foundation/nscopying/copy%28with%29.md) method makes a copy of the kernel object on the same device.

This method fails if the device is not supported. Query the [`MPSSupportsMTLDevice(_:)`](../mpssupportsmtldevice%28_%29.md) function to determine whether the device is supported.

## Parameters

- `zone`: The zone in which to allocate the kernel object.
- `device`: The Metal device for the new kernel object.

## See Also

### Methods
- [init(device: any MTLDevice)](./init%28device%29.md)
  Initializes a new kernel object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpskernel/copy(with:device:))*