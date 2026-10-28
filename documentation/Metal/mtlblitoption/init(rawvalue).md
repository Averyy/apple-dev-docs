# init(rawValue:)

**Framework**: Metal  
**Kind**: init  
**Role**: Initializer

Creates a blit option from a raw value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(rawValue: UInt)
```

## Discussion

Use one of the [`MTLBlitOption`](../mtlblitoption.md) type’s static properties, such as [`depthFromDepthStencil`](./depthfromdepthstencil.md), [`stencilFromDepthStencil`](./stencilfromdepthstencil.md), and [`rowLinearPVRTC`](./rowlinearpvrtc.md) instead of creating a blit option yourself with this initializer.

## Parameters

- `rawValue`: The bitwise value of a blit option as an integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitoption/init(rawvalue:))*