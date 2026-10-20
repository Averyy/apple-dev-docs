# metadata

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A collection of metadata to be written to the receiver’s output files.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var metadata: [AVMetadataItem] { get set }
```

```objc
@property (nonatomic, copy) NSArray<AVMetadataItem *> * metadata;
```

#### Discussion

The value of this property is an array of `AVMetadataItem` objects representing the collection of top-level metadata to be written in each output file. Only ID3 v2.2, v2.3, or v2.4 style metadata items are supported.

## See Also

### Configuring output
- [var audioSettings: [String : Any]?](./audiosettings.md)
  The settings used to decode or re-encode audio before it is output by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiofileoutput/metadata)*