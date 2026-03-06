# Artwork

**Framework**: Apple Music API  
**Kind**: dictionary

An object that represents artwork.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Artwork
```

## Properties

- `bgColor` (string): The average background color of the image.
- `height` (number) *(required)*: The maximum height available for the image.
- `width` (number) *(required)*: The maximum width available for the image.
- `textColor1` (string): The primary text color used if the background color gets displayed.
- `textColor2` (string): The secondary text color used if the background color gets displayed.
- `textColor3` (string): The tertiary text color used if the background color gets displayed.
- `textColor4` (string): The final post-tertiary text color used if the background color gets displayed.
- `url` (string) *(required)*: The URL to request the image asset. `{w}x{h}`must precede image filename, as placeholders for the `width` and `height` values as described above. For example, `{w}x{h}bb.jpeg`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/artwork)*