# program

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A program used when rendering the object.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
optional var program: SCNProgram? { get set }
```

```objc
@property (nonatomic, retain, nullable) SCNProgram * program;
```

## Discussion

Assigning a program to an object overrides all other rendering parameters, including material settings and shader modifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadable/program)*