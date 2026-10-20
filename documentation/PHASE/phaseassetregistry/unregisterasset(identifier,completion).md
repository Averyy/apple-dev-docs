# unregisterAsset(identifier:completion:)

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

Deallocates system memory for a given asset and removes it from the engine’s list of registered assets.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func unregisterAsset(identifier: String, completion handler: (@Sendable (Bool) -> Void)? = nil)
```

```swift
func unregisterAsset(identifier: String) async -> Bool
```

```objc
- (void) unregisterAssetWithIdentifier:(NSString *) identifier completion:(void (^)(bool success)) handler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func unregisterAsset(identifier: String) async -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `identifier`: The unique name that the app defines for the sound asset.
- `handler`: Code that the system runs after it unregisters the asset.

## See Also

### Registering Sound Assets
- [func registerSoundAsset(url: URL, identifier: String?, assetType: PHASEAsset.AssetType, channelLayout: AVAudioChannelLayout?, normalizationMode: PHASENormalizationMode) throws -> PHASESoundAsset](./registersoundasset%28url,identifier,assettype,channellayout,normalizationmode%29.md)
  Loads a sound asset from the argument URL and adds it to the engine’s list of registered assets.
- [func registerSoundAsset(data: Data, identifier: String?, format: AVAudioFormat, normalizationMode: PHASENormalizationMode) throws -> PHASESoundAsset](./registersoundasset%28data,identifier,format,normalizationmode%29.md)
  Loads a sound asset from memory and adds it to the engine’s list of registered assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseassetregistry/unregisterasset(identifier:completion:))*