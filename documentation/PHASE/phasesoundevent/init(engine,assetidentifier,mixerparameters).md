# init(engine:assetIdentifier:mixerParameters:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithEngine:(PHASEEngine *) engine assetIdentifier:(NSString *) assetIdentifier mixerParameters:(PHASEMixerParameters *) mixerParameters error:(NSError **) error;
```

## Parameters

- `engine`: The object that controls this class’s associated audio output.
- `assetIdentifier`: The identifier for the sound event asset from which to create the node.
- `mixerParameters`: A dictionary of spatial mixer parameters to enable. The keys match available identifiers of the object’s spatial mixers.

## See Also

### Creating a Sound Event
- [init(engine: PHASEEngine, assetIdentifier: String) throws](./init%28engine,assetidentifier%29.md)
  Creates a sound event node with the given asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/init(engine:assetidentifier:mixerparameters:))*