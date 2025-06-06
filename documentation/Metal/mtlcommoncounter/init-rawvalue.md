# init(rawValue:)

**Framework**: Metal  
**Kind**: init

Creates a common counter name from a raw value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(rawValue: String)
```

#### Discussion

Use of the [`MTLCommonCounter`](mtlcommoncounter.md) type’s static properties, such as [`timestamp`](mtlcommoncounter/timestamp.md), [`computeKernelInvocations`](mtlcommoncounter/computekernelinvocations.md), or [`totalCycles`](mtlcommoncounter/totalcycles.md) instead of creating a common counter instance yourself with this initializer.

## Parameters

- `rawValue`: The name of a common counter as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommoncounter/init(rawvalue:))*