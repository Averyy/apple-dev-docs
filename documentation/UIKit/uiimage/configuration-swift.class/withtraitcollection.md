# withTraitCollection(_:)

**Framework**: UIKit  
**Kind**: method

Returns a new configuration object that merges the current traits with the traits from the specified trait collection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func withTraitCollection(_ traitCollection: UITraitCollection?) -> Self
```

#### Return Value

A configuration object with the merged set of traits.

#### Discussion

Use this method to augment or change the traits in the current configuration object. This method prefers the values from `traitCollection` over the values in the current configuration object. If the value of the trait is unspecified in both collections, it remains unspecified in the new collection.

## Parameters

- `traitCollection`: The traits to insert or apply to the configuration object. The trait values in this parameter take precedence over the ones in the current configuration object, unless you left the trait with an unspecified value.

## See Also

- [func applying(UIImage.Configuration?) -> Self](uiimage/configuration-swift.class/applying(_:).md)
  Returns a configuration object that applies the specified configuration values on top of the current object’s values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/configuration-swift.class/withtraitcollection(_:))*