# width

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

The width of the output.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+

## Declaration

```swift
var width: Int { get set }
```

```objc
@property (nonatomic, assign) size_t width;
```

## See Also

### Specifying dimensions
- [var height: Int](./height.md)
  The height of the output.
- [var scalesToFit: Bool](./scalestofit.md)
  A Boolean value that indicates whether to scale the output to fit the configured width and height.
- [var sourceRect: CGRect](./sourcerect.md)
  A rectangle that specifies the source area to capture.
- [var destinationRect: CGRect](./destinationrect.md)
  A rectangle that specifies a destination into which to write the output.
- [var preservesAspectRatio: Bool](./preservesaspectratio.md)
  A Boolean value that determines if the stream preserves aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/width)*