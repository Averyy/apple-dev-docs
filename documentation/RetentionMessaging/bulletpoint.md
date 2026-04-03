# BulletPoint

**Framework**: Retention Messaging API  
**Kind**: dictionary

The text and its bullet-point image to include in a retention message’s bulleted list.

**Availability**:
- Retention Messaging API 1.4+

## Declaration

```swift
object BulletPoint
```

## Mentions

- [Retention Messaging API changelog](retention-messaging-changelog.md)

#### Overview

Use `BulletPoint` items when you set up a text-based message that contains bullet points. Each bullet point item consists of the following elements:

- An image to use as the bullet point. To use an image as a bullet point icon, upload the image with an [`imageSize`](imagesize.md) of `BULLET_POINT`. For more information, see [`Upload Image`](upload-image.md).
- The alternative text that describes the bullet point image.
- The text of the individual bullet point.

Provide an array of `BulletPoint` objects in the [`UploadMessageRequestBody`](uploadmessagerequestbody.md)  when you call [`Upload Message`](upload-message.md).

## Properties

- `altText` (altText) *(required)*: The alternative text you provide for the corresponding image of the bullet point.
- `imageIdentifier` (imageIdentifier) *(required)*: The identifier of the image to use as the bullet point.
- `text` (bulletPointText) *(required)*: The text of the individual bullet point.

## See Also

- [type messageIdentifier](messageidentifier.md)
  A unique identifier for a message, which you provide when you upload the message.
- [type messageState](messagestate.md)
  The approval state of the message.
- [type body](body.md)
  The body text you provide for a message.
- [type bulletPointText](bulletpointtext.md)
  The text you provide for an individual bullet-list item.
- [type header](header.md)
  The header text you provide that appears above the body text in a message.
- [type headerPosition](headerposition.md)
  The position where the header text appears in a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/bulletpoint)*