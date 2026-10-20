# message

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The message to encode in the Aztec barcode.

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
- [var compactStyle: Float](./compactstyle.md)
  A Boolean that specifies whether to force a compact style Aztec code.
- [var correctionLevel: Float](./correctionlevel.md)
  The Aztec error correction, a value from 5 to 95.
- [var layers: Float](./layers.md)
  The number of Aztec layers, a value from 1 to 32.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciazteccodegenerator/message)*