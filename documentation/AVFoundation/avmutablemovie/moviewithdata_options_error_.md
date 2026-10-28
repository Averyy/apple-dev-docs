# movieWithData:options:error:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new mutable movie object from a movie stored in a data object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
+ (instancetype) movieWithData:(NSData *) data options:(NSDictionary<NSString *,id> *) options error:(NSError **) outError;
```

## Return Value

An `AVMutableMovie` object.

## Discussion

On initialization, the [`defaultMediaDataStorage`](./defaultmediadatastorage.md) property and any associated [`mediaDataStorage`](../avmutablemovietrack/mediadatastorage.md) properties are set to `nil`. To create an `AVMutableMovie` from a file and then append sample buffers to any of its tracks, you must first set one of these properties to indicate where the sample data should be written.

Use this method to create movies from movie headers that are not stored in files, which can include movies on the pasteboard.

## Parameters

- `data`: An `NSData` object that contains a movie header.
- `options`: A dictionary that contains key for specifying the movie object initialization. Currently, no keys are defined.
- `outError`: A description of the error that occurred. Default value is `nil`.

## See Also

### Creating a movie
- [+ movieWithURL:options:error:](./moviewithurl_options_error_.md)
  Returns a new mutable movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [init(url: URL, options: [String : Any]?, error: ()) throws](./init%28url,options,error%29-8rnnj.md)
  Creates a mutable movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [init(data: Data, options: [String : Any]?, error: ()) throws](./init%28data,options,error%29.md)
  Creates a mutable movie object from a movie stored in a data object.
- [+ movieWithSettingsFromMovie:options:error:](./moviewithsettingsfrommovie_options_error_.md)
  Returns a new mutable movie object without tracks.
- [init(settingsFrom: AVMovie?, options: [String : Any]?) throws](./init%28settingsfrom,options%29.md)
  Creates a mutable movie object without tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/moviewithdata:options:error:)*