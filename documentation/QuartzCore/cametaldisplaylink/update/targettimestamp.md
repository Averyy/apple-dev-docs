# targetTimestamp

**Framework**: Core Animation  
**Kind**: property

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

#### Discussion

Your app needs to call the [`drawable`](cametaldisplaylink/update/drawable.md) instance’s [`present()`](https://developer.apple.com/documentation/Metal/MTLDrawable/present()) method before the deadline. GPU rendering can continue after this time, based on [`preferredFrameLatency`](cametaldisplaylink/preferredframelatency.md). For more information on timing your app’s rendering, see [`metalDisplayLink(_:needsUpdate:)`](cametaldisplaylinkdelegate/metaldisplaylink(_:needsupdate:).md).

## See Also

- [var drawable: any CAMetalDrawable](cametaldisplaylink/update/drawable.md)
  The Metal drawable your app uses to render the next frame.
- [var drawable: any CAMetalDrawable](cametaldisplaylink/update/drawable.md)
  The Metal drawable your app uses to render the next frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/update/targettimestamp)*