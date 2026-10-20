# addAmbientMixerParameters(identifier:listener:)

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addAmbientMixerParametersWithIdentifier:(NSString *) identifier listener:(PHASEListener *) listener;
```

## Parameters

- `identifier`: The name of the spatial submixer.
- `listener`: An object that receives a source audio signal. The mixer orients the sound the listener receives based on its [`transform`](../phaseobject/transform.md).

## See Also

### Positioning and Orienting Audio
- [func addSpatialMixerParameters(identifier: String, source: PHASESource, listener: PHASEListener)](./addspatialmixerparameters%28identifier,source,listener%29.md)
  Adds runtime parameters for a spatial mixer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemixerparameters/addambientmixerparameters(identifier:listener:))*