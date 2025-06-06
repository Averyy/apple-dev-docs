# init(engine:assetIdentifier:)

**Framework**: PHASE  
**Kind**: init

Creates a sound event node with the given asset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(engine: PHASEEngine, assetIdentifier: String) throws
```

## Parameters

- `engine`: The object that controls this class’s associated audio output.
- `assetIdentifier`: The identifier for the sound event asset from which to create the node.

## See Also

- [init(engine: PHASEEngine, assetIdentifier: String, mixerParameters: PHASEMixerParameters) throws](phasesoundevent/init(engine:assetidentifier:mixerparameters:).md)
  Creates a sound event node with the given asset and mixer parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/init(engine:assetidentifier:))*