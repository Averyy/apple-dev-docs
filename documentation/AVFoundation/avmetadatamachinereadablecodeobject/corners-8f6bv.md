# corners

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The points defining the (x, 	y) locations of the corners.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 9.0+

## Declaration

```objc
@property (readonly) NSArray<NSDictionary *> * corners;
```

#### Discussion

The value of this property is an array of `CFDictionary` objects, each of which has been created from a `CGPoint` struct using the [`dictionaryRepresentation`](../../CoreFoundation/cgpoint/dictionaryrepresentation.md) function, representing the coordinates of the corners of the object with respect to the image in which it resides.

If the metadata originates from video, the points may be expressed as scalar values from `0` to `1`.

The points in the corners differ from the bounds rectangle in that bounds is axis aligned to orientation of the captured image, and the values of the corners reside within the bounds rectangle.

The points are arranged in counterclockwise order (clockwise if the code or image is mirrored), starting with the top left of the code in its canonical orientation.

## See Also

### Getting machine-readable code values
- [var descriptor: CIBarcodeDescriptor?](./descriptor.md)
  A barcode description for use in Core Image.
- [var stringValue: String?](./stringvalue.md)
  Returns the error-corrected data decoded into a human-readable string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatamachinereadablecodeobject/corners-8f6bv)*