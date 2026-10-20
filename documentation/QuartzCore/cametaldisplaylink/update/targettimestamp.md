# targetTimestamp

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

A deadline that indicates when your app needs to finish rendering to the drawable.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var targetTimestamp: CFTimeInterval { get }
```

```objc
@property (nonatomic, readonly) CFTimeInterval targetTimestamp;
```

#### Discussion

Your app needs to call the [`drawable`](./drawable.md) instance’s [`present()`](../../../Metal/mtldrawable/present%28%29.md) method before the deadline. GPU rendering can continue after this time, based on [`preferredFrameLatency`](../preferredframelatency.md). For more information on timing your app’s rendering, see [`metalDisplayLink(_:needsUpdate:)`](../../cametaldisplaylinkdelegate/metaldisplaylink%28_,needsupdate%29.md).

## See Also

### Drawing the Next Frame
- [var drawable: any CAMetalDrawable](./drawable.md)
  The Metal drawable your app uses to render the next frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/update/targettimestamp)*