# init(device:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Initializes a new kernel object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device;
```

## Mentions

- [The MPSKernel Class](../the-mpskernel-class.md)

## Return Value

An initialized kernel object.

## Discussion

This method fails if the device is not supported. Query the [`MPSSupportsMTLDevice(_:)`](../mpssupportsmtldevice%28_%29.md) function to determine whether the device is supported.

## Parameters

- `device`: The Metal device on which the kernel will be used.

## See Also

### Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./copy%28with,device%29.md)
  Makes a copy of this kernel object for a new device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpskernel/init(device:))*