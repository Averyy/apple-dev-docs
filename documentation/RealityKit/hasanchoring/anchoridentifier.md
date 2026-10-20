# anchorIdentifier

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The identifier of the AR anchor with which the anchor entity is associated, or `nil` if it isn’t currently anchored.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS - Deprecated

> **Deprecated**: Anchoring with ARAnchor is not available on visionOS.

## Declaration

```swift
@MainActor
@preconcurrency var anchorIdentifier: UUID? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasanchoring/anchoridentifier)*