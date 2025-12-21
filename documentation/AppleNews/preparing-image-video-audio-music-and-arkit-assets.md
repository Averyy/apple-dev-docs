# Preparing Image, Video, Audio, Music, and ARKit Assets

**Framework**: Apple News

Add media assets to your article.

#### Overview

Images, videos, audio, music, and ARKit files serve a variety of purposes in your article. For example:

- Use an image as a logo, as a background, or as a placeholder for a video while it’s not playing.
- Use video files in an article to enhance the user’s experience, or as the thumbnail that represents the article in the user’s News feed.
- Use the audio or music component to include audio files in the article.

When you use such files, you provide the encoded URL in an Apple News Format property, and the asset based on the specifications given here. Which URL property you use depends on whether the file is an image, video, audio, music, or ARKit file, and how you use it.

> ❗ **Important**:  The maximum allowable file size for your article bundle, including remote and local media assets, is 450 MB. Verify that the total size of your article bundle doesn’t exceed this limit.

##### Provide the Url in an Apple News Format Property

To include an asset in your article, provide a well-formatted and encoded URL to specify the location of the asset file.

Apple News uses its user agent, AppleNewsBot, to access remote URLs. Apple News uses this user agent only for the purposes of accessing remote resources included in Apple News articles.

To learn which URL property to use, see [`Audio`](https://developer.apple.com/documentation/applenewsformat/audio), [`ArticleThumbnail`](https://developer.apple.com/documentation/applenewsformat/articlethumbnail), [`DataTable`](https://developer.apple.com/documentation/applenewsformat/datatable), [`Figure`](https://developer.apple.com/documentation/applenewsformat/figure), [`Image`](https://developer.apple.com/documentation/applenewsformat/image), [`Logo`](https://developer.apple.com/documentation/applenewsformat/logo), [`Music`](https://developer.apple.com/documentation/applenewsformat/music), [`Photo`](https://developer.apple.com/documentation/applenewsformat/photo), [`Portrait`](https://developer.apple.com/documentation/applenewsformat/portrait), [`Video`](https://developer.apple.com/documentation/applenewsformat/video), [`ImageFill`](https://developer.apple.com/documentation/applenewsformat/imagefill), [`RepeatableImageFill`](https://developer.apple.com/documentation/applenewsformat/repeatableimagefill), [`VideoFill`](https://developer.apple.com/documentation/applenewsformat/videofill), [`GalleryItem`](https://developer.apple.com/documentation/applenewsformat/galleryitem), [`Mosaic`](https://developer.apple.com/documentation/applenewsformat/mosaic), [`Metadata`](https://developer.apple.com/documentation/applenewsformat/metadata), or [`ARKit`](https://developer.apple.com/documentation/applenewsformat/arkit).

. Apple News Format supports the following prefixes for URLs:

- `http://`
- `https://`
- `bundle://` — If you are using the `URL` property, Apple News Format doesn’t support the `bundle://` prefix for [`Video`](https://developer.apple.com/documentation/applenewsformat/video) and [`Audio`](https://developer.apple.com/documentation/applenewsformat/audio) objects. For [`Audio`](https://developer.apple.com/documentation/applenewsformat/audio),  [`Music`](https://developer.apple.com/documentation/applenewsformat/music),  [`Video`](https://developer.apple.com/documentation/applenewsformat/video), and  [`VideoFill`](https://developer.apple.com/documentation/applenewsformat/videofill) objects use, `bundle://` for `imageURL` and `stillURL`. When a URL begins with `bundle://`, you must include the referenced file in the same directory as the JSON document.

. This example shows layered encoding for `markdown` format.

```json
{
  "role": "body",
  "format": "markdown",
  "text": "\\([Library of Congress](http://memory.loc.gov/cgi-bin/query/h?ammem/rbpebib:@field%28NUMBER+@band%28rbpe%2B1310110b%29%29)\\)"
}
```

##### Prepare an Image Asset

Follow the steps below to include an image in your article.

 JPEG (`.jpg` or `.jpeg` extension), WebP, PNG, and GIF are all supported, but JPEG with high-quality compression setting is preferred. Use PNG only if you need transparency. Note that Apple News Format removes animations from animated WebP images.

. Apple News Format automatically scales the image to the correct size, and high-resolution images scale smoothly.

. This color profile creates images that are well suited both for Apple devices that support a wide color gamut and for those that donʼt.

. Don’t exceed 20 MB for the image file size. Neither the height nor the width should exceed 6,000 pixels. Avoid using images that are tall and narrow because they don’t render well across all devices.

 There is no universal minimum size for images; the size of the component determines the minimum image width. For example, full width for an article designed for 1,024-point width and 120-point margins is different from full width for an article designed with different specifications.

The recommended minimum widths are as follows:

- [`Photo`](https://developer.apple.com/documentation/applenewsformat/photo), [`Portrait`](https://developer.apple.com/documentation/applenewsformat/portrait), [`Gallery`](https://developer.apple.com/documentation/applenewsformat/gallery), and [`Mosaic`](https://developer.apple.com/documentation/applenewsformat/mosaic) components: 640 pixels.
- [`Logo`](https://developer.apple.com/documentation/applenewsformat/logo) component: 300 pixels.
- [`Figure`](https://developer.apple.com/documentation/applenewsformat/figure) component: 1,080 pixels.

For images that span the full width of the document or the device, the recommended widths are as follows:

- Full width of the document.  At least as wide as the document, as specified in `layout.width`. See [`Layout`](https://developer.apple.com/documentation/applenewsformat/layout).
- Full width of the device. At least 1,366 pixels, to support larger devices.

. RGB — Red, Green, and Blue — is the only color mode that is compatible with Apple News. Don’t use CMYK — Cyan, Magenta, Yellow, and Key (black).

. Automatic Dark Mode doesn’t transform images in any way. To ensure that images display clearly on a screen with a light appearance or in Dark Mode, avoid images with white backgrounds. When this isn’t possible, the following techniques can improve the Dark Mode experience:

- Make the images bleed to both edges of the display.
- Provide even padding in images.

##### Prepare a Thumbnail Image Asset

For each article you publish, Apple News Format automatically creates an . An article tile provides information about the article. It uses information from the article’s [`Metadata`](https://developer.apple.com/documentation/applenewsformat/metadata) object and appears in feeds, such as the Today feed, channel feeds, and topic feeds. Use `thumbnailURL` in your article metadata to specify the image you want to use in the article tile.

. JPEG (`.jpg` or `.jpeg` extension), WebP, PNG, and GIF are all supported, but JPEG with high-quality compression setting is preferred. Use PNG only if you need transparency. Note that animations are removed from WebP and GIF images.

. The image is automatically scaled to the correct size, and high-resolution images scale smoothly.

. The minimum size of a thumbnail image is 300 pixels by 300 pixels.

. The aspect ratio is the proportion of an image’s width to its height and should be between 0.5 and 3.0.

. This color profile creates images that are well suited both for Apple devices that support a wide color gamut and for those that donʼt.

.  If you use the same image in both places and it appears on the first screen of the article, it moves with an animated effect from the feed to the article. Using the same image improves the loading time of the article.

##### Prepare a Video Asset

Follow the steps below to include a [`Video`](https://developer.apple.com/documentation/applenewsformat/video) or a [`VideoFill`](https://developer.apple.com/documentation/applenewsformat/videofill) in your article.

 Use the `stillURL` property to specify the URL of the image file to use as a still image when the video isn’t playing. This property is required for [`VideoFill`](https://developer.apple.com/documentation/applenewsformat/videofill) and optional for [`Video`](https://developer.apple.com/documentation/applenewsformat/video). To avoid letterboxing, make the aspect ratio of the `stillURL` image file match that of  the video.

. The video URL should begin with `https://` (preferred) or `http://`.

 M3U playlist is the preferred format. For more information about HLS, see the iOS developer documentation about [`HTTP Live Streaming`](https://developer.apple.comhttps://developer.apple.com/streaming/).

##### Prepare a Video for Feeds

To add a video to your article, specify the `videoURL` property to the [`Metadata`](https://developer.apple.com/documentation/applenewsformat/metadata) object. You can also specify an image to use as the thumbnail image (`thumbnailURL`) when the video hasn’t played yet. A glyph appears on the thumbnail image, allowing people to play the video in feeds, such as the Today feed, channel feeds, and topic feeds.

. Apple News Format supports the following prefixes for video URLs:

- `https://` (preferred)
- `http://`

 `videoURL` . Provide the same `videoURL` property value to the [`Metadata`](https://developer.apple.com/documentation/applenewsformat/metadata) object and the [`Video`](https://developer.apple.com/documentation/applenewsformat/video) component in the article.

 `thumbnailURL`  Provide the same `thumbnailURL` property value to the [`Metadata`](https://developer.apple.com/documentation/applenewsformat/metadata) object and the [`Video`](https://developer.apple.com/documentation/applenewsformat/video) component’s `stillURL`. Using the same image ensures that playback continues seamlessly from a video playing in the feed to the same video that plays when the article opens.

. M3U playlist is the preferred format. For more information about HLS, see [`HTTP Live Streaming`](https://developer.apple.comhttps://developer.apple.com/streaming/).

##### Prepare an Audio Asset

Configure the [`Audio`](https://developer.apple.com/documentation/applenewsformat/audio) or [`Music`](https://developer.apple.com/documentation/applenewsformat/music) component to include an audio file in your article.

 Apple News Format supports the following prefixes for audio URLs:

- `https://` (preferred)
- `http://`

. This property adds an audio or music file to the article.

. The supported formats are MP3, AAC, ALAC, and HE-AAC.

## See Also

- [Specifying Measurements for Components](specifying-measurements-for-components.md)
  Specify the units of measure to use for margins, minimum heights, and other dimensions.
- [type SupportedUnits](../applenewsformat/supportedunits.md)
  The units of measurement Apple News Format supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/preparing-image-video-audio-music-and-arkit-assets)*