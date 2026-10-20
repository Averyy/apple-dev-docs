# autoAdjustmentFilters()

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Returns all possible automatically selected and configured filters for adjusting the image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func autoAdjustmentFilters() -> [CIFilter]
```

```objc
- (NSArray<CIFilter *> *) autoAdjustmentFilters;
```

#### Return Value

An array of [`CIFilter`](../cifilter-swift.class.md) instances preconfigured for correcting deficiencies in the supplied image.

## See Also

### Getting Autoadjustment Filters
- [func autoAdjustmentFilters(options: [CIImageAutoAdjustmentOption : Any]?) -> [CIFilter]](./autoadjustmentfilters%28options%29.md)
  Returns a subset of automatically selected and configured filters for adjusting the image.
- [Autoadjustment Keys](../autoadjustment-keys.md)
  Constants used as keys in the options dictionary for the [`autoAdjustmentFilters(options:)`](./autoadjustmentfilters%28options%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/autoadjustmentfilters())*