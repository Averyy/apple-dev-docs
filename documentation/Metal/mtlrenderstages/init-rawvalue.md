# init(rawValue:)

**Framework**: Metal  
**Kind**: init

Creates a render stage from a raw value.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(rawValue: UInt)
```

#### Discussion

Use of the [`MTLRenderStages`](mtlrenderstages.md) type’s static properties, such as [`mesh`](mtlrenderstages/mesh.md), [`vertex`](mtlrenderstages/vertex.md), or [`fragment`](mtlrenderstages/fragment.md) instead of creating a render stage instance yourself with this initializer.

## Parameters

- `rawValue`: A bit field value of a render stage as an integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderstages/init(rawvalue:))*