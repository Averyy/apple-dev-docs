# listenerDirectivityModelParameters

**Framework**: PHASE  
**Kind**: property

A data set that determines how well the listener hears depending on its direction relative to a sound source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var listenerDirectivityModelParameters: PHASEDirectivityModelParameters? { get set }
```

#### Discussion

An app can configure this property to attenuate sound to the sides of the listener while leaving sound in front of or behind the listener unchanged.

## See Also

- [var sourceDirectivityModelParameters: PHASEDirectivityModelParameters?](phasespatialmixerdefinition/sourcedirectivitymodelparameters.md)
  A data set that directs sound such that it’s louder when directed at the listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialmixerdefinition/listenerdirectivitymodelparameters)*