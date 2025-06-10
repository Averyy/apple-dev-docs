# set(_:)

**Framework**: RealityKit  
**Kind**: method

Updates the element with identifier matching the new value.

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
mutating func set(_ newValue: IKComponent.ConstraintCollection.Element) -> IKComponent.ConstraintCollection.Element?
```

#### Return Value

The previous value if the identifier was found, nil otherwise.

## Parameters

- `newValue`: The new value to store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/constraintcollection/set(_:))*