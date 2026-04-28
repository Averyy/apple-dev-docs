# kSecTransformErrorMoreThanOneOutput

**Framework**: Security  
**Kind**: var

A transform has an internal routing error that has caused multiple outputs instead of a single discrete output.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var kSecTransformErrorMoreThanOneOutput: CFIndex { get }
```

#### Discussion

This error occurs if [`SecTransformExecute(_:_:)`](sectransformexecute(_:_:).md) has already been called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformerrormorethanoneoutput)*