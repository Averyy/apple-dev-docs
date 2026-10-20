# preservesAspectRatio

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines if the stream preserves aspect ratio.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
var preservesAspectRatio: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL preservesAspectRatio;
```

#### Discussion

The default value is `true`.

## See Also

### Specifying dimensions
- [var width: Int](./width.md)
  The width of the output.
- [var height: Int](./height.md)
  The height of the output.
- [var scalesToFit: Bool](./scalestofit.md)
  A Boolean value that indicates whether to scale the output to fit the configured width and height.
- [var sourceRect: CGRect](./sourcerect.md)
  A rectangle that specifies the source area to capture.
- [var destinationRect: CGRect](./destinationrect.md)
  A rectangle that specifies a destination into which to write the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/preservesaspectratio)*