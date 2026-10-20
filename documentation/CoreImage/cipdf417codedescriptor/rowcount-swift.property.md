# rowCount

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The number of rows in the PDF417 code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var rowCount: Int { get }
```

```objc
@property (readonly) NSInteger rowCount;
```

#### Discussion

Valid row count values are from 3 to 90.

## See Also

### Examining a Descriptor
- [var errorCorrectedPayload: Data](./errorcorrectedpayload-swift.property.md)
  The error-corrected payload containing the data encoded in the PDF417 code symbol.
- [var isCompact: Bool](./iscompact-swift.property.md)
  A boolean value telling if the PDF417 code is compact.
- [var columnCount: Int](./columncount-swift.property.md)
  The number of columns in the PDF417 code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor/rowcount-swift.property)*