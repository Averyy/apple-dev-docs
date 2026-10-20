# defaultCaptureScope

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The capture scope to use when a capture is initiated in Xcode.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var defaultCaptureScope: (any MTLCaptureScope)? { get set }
```

```objc
@property (atomic, strong, readwrite, nullable) id<MTLCaptureScope> defaultCaptureScope;
```

#### Discussion

Use this property to specify a default capture scope for Xcode to use when the user presses the capture button. You can still long-press the button to select a different capture scope.

The default value is `nil.` When the value is `nil`, the capture scope is defined by drawable presentation boundaries; such as those created by calls to [`present(_:)`](../mtlcommandbuffer/present%28_%29.md) or [`present()`](../mtldrawable/present%28%29.md).

## See Also

### Creating a capture scope
- [func makeCaptureScope(device: any MTLDevice) -> any MTLCaptureScope](./makecapturescope%28device%29.md)
  Creates a capture scope for commands submitted to a specific device object.
- [func makeCaptureScope(commandQueue: any MTLCommandQueue) -> any MTLCaptureScope](./makecapturescope%28commandqueue%29-1rozd.md)
  Creates a capture scope for commands submitted to a specific command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturemanager/defaultcapturescope)*