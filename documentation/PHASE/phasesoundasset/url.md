# url

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

The URL of the sound asset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var url: URL? { get }
```

```objc
@property (readonly, nullable) NSURL * url;
```

#### Discussion

This property has a value when an app creates the asset with [`registerSoundAsset(url:identifier:assetType:channelLayout:normalizationMode:)`](../phaseassetregistry/registersoundasset%28url,identifier,assettype,channellayout,normalizationmode%29.md); otherwise the value is `nil`.

## See Also

### Accessing Sound Data
- [var data: Data?](./data.md)
  A storage buffer for the sound asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundasset/url)*