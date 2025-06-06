# LPLinkMetadata

**Framework**: Link Presentation  
**Kind**: class

An object that contains metadata about a URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class LPLinkMetadata
```

#### Overview

Use [`LPLinkMetadata`](lplinkmetadata.md) to store the metadata about a URL, including its title, icon, images and video.

Fetch metadata using [`LPMetadataProvider`](lpmetadataprovider.md). For remote URLs, cache the metadata locally to avoid the data and performance cost of fetching it from the internet every time you present it. [`LPLinkMetadata`](lplinkmetadata.md) is serializable with [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding).

For local file URLs, the [`Quick Look Thumbnailing`](https://developer.apple.com/documentation/QuickLookThumbnailing) API retrieves a representative thumbnail for the file, if possible.

#### Provide Custom Metadata

Say your app already has a database of links, with titles and images that weren’t fetched by [`LPMetadataProvider`](lpmetadataprovider.md). You don’t have to fetch new metadata from the internet in order to accelerate the share sheet or to present a rich link. Instead, you can fill in the fields of [`LPLinkMetadata`](lplinkmetadata.md) yourself.

Create an [`LPLinkMetadata`](lplinkmetadata.md) object, and fill in at least the [`originalURL`](lplinkmetadata/originalurl.md) and [`url`](lplinkmetadata/url.md) fields, plus whatever additional information you have.

```swift
func activityViewControllerLinkMetadata(_: UIActivityViewController) -> LPLinkMetadata? {
    let metadata = LPLinkMetadata()
    metadata.originalURL = URL(string: "https://www.example.com/apple-pie")
    metadata.url = metadata.originalURL
    metadata.title = "The Greatest Apple Pie In The World"
    metadata.imageProvider = NSItemProvider.init(contentsOf:
        Bundle.main.url(forResource: "apple-pie", withExtension: "jpg"))
    return metadata
}
```

#### Accelerate the Share Sheet Preview

For existing apps that share URLs, the share sheet automatically presents a preview of the link. The preview first shows a placeholder link icon alongside the base URL while fetching the link’s metadata over the network. The preview updates once the link’s icon and title become available.

If you already have an [`LPLinkMetadata`](lplinkmetadata.md) object for a URL, pass it to the share sheet to present the preview instantly, without fetching data over the network. In your implementation of [`activityViewControllerLinkMetadata(_:)`](https://developer.apple.com/documentation/UIKit/UIActivityItemSource/activityViewControllerLinkMetadata(_:)), return the metadata object.

```swift
func activityViewControllerLinkMetadata(_:
UIActivityViewController) -> LPLinkMetadata? {
    return self.metadata
}
```

If the user chooses to share to Messages, the same metadata passes directly through, providing a smooth and seamless experience with no unnecessary loading.

## Topics

### Identifying the link
- [var url: URL?](lplinkmetadata/url.md)
  The URL that returned the metadata, taking server-side redirects into account.
- [var originalURL: URL?](lplinkmetadata/originalurl.md)
  The original URL of the metadata request.
### Getting the link’s title
- [var title: String?](lplinkmetadata/title.md)
  A representative title for the URL.
### Getting the link’s images
- [var iconProvider: NSItemProvider?](lplinkmetadata/iconprovider.md)
  An object that retrieves data corresponding to a representative icon for the URL.
- [var imageProvider: NSItemProvider?](lplinkmetadata/imageprovider.md)
  An object that retrieves data corresponding to a representative image for the URL.
### Getting the link’s video
- [var remoteVideoURL: URL?](lplinkmetadata/remotevideourl.md)
  A remote URL corresponding to a representative video for the URL.
- [var videoProvider: NSItemProvider?](lplinkmetadata/videoprovider.md)
  An object that retrieves data corresponding to a representative video for the URL.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class LPMetadataProvider](lpmetadataprovider.md)
  An object that retrieves metadata for a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lplinkmetadata)*