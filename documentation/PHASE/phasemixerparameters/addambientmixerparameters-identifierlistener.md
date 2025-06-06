# addAmbientMixerParameters(identifier:listener:)

**Framework**: PHASE  
**Kind**: method

Adds runtime parameters for an ambient mixer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func addAmbientMixerParameters(identifier: String, listener: PHASEListener)
```

## Parameters

- `identifier`: The name of the spatial submixer.
- `listener`: An object that receives a source audio signal. The mixer orients the sound the listener receives based on its  .

## See Also

- [func addSpatialMixerParameters(identifier: String, source: PHASESource, listener: PHASEListener)](phasemixerparameters/addspatialmixerparameters(identifier:source:listener:).md)
  Adds runtime parameters for a spatial mixer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemixerparameters/addambientmixerparameters(identifier:listener:))*