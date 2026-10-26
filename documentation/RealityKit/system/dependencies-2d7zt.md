# dependencies

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

A default implementation of the dependencies array.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
static var dependencies: [SystemDependency] { get }
```

#### Discussion

RealityKit provides a default implementation of this property which returns an empty array. If a class that conforms to [`System`](../system.md) has no dependencies, it doesn’t need to implement this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/system/dependencies-2d7zt)*