# imageData

**Framework**: Contacts  
**Kind**: property

The profile picture of a contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var imageData: Data? { get }
```

#### Discussion

It is recommended that you fetch this property only when you need to access its value, such as when you need to display the contact’s profile picture.

## See Also

- [var thumbnailImageData: Data?](cncontact/thumbnailimagedata.md)
  The thumbnail version of the contact’s profile picture.
- [var imageDataAvailable: Bool](cncontact/imagedataavailable.md)
  A Boolean indicating whether a contact has a profile picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/imagedata)*