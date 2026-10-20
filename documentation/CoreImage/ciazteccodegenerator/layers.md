# layers

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The number of Aztec layers, a value from 1 to 32.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var layers: Float { get set }
```

```objc
@property (nonatomic) float layers;
```

#### Discussion

Set to `nil` for automatic.

## See Also

### Instance Properties
- [var compactStyle: Float](./compactstyle.md)
  A Boolean that specifies whether to force a compact style Aztec code.
- [var correctionLevel: Float](./correctionlevel.md)
  The Aztec error correction, a value from 5 to 95.
- [var message: Data](./message.md)
  The message to encode in the Aztec barcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciazteccodegenerator/layers)*