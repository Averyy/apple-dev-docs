# withTraitCollection(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (instancetype) configurationWithTraitCollection:(UITraitCollection *) traitCollection;
```

#### Return Value

A configuration object with the merged set of traits.

#### Discussion

Use this method to augment or change the traits in the current configuration object. This method prefers the values from `traitCollection` over the values in the current configuration object. If the value of the trait is unspecified in both collections, it remains unspecified in the new collection.

## Parameters

- `traitCollection`: The traits to insert or apply to the configuration object. The trait values in this parameter take precedence over the ones in the current configuration object, unless you left the trait with an unspecified value.

## See Also

### Modifying a configuration object
- [func applying(UIImage.Configuration?) -> Self](./applying%28_%29.md)
  Returns a configuration object that applies the specified configuration values on top of the current object’s values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/configuration-swift.class/withtraitcollection(_:))*