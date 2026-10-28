# thumbnailImageData

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSData * thumbnailImageData;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSData * thumbnailImageData;
```

## Discussion

The [`thumbnailImageData`](./thumbnailimagedata.md) property is derived from the [`imageData`](./imagedata.md) property, including cropping information from vCards or edits from contact viewing. It is recommended that you fetch this property only when you need to access its value, such as when you need to display the contact’s profile thumbnail picture.

## See Also

### Getting Contact Images
- [var imageData: Data?](./imagedata.md)
  The profile picture of a contact.
- [var imageDataAvailable: Bool](./imagedataavailable.md)
  A Boolean indicating whether a contact has a profile picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/thumbnailimagedata)*