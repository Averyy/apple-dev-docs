# set(_:)

**Framework**: RealityKit  
**Kind**: method

Updates the element with identifier matching the provided value’s identifier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@discardableResult
mutating func set(_ newValue: IKRig.ConstraintsCollection.Element) -> IKRig.ConstraintsCollection.Element?
```

#### Return Value

The previous element value if the identifier exists, `nil` otherwise.

#### Discussion

If an element with the provided identifier is not contained, adds a new one.

## Parameters

- `newValue`: The new element value to store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraintscollection/set(_:))*