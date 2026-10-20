# outputs

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The outputs from which you read media data.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var outputs: [AVAssetReaderOutput] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVAssetReaderOutput *> * outputs;
```

#### Discussion

The array contains the concrete instances of [`AVAssetReaderOutput`](../avassetreaderoutput.md) that you associate with the reader.

## See Also

### Managing outputs
- [func canAdd(AVAssetReaderOutput) -> Bool](./canadd%28_%29.md)
  Determines whether you can add the output to the asset reader.
- [func add(AVAssetReaderOutput)](./add%28_%29.md)
  Adds an output to the reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/outputs)*