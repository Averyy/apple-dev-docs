# data

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

A storage buffer for the sound asset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var data: Data? { get }
```

```objc
@property (readonly, nullable) NSData * data;
```

## Discussion

This property has a value when an app creates the asset with [`registerSoundAsset(data:identifier:format:normalizationMode:)`](../phaseassetregistry/registersoundasset%28data,identifier,format,normalizationmode%29.md); otherwise the value is `nil`.

## See Also

### Accessing Sound Data
- [var url: URL?](./url.md)
  The URL of the sound asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundasset/data)*