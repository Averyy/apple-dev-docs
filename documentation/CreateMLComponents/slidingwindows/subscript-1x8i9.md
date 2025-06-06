# subscript(_:)

**Framework**: Create ML Components  
**Kind**: subscript

Accesses the window at the specified position.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
subscript(position: Int) -> MLShapedArray<Scalar> { get }
```

## Parameters

- `position`: The position of the window to access.   must be a valid index of the   collection that is not equal to the   property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/slidingwindows/subscript(_:)-1x8i9)*