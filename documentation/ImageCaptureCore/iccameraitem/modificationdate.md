# modificationDate

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The item’s modification date, usually the same as its `EXIF` modification date.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var modificationDate: Date? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDate * modificationDate;
```

## See Also

### Determining an Item’s Change Dates
- [var creationDate: Date?](./creationdate.md)
  The item’s creation date, usually the same as its `EXIF` creation date.
- [var wasAddedAfterContentCatalogCompleted: Bool](./wasaddedaftercontentcatalogcompleted.md)
  A Boolean value indicating whether the item was captured on the camera after the camera’s content had been fully enumerated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/modificationdate)*