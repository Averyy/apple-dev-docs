# init(url:options:)

**Framework**: AVFoundation  
**Kind**: init

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

#### Return Value

An asset that models the media resource found at `URL`.

## Parameters

- `URL`: A URL that references the media for the asset to model.
- `options`: For supported keys and values, see  .

## See Also

- [convenience init(url: URL)](avurlasset/init(url:).md)
  Creates an asset that models the media at the specified URL.
- [Initialization Options](avurlasset-initialization-options.md)
  Specify options to configure the initialization of a media asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/init(url:options:))*