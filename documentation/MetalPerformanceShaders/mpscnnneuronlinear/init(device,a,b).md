# init(device:a:b:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Initializes a linear neuron filter.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 10.0+ - Deprecated in 12.0
- macOS 10.13+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
init(device: any MTLDevice, a: Float, b: Float)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device a:(float) a b:(float) b;
```

#### Return Value

A valid [`MPSCNNNeuronLinear`](../mpscnnneuronlinear.md) object or `nil`, if failure.

## Parameters

- `device`: The device the filter will run on.
- `a`: The “a” variable of the filter function.
- `b`: The “b” variable of the filter function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuronlinear/init(device:a:b:))*