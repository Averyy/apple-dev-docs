# program

**Framework**: SceneKit  
**Kind**: property

A program used when rendering the object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional var program: SCNProgram? { get set }
```

#### Discussion

Assigning a program to an object overrides all other rendering parameters, including material settings and shader modifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadable/program)*