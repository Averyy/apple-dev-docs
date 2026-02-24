# autoAdjustmentFilters(options:)

**Framework**: Core Image  
**Kind**: method

Returns a subset of automatically selected and configured filters for adjusting the image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func autoAdjustmentFilters(options: [CIImageAutoAdjustmentOption : Any]? = nil) -> [CIFilter]
```

#### Return Value

An array of [`CIFilter`](cifilter-swift.class.md) instances preconfigured for correcting deficiencies in the supplied image.

## Parameters

- `options`: You can control which filters are returned by supplying one or more of the keys described in [`Autoadjustment Keys`](autoadjustment-keys.md). The options dictionary can also contain a [`CIDetectorImageOrientation`](cidetectorimageorientation.md) key. Because some autoadjustment filters rely on face detection, you should specify an image orientation if you want to enable these filters for an image containing face whose orientation does not match that of the image.

## See Also

- [func autoAdjustmentFilters() -> [CIFilter]](ciimage/autoadjustmentfilters.md)
  Returns all possible automatically selected and configured filters for adjusting the image.
- [Autoadjustment Keys](autoadjustment-keys.md)
  Constants used as keys in the options dictionary for the [`autoAdjustmentFilters(options:)`](ciimage/autoadjustmentfilters(options:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/autoadjustmentfilters(options:))*