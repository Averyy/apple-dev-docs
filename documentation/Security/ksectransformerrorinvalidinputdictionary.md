# kSecTransformErrorInvalidInputDictionary

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A dictionary used to import a transform has invalid data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var kSecTransformErrorInvalidInputDictionary: CFIndex { get }
```

```c
kSecTransformErrorInvalidInputDictionary
```

#### Discussion

This error may occur when trying to import a transform from a data representation using the [`SecTransformCreateFromExternalRepresentation(_:_:)`](./sectransformcreatefromexternalrepresentation%28_,_%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformerrorinvalidinputdictionary)*