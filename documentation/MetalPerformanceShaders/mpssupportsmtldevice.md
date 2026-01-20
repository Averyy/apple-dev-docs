# MPSSupportsMTLDevice(_:)

**Framework**: Metal Performance Shaders  
**Kind**: func

Determines whether the Metal Performance Shaders framework supports a Metal device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MPSSupportsMTLDevice(_ device: (any MTLDevice)?) -> Bool
```

## Mentions

- [The MPSKernel Class](the-mpskernel-class.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the device is supported. [`false`](https://developer.apple.com/documentation/Swift/false) if the device is not supported.

#### Discussion

For a full listing of Metal Performance Shaders feature set support, see [`Feature Availability`](https://developer.apple.comhttps://developer.apple.com/metal/availability/).

## Parameters

- `device`: A valid Metal device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssupportsmtldevice(_:))*