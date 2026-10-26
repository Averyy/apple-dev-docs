# URLAssetWithURL:options:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns an asset that models the media resource found at the specified URL.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```objc
+ (instancetype) URLAssetWithURL:(NSURL *) URL options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

An asset that models the media resource found at `URL`.

## Parameters

- `URL`: A URL that references the media for the asset to model.
- `options`: A dictionary that contains options used to customize the initialization of the asset.

  For possible keys and values, see [Initialization options](../initialization-options.md).

## See Also

### Creating an asset
- [init(url: URL, options: [String : Any]?)](./init%28url,options%29-2x8uu.md)
  Creates an asset that models the media resource at the specified URL.
- [Initialization options](../avurlasset-initialization-options.md)
  Specify options to configure the initialization of a media asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/urlassetwithurl:options:)*