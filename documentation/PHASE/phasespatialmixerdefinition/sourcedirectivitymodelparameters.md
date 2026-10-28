# sourceDirectivityModelParameters

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

A data set that directs sound such that it’s louder when directed at the listener.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var sourceDirectivityModelParameters: PHASEDirectivityModelParameters? { get set }
```

```objc
@property (nonatomic, strong, nullable) PHASEDirectivityModelParameters * sourceDirectivityModelParameters;
```

## Discussion

The framework applies directivity to sound sources that emanate from a point.

## See Also

### Configuring Directivity
- [var listenerDirectivityModelParameters: PHASEDirectivityModelParameters?](./listenerdirectivitymodelparameters.md)
  A data set that determines how well the listener hears depending on its direction relative to a sound source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialmixerdefinition/sourcedirectivitymodelparameters)*