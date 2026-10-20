# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript

Accesses the element with the specified identifier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
subscript(id: IKRig.JointCollection.Element.ID) -> IKRig.JointCollection.Element? { get set }
```

#### Overview

The following set scenarios are ignored:

- Setting nil
- Setting element with different id, e.g. `collection[ID(2)]?.id = ID(3)
- Setting element with id not in the set

## Parameters

- `id`: The identifier of the requested element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/jointcollection/subscript(_:))*