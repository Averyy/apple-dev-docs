# imageDataAvailable

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether a contact has a profile picture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var imageDataAvailable: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, readonly) BOOL imageDataAvailable;
```

*macOS*

```objc
@property (atomic, readonly) BOOL imageDataAvailable;
```

## See Also

### Getting Contact Images
- [var imageData: Data?](./imagedata.md)
  The profile picture of a contact.
- [var thumbnailImageData: Data?](./thumbnailimagedata.md)
  The thumbnail version of the contact’s profile picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/imagedataavailable)*