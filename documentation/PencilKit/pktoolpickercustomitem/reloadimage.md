# reloadImage()

**Framework**: PencilKit  
**Kind**: method

Requests a new image for the custom tool item from the image provider.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
func reloadImage()
```

#### Discussion

Calling this method requests a new image for the custom tool item from the [`imageProvider`](pktoolpickercustomitem/configuration-swift.struct/imageprovider.md) of the [`configuration`](pktoolpickercustomitem/configuration-v7e5.md).

The system automatically calls this method when PencilKit attributes like [`color`](pktoolpickercustomitem/color.md) or [`width`](pktoolpickercustomitem/width.md) change. You can call this method when you need to generate a new image for the custom tool item that’s different from the current image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickercustomitem/reloadimage())*