# thumbnailImageData

**Framework**: Contacts  
**Kind**: property

The thumbnail version of the contact’s profile picture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var thumbnailImageData: Data? { get }
```

#### Discussion

The [`thumbnailImageData`](cncontact/thumbnailimagedata.md) property is derived from the [`imageData`](cncontact/imagedata.md) property, including cropping information from vCards or edits from contact viewing. It is recommended that you fetch this property only when you need to access its value, such as when you need to display the contact’s profile thumbnail picture.

## See Also

- [var imageData: Data?](cncontact/imagedata.md)
  The profile picture of a contact.
- [var imageDataAvailable: Bool](cncontact/imagedataavailable.md)
  A Boolean indicating whether a contact has a profile picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/thumbnailimagedata)*