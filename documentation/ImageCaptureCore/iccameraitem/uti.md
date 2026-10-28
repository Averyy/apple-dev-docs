# uti

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The item’s uniform type identifier (UTI) string.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var uti: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * UTI;
```

## Discussion

The `UTI` options are `kUTTypeFolder`, `kUTTypeImage`, `kUTTypeMovie`, `kUTTypeAudio`, or `kUTTypeData`.

## See Also

### Inspecting an Item’s Name and Type
- [var name: String?](./name.md)
  The item’s name.
- [var ptpObjectHandle: UInt32](./ptpobjecthandle.md)
  The item’s `PTP` object handle value, if the camera uses the `PTP` protocol.
- [var isRaw: Bool](./israw.md)
  A Boolean value indicating whether the item is a raw image file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/uti)*