# buffer

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The buffer that holds the geometry data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var buffer: (any MTLBuffer)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MTLBuffer> buffer;
```

## See Also

### Specifying the keyframe data
- [var offset: Int](./offset.md)
  The offset, in bytes, to the keyframe data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlmotionkeyframedata/buffer)*