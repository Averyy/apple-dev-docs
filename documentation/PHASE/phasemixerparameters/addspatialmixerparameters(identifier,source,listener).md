# addSpatialMixerParameters(identifier:source:listener:)

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

Adds runtime parameters for a spatial mixer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func addSpatialMixerParameters(identifier: String, source: PHASESource, listener: PHASEListener)
```

```objc
- (void) addSpatialMixerParametersWithIdentifier:(NSString *) identifier source:(PHASESource *) source listener:(PHASEListener *) listener;
```

## Parameters

- `identifier`: The name of the spatial submixer.
- `source`: A location in the scene that plays audio.
- `listener`: An object that receives a source audio signal. The mixer scales and orients the sound the listener receives based on its [`transform`](../phaseobject/transform.md).

## See Also

### Positioning and Orienting Audio
- [func addAmbientMixerParameters(identifier: String, listener: PHASEListener)](./addambientmixerparameters%28identifier,listener%29.md)
  Adds runtime parameters for an ambient mixer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemixerparameters/addspatialmixerparameters(identifier:source:listener:))*