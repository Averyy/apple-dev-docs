# replaceAll(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Replaces the existing anchor collection with a provided collection.

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
@preconcurrency func replaceAll(_ entities: [any HasAnchoring])
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func replaceAll<S>(_ entities: S) where S : Sequence, S.Element : HasAnchoring
```

#### Discussion

This method removes all anchors currently in the collection, then appends all the elements in `entities` to the collection.

## Parameters

- `entities`: An array of anchors to replace the existing collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/replaceall(_:))*