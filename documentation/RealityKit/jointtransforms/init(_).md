# init(_:)

**Framework**: RealityKit  
**Kind**: init

Initializes a collection of transforms of a specific type for a single skeletal pose.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
init<S>(_ transforms: S) where S : Sequence, S.Element == Transform
```

## Parameters

- `transforms`: An array of position, rotation, and scale data for the joints.

## See Also

- [init()](jointtransforms/init.md)
  Initializes a collection of animatable transforms for a single skeletal pose.
- [init(arrayLiteral: Transform...)](jointtransforms/init(arrayliteral:).md)
  Initializes a collection of animatable transforms using the argument elements for a single skeletal pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/jointtransforms/init(_:))*