# subscript(_:)

**Framework**: GameplayKit  
**Kind**: subscript

Returns the component at the specified index in the system’s list of components.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
subscript(idx: Int) -> ComponentType { get }
```

#### Return Value

The component at the specified index in the [`components`](gkcomponentsystem/components.md) array.

#### Discussion

This method is equivalent to accessing objects by index in the [`components`](gkcomponentsystem/components.md) array, but allows access using subscript syntax on the component system itself.

## Parameters

- `idx`: A valid index to the   array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcomponentsystem/subscript(_:))*