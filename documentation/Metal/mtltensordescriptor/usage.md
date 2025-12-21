# usage

**Framework**: Metal  
**Kind**: property

A set of contexts in which you can use tensors you create with this descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

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