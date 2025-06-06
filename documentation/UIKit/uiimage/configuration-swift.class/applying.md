# applying(_:)

**Framework**: UIKit  
**Kind**: method

Returns a configuration object that applies the specified configuration values on top of the current object’s values.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func applying(_ otherConfiguration: UIImage.Configuration?) -> Self
```

## Mentions

- [Configuring and displaying symbol images in your UI](configuring-and-displaying-symbol-images-in-your-ui.md)

#### Return Value

A configuration object with the specified image configuration attributes and merged traits.

#### Discussion

This method merges the traits from `otherConfiguration` with the current object’s trait collection, giving precedence to traits in `otherConfiguration` unless the trait is unspecified. For image-specific traits, this method replaces the current image attributes with the attributes in `otherConfiguration`.

## Parameters

- `otherConfiguration`: The configuration attributes to apply over the current attributes. Values in this object take precedence over values in the image’s current configuration object.

## See Also

- [func withTraitCollection(UITraitCollection?) -> Self](uiimage/configuration-swift.class/withtraitcollection(_:).md)
  Returns a new configuration object that merges the current traits with the traits from the specified trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/configuration-swift.class/applying(_:))*