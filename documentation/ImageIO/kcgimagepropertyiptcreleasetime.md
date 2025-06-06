# kCGImagePropertyIPTCReleaseTime

**Framework**: Image I/O  
**Kind**: var

The earliest time at which you can use the image, in the form HHMMSS.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCGImagePropertyIPTCReleaseTime: CFString
```

#### Discussion

This time is valid on the release date, which is available in the [`kCGImagePropertyIPTCReleaseDate`](kcgimagepropertyiptcreleasedate.md) property.

## See Also

- [let kCGImagePropertyIPTCReleaseDate: CFString](kcgimagepropertyiptcreleasedate.md)
  The earliest day on which you can use the image, in the form CCYYMMDD.
- [let kCGImagePropertyIPTCExpirationDate: CFString](kcgimagepropertyiptcexpirationdate.md)
  The latest date you can use the image, in the form CCYYMMDD.
- [let kCGImagePropertyIPTCExpirationTime: CFString](kcgimagepropertyiptcexpirationtime.md)
  The latest time on the expiration date you can use the image, in the form HHMMSS.
- [let kCGImagePropertyIPTCSpecialInstructions: CFString](kcgimagepropertyiptcspecialinstructions.md)
  Special instructions about the use of the image.
- [let kCGImagePropertyIPTCActionAdvised: CFString](kcgimagepropertyiptcactionadvised.md)
  The advised action.
- [let kCGImagePropertyIPTCReferenceService: CFString](kcgimagepropertyiptcreferenceservice.md)
  The reference service.
- [let kCGImagePropertyIPTCReferenceDate: CFString](kcgimagepropertyiptcreferencedate.md)
  The reference date.
- [let kCGImagePropertyIPTCReferenceNumber: CFString](kcgimagepropertyiptcreferencenumber.md)
  The reference number.
- [let kCGImagePropertyIPTCDateCreated: CFString](kcgimagepropertyiptcdatecreated.md)
  The creation date.
- [let kCGImagePropertyIPTCTimeCreated: CFString](kcgimagepropertyiptctimecreated.md)
  The creation time.
- [let kCGImagePropertyIPTCDigitalCreationDate: CFString](kcgimagepropertyiptcdigitalcreationdate.md)
  The digital creation date.
- [let kCGImagePropertyIPTCDigitalCreationTime: CFString](kcgimagepropertyiptcdigitalcreationtime.md)
  The digital creation time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcreleasetime)*