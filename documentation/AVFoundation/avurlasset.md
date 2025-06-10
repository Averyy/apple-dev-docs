# AVURLAsset

**Framework**: AVFoundation  
**Kind**: class

An asset that represents media at a local or remote URL.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class AVURLAsset
```

#### Overview

This class is a concrete subclass of [`AVAsset`](avasset.md). When you create an asset as shown below, the system creates and returns an instance of [`AVURLAsset`](avurlasset.md).

```swift
// A local or remote asset URL.
guard let url: URL = Bundle.main.url(forResource: "Image",
                                     withExtension: "png") else { return }
let asset = AVAsset(url: url)
```

In many cases, this is an appropriate way to create asset instances, but you can also directly instantiate an [`AVURLAsset`](avurlasset.md) when you need more fine-grained control over its initialization. The initializer for [`AVURLAsset`](avurlasset.md) accepts an options dictionary, which you use to customize the asset’s initialization for your particular purpose. For example, if you’re creating an asset for an HLS stream, you may want to prevent it from retrieving its media when it connects over a cellular network. You can do this by providing the initialization option and value as shown below.

```swift
let url: URL = // A remote asset URL.
let options = [AVURLAssetAllowsCellularAccessKey: false]
let asset = AVURLAsset(url: url, options: options)
```

## Topics

### Creating an Asset
- [convenience init(url: URL)](avurlasset/init(url:).md)
  Creates an asset that models the media at the specified URL.
- [init(url: URL, options: [String : Any]?)](avurlasset/init(url:options:).md)
  Creates an asset that models the media resource at the specified URL.
- [Initialization Options](avurlasset-initialization-options.md)
  Specify options to configure the initialization of a media asset.
### Loading Tracks
- [static var tracks: AVAsyncProperty<Root, [AVAssetTrack]>](avpartialasyncproperty/tracks-44ptx.md)
  The tracks an asset contains.
- [func findCompatibleTrack(for: AVCompositionTrack, completionHandler: (AVAssetTrack?, (any Error)?) -> Void)](avurlasset/findcompatibletrack(for:completionhandler:).md)
  Loads an asset track from which you can insert any time range into the composition track.
### Loading Variants
- [static var variants: AVAsyncProperty<Root, [AVAssetVariant]>](avpartialasyncproperty/variants.md)
  An array of variants that an asset contains.
### Determining Supported Media Types
- [class func audiovisualTypes() -> [AVFileType]](avurlasset/audiovisualtypes.md)
  Returns an array of the file types the asset supports.
- [class func audiovisualMIMETypes() -> [String]](avurlasset/audiovisualmimetypes.md)
  Returns an array of the MIME types the asset supports.
- [class func isPlayableExtendedMIMEType(String) -> Bool](avurlasset/isplayableextendedmimetype(_:).md)
  Returns a Boolean value that indicates whether the asset is playable with the specified codecs and container type.
### Assisting with Resource Loading
- [var resourceLoader: AVAssetResourceLoader](avurlasset/resourceloader.md)
  The resource loader for the asset.
- [var mayRequireContentKeysForMediaDataProcessing: Bool](avurlasset/mayrequirecontentkeysformediadataprocessing.md)
  A Boolean value that indicates whether you can add this asset as a content key recipient to a content key session.
### Working with Offline Assets
- [var assetCache: AVAssetCache?](avurlasset/assetcache.md)
  The asset’s associated asset cache, if it exists.
### Accessing the Media URL
- [var url: URL](avurlasset/url.md)
  A URL to the asset’s media.
### Accessing Asset Variants
- [var variants: [AVAssetVariant]](avurlasset/variants.md)
  An array of variants that an asset contains.
### Accessing Compatible Tracks
- [func compatibleTrack(for: AVCompositionTrack) -> AVAssetTrack?](avurlasset/compatibletrack(for:).md)
  Returns an asset track from which you can insert any time range into a given composition track.
### Accessing the Session Identifier
- [var httpSessionIdentifier: UUID](avurlasset/httpsessionidentifier.md)
  A session identifier that the asset sends in HTTP requests that it makes.
### Accessing Media Extension Properties
- [var mediaExtensionProperties: AVMediaExtensionProperties?](avurlasset/mediaextensionproperties.md)
  The properties of the media extension format reader that decodes the asset.
- [class AVMediaExtensionProperties](avmediaextensionproperties.md)
  An object that describes a Media Extension.
### Type Properties
- [class var audiovisualContentTypes: [UTType]](avurlasset/audiovisualcontenttypes.md)
  Provides the content types the AVURLAsset class understands.

## Relationships

### Inherits From
- [AVAsset](avasset.md)
### Inherited By
- [AVFragmentedAsset](avfragmentedasset.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md)
- [AVContentKeyRecipient](avcontentkeyrecipient.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSItemProviderReading](../Foundation/NSItemProviderReading.md)
- [NSItemProviderWriting](../Foundation/NSItemProviderWriting.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVAsset](avasset.md)
  An object that models timed audiovisual media.
- [class AVAssetTrack](avassettrack.md)
  An object that models a track of media that an asset contains.
- [class AVAssetTrackSegment](avassettracksegment.md)
  An object that represents a time range segment of an asset track.
- [class AVAssetTrackGroup](avassettrackgroup.md)
  A group of related tracks in an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset)*