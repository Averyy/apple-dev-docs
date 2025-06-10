# usage

**Framework**: Metal  
**Kind**: property

A set of contexts in which you can use tensors you create with this descriptor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var usage: MTLTensorUsage { get set }
```

#### Discussion

The default value for this property is a bitwise `OR` of:

- [`render`](mtltensorusage/render.md)
- [`compute`](mtltensorusage/compute.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensordescriptor/usage)*