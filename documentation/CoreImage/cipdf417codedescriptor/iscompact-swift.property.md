# isCompact

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

A boolean value telling if the PDF417 code is compact.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isCompact: Bool { get }
```

```objc
@property (readonly) BOOL isCompact;
```

## Discussion

Compact PDF417 symbols have abbreviated right-side guard bars.

## See Also

### Examining a Descriptor
- [var errorCorrectedPayload: Data](./errorcorrectedpayload-swift.property.md)
  The error-corrected payload containing the data encoded in the PDF417 code symbol.
- [var rowCount: Int](./rowcount-swift.property.md)
  The number of rows in the PDF417 code symbol.
- [var columnCount: Int](./columncount-swift.property.md)
  The number of columns in the PDF417 code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor/iscompact-swift.property)*