# default()

**Framework**: UIKit  
**Kind**: method

Returns a format that represents the highest fidelity that the current device supports.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func `default`() -> Self
```

#### Return Value

An initialized format.

#### Discussion

The returned format object always represents the device’s highest fidelity, regardless of the actual fidelity currently employed by the device. A graphics renderer uses this method to create a format at initialization time if you use an initializer that does not have a format argument.

This property doesn’t always return a format that’s optimized for the current configuration of the main screen. If you’re rendering content for immediate display, it’s recommended that you use [`preferred()`](uigraphicsrendererformat/preferred().md) instead of this property.

## See Also

- [class func preferred() -> Self](uigraphicsrendererformat/preferred.md)
  Returns the most suitable format for the main screen’s current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrendererformat/default())*