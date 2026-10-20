# message

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The message to encode in the PDF417 barcode.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var message: Data { get set }
```

```objc
@property (nonatomic, retain) NSData * message;
```

## See Also

### Instance Properties
- [var alwaysSpecifyCompaction: Float](./alwaysspecifycompaction.md)
  A Boolean value specifying whether to force compaction style.
- [var compactStyle: Float](./compactstyle.md)
  A Boolean value specifying whether to force compact style Aztec code.
- [var compactionMode: Float](./compactionmode.md)
  The compaction mode of the generated barcode.
- [var correctionLevel: Float](./correctionlevel.md)
  The correction level ratio of the generated barcode.
- [var dataColumns: Float](./datacolumns.md)
  The number of data columns in the generated barcode.
- [var maxHeight: Float](./maxheight.md)
  The maximum height, in pixels, of the generated barcode.
- [var maxWidth: Float](./maxwidth.md)
  The maximum width, in pixels, of the generated barcode.
- [var minHeight: Float](./minheight.md)
  The minimum height, in pixels, of the generated barcode.
- [var minWidth: Float](./minwidth.md)
  The minimum width, in pixels, of the generated barcode.
- [var preferredAspectRatio: Float](./preferredaspectratio.md)
  The preferred aspect ratio of the generated barcode.
- [var rows: Float](./rows.md)
  The number of rows in the generated barcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipdf417barcodegenerator/message)*