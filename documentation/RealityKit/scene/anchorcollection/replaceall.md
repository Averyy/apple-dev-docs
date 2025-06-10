# replaceAll(_:)

**Framework**: RealityKit  
**Kind**: method

Replaces the existing anchor collection with a provided collection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func replaceAll(_ entities: [any HasAnchoring])
```

#### Discussion

This method removes all anchors currently in the collection, then appends all the elements in `entities` to the collection.

## Parameters

- `entities`: An array of anchors to replace the existing collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/replaceall(_:))*