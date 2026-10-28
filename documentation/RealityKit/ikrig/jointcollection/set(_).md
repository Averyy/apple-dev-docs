# set(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Updates the element with identifier matching the provided value’s identifier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@discardableResult
mutating func set(_ newValue: IKRig.JointCollection.Element) -> IKRig.JointCollection.Element?
```

## Return Value

The previous element value if the identifier exists, `nil` otherwise.

## Discussion

If an element with the provided identifier is not contained - does nothing.

## Parameters

- `newValue`: The new element value to store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/jointcollection/set(_:))*