# append(contentsOf:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Adds anchors from an array to the end of this collection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func append(contentsOf array: [any HasAnchoring])
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func append<S>(contentsOf sequence: S) where S : Sequence, S.Element : HasAnchoring
```

## Parameters

- `array`: The array of anchor entities to add.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/append(contentsof:))*