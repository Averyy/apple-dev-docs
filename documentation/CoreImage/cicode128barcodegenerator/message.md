# message

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The message to encode in the Code 128 barcode.

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
- [var barcodeHeight: Float](./barcodeheight.md)
  The height, in pixels, of the generated barcode.
- [var quietSpace: Float](./quietspace.md)
  The number of empty white pixels that should surround the barcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicode128barcodegenerator/message)*