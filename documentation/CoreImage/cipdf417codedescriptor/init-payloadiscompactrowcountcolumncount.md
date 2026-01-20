# init(payload:isCompact:rowCount:columnCount:)

**Framework**: Core Image  
**Kind**: init

Initializes an PDF417 code descriptor for the given payload and parameters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init?(payload errorCorrectedPayload: Data, isCompact: Bool, rowCount: Int, columnCount: Int)
```

#### Return Value

 An initialized [`CIPDF417CodeDescriptor`](cipdf417codedescriptor.md) instance or `nil` if the parameters are invalid

## Parameters

- `errorCorrectedPayload`: The data to encode in the PDF417 code symbol.
- `isCompact`: A Boolean indicating whether or not the PDF417 code is compact.
- `rowCount`: The number of rows in the PDF417 code, from 3 to 90.
- `columnCount`: The number of columns in the Aztec code, from 1 to 30.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor/init(payload:iscompact:rowcount:columncount:))*