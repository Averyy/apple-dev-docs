# digest

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A 64-bit digest that uniquely describes the contents of the input to a processor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var digest: UInt64 { get }
```

```objc
@property (nonatomic, readonly) uint64_t digest;
```

#### Discussion

This digest will change if the graph of the input changes in any way.

## See Also

### Instance Properties
- [var roiTileCount: Int](./roitilecount.md)
  This property tells a tiled-input processor how many input tiles will be processed.
- [var roiTileIndex: Int](./roitileindex.md)
  This property tells a tiled-input processor which input tile index is being processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/digest)*