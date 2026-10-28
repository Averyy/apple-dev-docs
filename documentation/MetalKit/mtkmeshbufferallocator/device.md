# device

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The device used to create Metal objects.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var device: any MTLDevice { get }
```

```objc
@property (nonatomic, readonly, nonnull) id<MTLDevice> device;
```

## Discussion

A Metal device must be specialized at initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmeshbufferallocator/device)*