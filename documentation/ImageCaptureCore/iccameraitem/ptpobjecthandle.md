# ptpObjectHandle

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The item’s `PTP` object handle value, if the camera uses the `PTP` protocol.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var ptpObjectHandle: UInt32 { get }
```

```objc
@property (nonatomic, readonly) unsigned int ptpObjectHandle;
```

#### Discussion

The value of this property is set to `0` if the camera does not use PTP protocol.

## See Also

### Inspecting an Item’s Name and Type
- [var uti: String?](./uti.md)
  The item’s uniform type identifier (UTI) string.
- [var name: String?](./name.md)
  The item’s name.
- [var isRaw: Bool](./israw.md)
  A Boolean value indicating whether the item is a raw image file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/ptpobjecthandle)*