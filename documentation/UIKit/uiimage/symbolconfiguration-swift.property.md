# symbolConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The configuration details for a symbol image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var symbolConfiguration: UIImage.SymbolConfiguration? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) UIImageSymbolConfiguration * symbolConfiguration;
```

#### Discussion

Use this property to access the traits and rendering attributes associated with the symbol image. The system uses the specified details to determine which variant of the image to load and draw and how to render it, falling back on the current environment as needed for any unspecified values. For symbol images, the default value of this property is a symbol image configuration object with unspecified values. For other image types, the default value of this property is `nil`.

You can’t modify this property directly, but you can use the [`withConfiguration(_:)`](./withconfiguration%28_%29.md) when you want to create a new image object with a specific set of traits.

If the image is a symbol image, this property always contains a [`UIImage.SymbolConfiguration`](./symbolconfiguration-swift.class.md) object.

## See Also

### Getting the image configuration
- [var configuration: UIImage.Configuration?](./configuration-swift.property.md)
  The configuration details for the image.
- [var traitCollection: UITraitCollection](./traitcollection.md)
  The trait collection that describes the current variant of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.property)*