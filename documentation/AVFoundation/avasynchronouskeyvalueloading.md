# AVAsynchronousKeyValueLoading

**Framework**: AVFoundation  
**Kind**: protocol

A protocol that defines the interface to load media data asynchronously.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol AVAsynchronousKeyValueLoading
```

## Mentions

- [Loading media data asynchronously](loading-media-data-asynchronously.md)

#### Overview

Loading media data takes an amount of time that depends on factors including the media’s size, location, device capabilities, network conditions, and so on. To optimize performance, [`AVAsset`](avasset.md) defers loading its media data until you query its properties or perform an operation that requires it. This means that performing these actions from a synchronous context would block the calling thread for an unknown amount of time, which would result in a poor user experience, and may even cause your app to crash. For this reason, you must load media data asynchronously.

Call the asynchronous `load(_:)` method to retrieve the values of media properties, or determine the loaded status of a property by calling the [`status(of:)`](avasynchronouskeyvalueloading/status(of:).md) method. See [`Loading media data asynchronously`](loading-media-data-asynchronously.md) for more information.

## Topics

### Determining the Loaded Status
- [func status<T>(of: AVAsyncProperty<Self, T>) -> AVAsyncProperty<Self, T>.Status](avasynchronouskeyvalueloading/status(of:).md)
  Returns a value that indicates the loaded status of a property.
### Deprecated
- [Deprecated Symbols](avasynchronouskeyvalueloading-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
- [func loadValuesAsynchronously(forKeys: [String], completionHandler: (() -> Void)?)](avasynchronouskeyvalueloading/loadvaluesasynchronously(forkeys:completionhandler:).md)
  Tells the asset to load the values of all of the specified keys that aren’t already loaded.
- [func statusOfValue(forKey: String, error: NSErrorPointer) -> AVKeyValueStatus](avasynchronouskeyvalueloading/statusofvalue(forkey:error:).md)
  Returns a status that indicates whether a property value is immediately available without blocking the calling thread.
- [enum AVKeyValueStatus](avkeyvaluestatus.md)
  Values that indicate the loaded status of a property.
### Instance Methods
- [func load<A, B, each C>(AVAsyncProperty<Self, A>, AVAsyncProperty<Self, B>, repeat AVAsyncProperty<Self, each C>, isolation: isolated (any Actor)?) async throws -> (A, B, repeat each C)](avasynchronouskeyvalueloading/load(_:_:_:isolation:).md)
- [func load<T>(AVAsyncProperty<Self, T>, isolation: isolated (any Actor)?) async throws -> T](avasynchronouskeyvalueloading/load(_:isolation:).md)

## Relationships

### Conforming Types
- [AVAsset](avasset.md)
- [AVAssetTrack](avassettrack.md)
- [AVComposition](avcomposition.md)
- [AVCompositionTrack](avcompositiontrack.md)
- [AVFragmentedAsset](avfragmentedasset.md)
- [AVFragmentedAssetTrack](avfragmentedassettrack.md)
- [AVFragmentedMovie](avfragmentedmovie.md)
- [AVFragmentedMovieTrack](avfragmentedmovietrack.md)
- [AVMetadataItem](avmetadataitem.md)
- [AVMovie](avmovie.md)
- [AVMovieTrack](avmovietrack.md)
- [AVMutableComposition](avmutablecomposition.md)
- [AVMutableCompositionTrack](avmutablecompositiontrack.md)
- [AVMutableMetadataItem](avmutablemetadataitem.md)
- [AVMutableMovie](avmutablemovie.md)
- [AVMutableMovieTrack](avmutablemovietrack.md)
- [AVURLAsset](avurlasset.md)

## See Also

- [class AVAsyncProperty](avasyncproperty.md)
  An asynchronous property that constrains its type and value.
- [class AVPartialAsyncProperty](avpartialasyncproperty.md)
  An asynchronous property that constrains its type.
- [class AVAnyAsyncProperty](avanyasyncproperty.md)
  A base class for asynchronous properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading)*