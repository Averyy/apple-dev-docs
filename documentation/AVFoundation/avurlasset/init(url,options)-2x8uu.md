# init(url:options:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates an asset that models the media resource at the specified URL.

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
init(url URL: URL, options: [String : Any]? = nil)
```

```objc
- (instancetype) initWithURL:(NSURL *) URL options:(NSDictionary<NSString *,id> *) options;
```

## Return Value

An asset that models the media resource found at `URL`.

## Parameters

- `URL`: A URL that references the media for the asset to model.
- `options`: A dictionary that contains options used to customize the initialization of the asset.

  For supported keys and values, see [Initialization options](../initialization-options.md).

## See Also

### Creating an asset
- [convenience init(url: URL)](./init%28url%29.md)
  Creates an asset that models the media at the specified URL.
- [Initialization options](../avurlasset-initialization-options.md)
  Specify options to configure the initialization of a media asset.
- [+ URLAssetWithURL:options:](./urlassetwithurl_options_.md)
  Returns an asset that models the media resource found at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/init(url:options:)-2x8uu)*