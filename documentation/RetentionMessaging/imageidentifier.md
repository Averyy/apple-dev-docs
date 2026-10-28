# imageIdentifier

**Framework**: Retention Messaging API  
**Kind**: typealias  
**Role**: Type

A unique identifier for an image that you provide when you upload the image.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```
uuid imageIdentifier
```

## Discussion

You create a UUID to identify an image when you call [`Upload Image`](./upload-image.md). Use this identifier to refer to the same image throughout the API.

## See Also

### Images
- [type imageState](./imagestate.md)
  The approval state of an image.
- [type imageSize](./imagesize.md)
  The size of an image.
- [type altText](./alttext.md)
  The alternative text for a corresponding image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/imageidentifier)*