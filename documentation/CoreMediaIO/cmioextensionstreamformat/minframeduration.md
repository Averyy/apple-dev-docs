# minFrameDuration

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

The minimum frame duration a stream supports.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var minFrameDuration: CMTime { get }
```

```objc
@property (atomic, readonly) CMTime minFrameDuration;
```

## See Also

### Configuring Frame Durations
- [var maxFrameDuration: CMTime](./maxframeduration.md)
  The maximum duration a stream supports.
- [var validFrameDurations: [CMTime]?](./validframedurations-707st.md)
  An array of frame durations the stream supports.
- [validFrameDurations](./validframedurations-4rbay.md)
  An array of frame durations the stream supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamformat/minframeduration)*