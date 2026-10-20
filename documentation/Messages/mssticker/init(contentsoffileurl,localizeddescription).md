# init(contentsOfFileURL:localizedDescription:)

**Framework**: Messages  
**Kind**: init

Initializes a sticker with the contents of the URL and the localized description.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(contentsOfFileURL fileURL: URL, localizedDescription: String) throws
```

#### Return Value

A newly initialized sticker object, or `nil` if an error occurs.

## Parameters

- `fileURL`: A URL for the image displayed by this sticker. This URL must refer to a file saved on the device. The file must be a PNG, APNG, GIF, or JPEG, and must be less than 500 KB. For the best results, the image should not be smaller than 100 x 100 points or larger than 206 x 206 points. Always provide @3x images (300 x 300 pixels to 618 x 618 pixels). The system generates the @2x and @1x versions by downscaling the @3x images at runtime.
- `localizedDescription`: A succinct, localized description of the sticker. The description is limited to 150 Unicode characters. The system uses this string as an accessibility description of the sticker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/mssticker/init(contentsoffileurl:localizeddescription:))*