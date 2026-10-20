# metalDisplayLink(_:needsUpdate:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A method the system calls to notify your app when it plans to update the display.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func metalDisplayLink(_ link: CAMetalDisplayLink, needsUpdate update: CAMetalDisplayLink.Update)
```

```objc
- (void) metalDisplayLink:(CAMetalDisplayLink *) link needsUpdate:(CAMetalDisplayLinkUpdate *) update;
```

#### Discussion

In this method’s implementation, perform your app’s rendering on the [`layer`](../cametaldrawable/layer.md) or [`texture`](../cametaldrawable/texture.md) of the `update` instance’s [`drawable`](../cametaldisplaylink/update/drawable.md) property. Before calling [`present()`](../../Metal/mtldrawable/present%28%29.md), encode all your Metal commands to the `link` parameter’s [`MTLDevice`](../../Metal/mtldevice.md). The GPU has additional time to complete running your commands before the frame displays on screen, determined by the value of the `link` parameter’s [`preferredFrameLatency`](../cametaldisplaylink/preferredframelatency.md) property.

> ⚠️ **Warning**:  Using alternative methods to [`present()`](../../Metal/mtldrawable/present%28%29.md) that target the presentation for a specific time cause an assert when used with a [`CAMetalDisplayLink`](../cametaldisplaylink.md).

## Parameters

- `link`: A Metal display link instance the system notifies.
- `update`: An update instance that contains the time the system intends to update the display, a [`CAMetalDrawable`](../cametaldrawable.md) instance, and a deadline to call its [`present()`](../../Metal/mtldrawable/present%28%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldisplaylinkdelegate/metaldisplaylink(_:needsupdate:))*