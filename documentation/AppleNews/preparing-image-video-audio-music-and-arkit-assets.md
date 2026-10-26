# Preparing Image, Video, Audio, Music, and ARKit Assets

**Framework**: Apple News  
**Role**: Article

Add media assets to your article.

#### Overview

Images, videos, audio, music, and ARKit files serve a variety of purposes in your article. For example:

- Use an image as a logo, as a background, or as a placeholder for a video while it’s not playing.
- Use video files in an article to enhance the user’s experience, or as the thumbnail that represents the article in the user’s News feed.
- Use the audio or music component to include audio files in the article.

When you use such files, you provide the encoded URL in an Apple News Format property, and the asset based on the specifications given here. Which URL property you use depends on whether the file is an image, video, audio, music, or ARKit file, and how you use it.

> ❗ **Important**:  The maximum allowable file size for your article bundle, including remote and local media assets, is 450 MB. Verify that the total size of your article bundle doesn’t exceed this limit.

##### Provide the URL in an Apple News Format Property

To include an asset in your article, provide a well-formatted and encoded URL to specify the location of the asset file.

Apple News uses its user agent, AppleNewsBot, to access remote URLs. Apple News uses this user agent only for the purposes of accessing remote resources included in Apple News articles.

To learn which URL property to use, see [`Audio`](../AppleNewsFormat/audio.md), [`ArticleThumbnail`](../AppleNewsFormat/articlethumbnail.md), [`DataTable`](../AppleNewsFormat/datatable.md), [`Figure`](../AppleNewsFormat/figure.md), [`Image`](../AppleNewsFormat/image.md), [`Logo`](../AppleNewsFormat/logo.md), [`Music`](../AppleNewsFormat/music.md), [`Photo`](../AppleNewsFormat/photo.md), [`Portrait`](../AppleNewsFormat/portrait.md), [`Video`](../AppleNewsFormat/video.md), [`ImageFill`](../AppleNewsFormat/imagefill.md), [`RepeatableImageFill`](../AppleNewsFormat/repeatableimagefill.md), [`VideoFill`](../AppleNewsFormat/videofill.md), [`GalleryItem`](../AppleNewsFormat/galleryitem.md), [`Mosaic`](../AppleNewsFormat/mosaic.md), [`Metadata`](../AppleNewsFormat/metadata.md), or [`ARKit`](../AppleNewsFormat/arkit.md).

**Include the URL’s prefix**. Apple News Format supports the following prefixes for URLs:

- `http://`
- `https://`
- `bundle://` — If you are using the `URL` property, Apple News Format doesn’t support the `bundle://` prefix for [`Video`](../AppleNewsFormat/video.md) and [`Audio`](../AppleNewsFormat/audio.md) objects. For [`Audio`](../AppleNewsFormat/audio.md),  [`Music`](../AppleNewsFormat/music.md),  [`Video`](../AppleNewsFormat/video.md), and  [`VideoFill`](../AppleNewsFormat/videofill.md) objects use, `bundle://` for `imageURL` and `stillURL`. When a URL begins with `bundle://`, you must include the referenced file in the same directory as the JSON document.

**Use layered encoding for links nested within special characters or formats**. This example shows layered encoding for `markdown` format.

```json
{
  "role": "body",
  "format": "markdown",
  "text": "\\([Library of Congress](http://memory.loc.gov/cgi-bin/query/h?ammem/rbpebib:@field%28NUMBER+@band%28rbpe%2B1310110b%29%29)\\)"
}
```

##### Prepare an Image Asset

Follow the steps below to include an image in your article.

**Use a supported image type.** JPEG (`.jpg` or `.jpeg` extension), WebP, PNG, and GIF are all supported, but JPEG with high-quality compression setting is preferred. Use PNG only if you need transparency. Note that Apple News Format removes animations from animated WebP images.

**Choose a high-resolution image**. Apple News Format automatically scales the image to the correct size, and high-resolution images scale smoothly.

**Use the Display P3 color profile**. This color profile creates images that are well suited both for Apple devices that support a wide color gamut and for those that donʼt.

**Check the size of the image**. Don’t exceed 20 MB for the image file size. Neither the height nor the width should exceed 6,000 pixels. Avoid using images that are tall and narrow because they don’t render well across all devices.

**Use the recommended minimum image width.** There is no universal minimum size for images; the size of the component determines the minimum image width. For example, full width for an article designed for 1,024-point width and 120-point margins is different from full width for an article designed with different specifications.

The recommended minimum widths are as follows:

- [`Photo`](../AppleNewsFormat/photo.md), [`Portrait`](../AppleNewsFormat/portrait.md), [`Gallery`](../AppleNewsFormat/gallery.md), and [`Mosaic`](../AppleNewsFormat/mosaic.md) components: 640 pixels.
- [`Logo`](../AppleNewsFormat/logo.md) component: 300 pixels.
- [`Figure`](../AppleNewsFormat/figure.md) component: 1,080 pixels.

For images that span the full width of the document or the device, the recommended widths are as follows:

- Full width of the document.  At least as wide as the document, as specified in `layout.width`. See [`Layout`](../AppleNewsFormat/layout.md).
- Full width of the device. At least 1,366 pixels, to support larger devices.

**Use only RGB color mode for images**. RGB — Red, Green, and Blue — is the only color mode that is compatible with Apple News. Don’t use CMYK — Cyan, Magenta, Yellow, and Key (black).

**Optimize images for Dark Mode**. Automatic Dark Mode doesn’t transform images in any way. To ensure that images display clearly on a screen with a light appearance or in Dark Mode, avoid images with white backgrounds. When this isn’t possible, the following techniques can improve the Dark Mode experience:

- Make the images bleed to both edges of the display.
- Provide even padding in images.

##### Prepare a Thumbnail Image Asset

For each article you publish, Apple News Format automatically creates an *article tile*. An article tile provides information about the article. It uses information from the article’s [`Metadata`](../AppleNewsFormat/metadata.md) object and appears in feeds, such as the Today feed, channel feeds, and topic feeds. Use `thumbnailURL` in your article metadata to specify the image you want to use in the article tile.

**Use a supported image type**. JPEG (`.jpg` or `.jpeg` extension), WebP, PNG, and GIF are all supported, but JPEG with high-quality compression setting is preferred. Use PNG only if you need transparency. Note that animations are removed from WebP and GIF images.

**Choose a high-resolution image**. The image is automatically scaled to the correct size, and high-resolution images scale smoothly.

**Check the size of the image**. The minimum size of a thumbnail image is 300 pixels by 300 pixels.

**Verify the image aspect ratio**. The aspect ratio is the proportion of an image’s width to its height and should be between 0.5 and 3.0.

**Use the Display P3 color profile**. This color profile creates images that are well suited both for Apple devices that support a wide color gamut and for those that donʼt.

**Use an image from the article as the thumbnail image**.  If you use the same image in both places and it appears on the first screen of the article, it moves with an animated effect from the feed to the article. Using the same image improves the loading time of the article.

##### Prepare a Video Asset

Follow the steps below to include a [`Video`](../AppleNewsFormat/video.md) or a [`VideoFill`](../AppleNewsFormat/videofill.md) in your article.

**Include a still image.** Use the `stillURL` property to specify the URL of the image file to use as a still image when the video isn’t playing. This property is required for [`VideoFill`](../AppleNewsFormat/videofill.md) and optional for [`Video`](../AppleNewsFormat/video.md). To avoid letterboxing, make the aspect ratio of the `stillURL` image file match that of  the video.

**Use the URL property to specify the location of the video file**. The video URL should begin with `https://` (preferred) or `http://`.

**Use supported HLS formats.** M3U playlist is the preferred format. For more information about HLS, see the iOS developer documentation about [HTTP Live Streaming](https://developer.apple.com/streaming/).

##### Prepare a Video for Feeds

To add a video to your article, specify the `videoURL` property to the [`Metadata`](../AppleNewsFormat/metadata.md) object. You can also specify an image to use as the thumbnail image (`thumbnailURL`) when the video hasn’t played yet. A glyph appears on the thumbnail image, allowing people to play the video in feeds, such as the Today feed, channel feeds, and topic feeds.

**Provide a URL**. Apple News Format supports the following prefixes for video URLs:

- `https://` (preferred)
- `http://`

**Use the same video URL for the Metadata** `videoURL` **property**. Provide the same `videoURL` property value to the [`Metadata`](../AppleNewsFormat/metadata.md) object and the [`Video`](../AppleNewsFormat/video.md) component in the article.

**Use the same image for the Metadata** `thumbnailURL` **property.** Provide the same `thumbnailURL` property value to the [`Metadata`](../AppleNewsFormat/metadata.md) object and the [`Video`](../AppleNewsFormat/video.md) component’s `stillURL`. Using the same image ensures that playback continues seamlessly from a video playing in the feed to the same video that plays when the article opens.

**Use supported HLS formats**. M3U playlist is the preferred format. For more information about HLS, see [HTTP Live Streaming](https://developer.apple.com/streaming/).

##### Prepare an Audio Asset

Configure the [`Audio`](../AppleNewsFormat/audio.md) or [`Music`](../AppleNewsFormat/music.md) component to include an audio file in your article.

**Provide a URL.** Apple News Format supports the following prefixes for audio URLs:

- `https://` (preferred)
- `http://`

**Use the imageURL property**. This property adds an audio or music file to the article.

**Use a supported AVPlayer audio format**. The supported formats are MP3, AAC, ALAC, and HE-AAC.

## See Also

### Component Measurements and Media Guidelines
- [Specifying Measurements for Components](./specifying-measurements-for-components.md)
  Specify the units of measure to use for margins, minimum heights, and other dimensions.
- [type SupportedUnits](../AppleNewsFormat/supportedunits.md)
  The units of measurement Apple News Format supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/preparing-image-video-audio-music-and-arkit-assets)*