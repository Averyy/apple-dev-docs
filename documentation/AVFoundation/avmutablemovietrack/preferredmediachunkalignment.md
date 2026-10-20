# preferredMediaChunkAlignment

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The boundary for media chunk alignment for file types that support media chunk alignment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var preferredMediaChunkAlignment: Int { get set }
```

```objc
@property (nonatomic) NSInteger preferredMediaChunkAlignment;
```

#### Discussion

The default value is `0`, which indicates to use no padding should to achieve chunk alignment. Setting a negative chunk alignment value causes an error.

## See Also

### Accessing media chunks
- [var preferredMediaChunkDuration: CMTime](./preferredmediachunkduration.md)
  The maximum duration to use for each chunk of sample data written to the file for file types that support media chunk duration.
- [var preferredMediaChunkSize: Int](./preferredmediachunksize.md)
  The maximum size to use for each chunk of sample data written to the file for file types that support media chunk duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/preferredmediachunkalignment)*