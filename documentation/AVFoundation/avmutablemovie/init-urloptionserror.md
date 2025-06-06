# init(url:options:error:)

**Framework**: AVFoundation  
**Kind**: init

Creates a mutable movie object from a movie header stored in a QuickTime movie file of ISO base media file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(url URL: URL, options: [String : Any]? = nil, error: ()) throws
```

#### Return Value

An `AVMutableMovie` object.

#### Discussion

On initialization, the [`defaultMediaDataStorage`](avmutablemovie/defaultmediadatastorage.md) property and any associated [`mediaDataStorage`](avmutablemovietrack/mediadatastorage.md) properties are set to `nil`. To create an `AVMutableMovie` from a file and then append sample buffers to any of its tracks, you must first set one of these properties to indicate where the sample data should be written.

## Parameters

- `URL`: The URL that points to a file containing a movie header.
- `options`: A dictionary that contains key for specifying the movie object initialization. Currently, no keys are defined.

## See Also

- [init(data: Data, options: [String : Any]?, error: ()) throws](avmutablemovie/init(data:options:error:).md)
  Creates a mutable movie object from a movie stored in a data object.
- [init(settingsFrom: AVMovie?, options: [String : Any]?) throws](avmutablemovie/init(settingsfrom:options:).md)
  Creates a mutable movie object without tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/init(url:options:error:))*