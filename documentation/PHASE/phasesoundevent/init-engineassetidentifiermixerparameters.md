# init(engine:assetIdentifier:mixerParameters:)

**Framework**: PHASE  
**Kind**: init

Creates a sound event node with the given asset and mixer parameters.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(engine: PHASEEngine, assetIdentifier: String, mixerParameters: PHASEMixerParameters) throws
```

## Parameters

- `engine`: The object that controls this class’s associated audio output.
- `assetIdentifier`: The identifier for the sound event asset from which to create the node.
- `mixerParameters`: A dictionary of spatial mixer parameters to enable. The keys match available identifiers of the object’s spatial mixers.

## See Also

- [init(engine: PHASEEngine, assetIdentifier: String) throws](phasesoundevent/init(engine:assetidentifier:).md)
  Creates a sound event node with the given asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/init(engine:assetidentifier:mixerparameters:))*