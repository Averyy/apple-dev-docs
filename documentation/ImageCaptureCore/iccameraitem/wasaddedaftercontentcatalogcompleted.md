# wasAddedAfterContentCatalogCompleted

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the item was captured on the camera after the camera’s content had been fully enumerated.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var wasAddedAfterContentCatalogCompleted: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=wasAddedAfterContentCatalogCompleted) BOOL addedAfterContentCatalogCompleted;
```

#### Discussion

This value does not apply to files added as a result of adding a new store to the camera.

## See Also

### Determining an Item’s Change Dates
- [var creationDate: Date?](./creationdate.md)
  The item’s creation date, usually the same as its `EXIF` creation date.
- [var modificationDate: Date?](./modificationdate.md)
  The item’s modification date, usually the same as its `EXIF` modification date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/wasaddedaftercontentcatalogcompleted)*