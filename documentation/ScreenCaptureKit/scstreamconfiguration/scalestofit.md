# scalesToFit

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to scale the output to fit the configured width and height.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var scalesToFit: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL scalesToFit;
```

#### Discussion

The system uses this value during independent window capture.

## See Also

### Specifying dimensions
- [var width: Int](./width.md)
  The width of the output.
- [var height: Int](./height.md)
  The height of the output.
- [var sourceRect: CGRect](./sourcerect.md)
  A rectangle that specifies the source area to capture.
- [var destinationRect: CGRect](./destinationrect.md)
  A rectangle that specifies a destination into which to write the output.
- [var preservesAspectRatio: Bool](./preservesaspectratio.md)
  A Boolean value that determines if the stream preserves aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/scalestofit)*