# remove(named:)

**Framework**: RealityKit  
**Kind**: method

Removes a geometric pin with the given name from this entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
func remove(named name: String)
```

#### Discussion

If found, the pin is removed from the entity’s [`GeometricPinsComponent`](geometricpinscomponent.md). There is no effect if no matching [`GeometricPin`](geometricpin.md) is found.

## Parameters

- `name`: The name of the geometric pin to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitygeometricpins/remove(named:))*