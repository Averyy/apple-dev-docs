# compactStyle

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean that specifies whether to force a compact style Aztec code.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var compactStyle: Float { get set }
```

```objc
@property (nonatomic) float compactStyle;
```

## Discussion

Set to `nil` for automatic.

## See Also

### Instance Properties
- [var correctionLevel: Float](./correctionlevel.md)
  The Aztec error correction, a value from 5 to 95.
- [var layers: Float](./layers.md)
  The number of Aztec layers, a value from 1 to 32.
- [var message: Data](./message.md)
  The message to encode in the Aztec barcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciazteccodegenerator/compactstyle)*