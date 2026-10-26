# media-rep

**Framework**: Professional-Video-Applications

References a media representation, that is either the original or a proxy media managed by Final Cut Pro.

#### Overview

A media that Final Cut Pro manages in its library can have a proxy media representation, in addition to the original media representation. Use the `media-rep` element to describe a media representation, as a child element of the `asset` element.

> **Note**:  The `media-rep` element is new in FCPXML 1.9. Use the `asset` element with the `src` attribute to specify the original media file for FCPXML 1.8 or earlier.

##### Media-Rep Element Attributes

| Attribute | Description |
| --- | --- |
| `kind` | The kind of media representation. Either “`original-media`” or “`proxy-media`”. |
| `src` | A string that specifies the location of the media file as a URL. For details about the URL, see the [Location of Media Files](./media-rep.md#Location-of-Media-Files) section. |
| `sig` | The unique identifier of a media representation, assigned by Final Cut Pro. |
| `suggestedFilename` | The filename string to use when Final Cut Pro manages the media representation file. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) Under specific circumstances, the URL for a media file may not contain the filename to use when Final Cut Pro manages the media file. Use the `suggestedFilename` attribute to specify the filename to use when Final Cut Pro manages the file.  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) The expected value of this attribute is the basename of the file without the file extension. Even when the value contains a dot, Final Cut Pro interprets the substring after the dot as part of the file’s basename and not as a file extension. Final cut pro uses the extension derived from the source URL for the filename extension. An exception to that is when the substring after the dot exactly matches the extension derived from the source URL, where Final Cut Pro uses the attribute value as the file basename and the extension. |

##### Location of Media Files

Describe the location of media files by using a URL as the value of the `src` attribute. The URL can be one of the following:

- An absolute URL conforming to RFC 2396
- A relative URL based on the location of the FCPXML document itself, for example: `./Media/MyMovie.mov`

An absolute URL  can be either a file URL with the “`file:`” scheme tag, for example:

```swift
file:///path/to/MyMovieFile.mov
```

`    `

Or, a remote URL with the “`http:`” or “`https:`” scheme tag, for  example:

```swift
 http://myserver.mydomain.net/path/to/MyMovieFile.mov
```

When a media representation has its file on a remote location, Final Cut Pro initially imports the media as offline and then schedules a download of the media as a background task. When the download completes, the respective media comes online.

> **Note**:  Support for remote URL is new in FCPXML v1.9. As of Final Cut Pro 10.4.9, it doesn’t have support for user authentication. The recommendation is to authenticate the user prior to the XML import and include the authentication token in the remote URL.

Final Cut Pro expects the media file to exist at the location specified by the URL. If the file exists, Final Cut Pro reads the content of the media file to get the information about the media. If the file is missing, Final Cut Pro still imports the media representation and marks it offline. Red frames indicate that the media is missing when the media representation you choose is offline. If you know the file exists elsewhere, you can relink to that file. For more information on relinking media files, see [Relink clips to media files](https://support.apple.com/guide/final-cut-pro/relink-clips-to-media-files-ver26f5c8c9/mac).

When Final Cut Pro manages the media file in the library or at its media location, Final Cut Pro uses the file name and extenion from the URL you provide as the `src` attribute’s value. While Final Cut Pro itself offers ways to manage media in those locations, some users may still choose to manage the media files externally. Use file names that make sense to the user. Specify a file name to use when Final Cut Pro manages the media file through the `suggestedFilename` attribute.

## Topics

### Bookmark Element
- [bookmark](./bookmark.md)
  Represents security-scoped bookmark data in a base64-encoded string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/media-rep)*