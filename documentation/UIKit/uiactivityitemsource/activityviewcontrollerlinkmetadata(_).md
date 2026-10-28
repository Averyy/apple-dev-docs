# activityViewControllerLinkMetadata(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns metadata to display in the preview header of the share sheet.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func activityViewControllerLinkMetadata(_ activityViewController: UIActivityViewController) -> LPLinkMetadata?
```

```objc
- (LPLinkMetadata *) activityViewControllerLinkMetadata:(UIActivityViewController *) activityViewController;
```

## Return Value

The [`LPLinkMetadata`](../../LinkPresentation/lplinkmetadata.md) object that contains the metadata about a URL, including its title, icon, images, and video.

## Discussion

Using the [Link Presentation](../../LinkPresentation/LinkPresentation.md) framework, you can display rich previews of web links inside your app. For instance, if your app already has a database of links, with titles and images that weren’t fetched by [`LPMetadataProvider`](../../LinkPresentation/lpmetadataprovider.md), you don’t have to fetch new metadata from the internet. Use this method instead and avoid downloading it again.

In your implementation, create an [`LPLinkMetadata`](../../LinkPresentation/lplinkmetadata.md) object, and fill in at least the [`originalURL`](../../LinkPresentation/lplinkmetadata/originalurl.md) and [`url`](../../LinkPresentation/lplinkmetadata/url.md) fields, plus whatever additional information you have.

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

To learn more about presenting rich links and accelerating the share sheet, see [Link Presentation](../../LinkPresentation/LinkPresentation.md) and [`LPMetadataProvider`](../../LinkPresentation/lpmetadataprovider.md), or watch the WWDC 2019 session [262: Embedding and Sharing Visually Rich Links](https://developer.apple.com/videos/play/wwdc2019/262/).

## Parameters

- `activityViewController`: The [`UIActivityViewController`](../uiactivityviewcontroller.md) object requesting information about the item that the user wants to share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsource/activityviewcontrollerlinkmetadata(_:))*