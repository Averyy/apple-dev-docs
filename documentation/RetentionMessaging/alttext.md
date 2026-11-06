# altText

**Framework**: Retention Messaging API  
**Kind**: typealias  
**Role**: Type

The alternative text for a corresponding image.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```
string altText
```



**Maximum Length**: `150`

## Discussion

Provide the `altText` as a UTF-8-encoded string with a maximum length of 150 characters.

> **Note**: Use only allowed Unicode characters in the string. If it contains a disallowed character, [`Upload Message`](./upload-message.md) returns a [`BadRequestInvalidTextFieldError`](./badrequestinvalidtextfielderror.md).

## See Also

### Images
- [type imageIdentifier](./imageidentifier.md)
  A unique identifier for an image that you provide when you upload the image.
- [type imageState](./imagestate.md)
  The approval state of an image.
- [type imageSize](./imagesize.md)
  The size of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/alttext)*