# UIImage.Configuration

**Framework**: UIKit  
**Kind**: class

A configuration object that contains the traits that the system uses when selecting the current image variant.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class Configuration
```

#### Overview

Images may contain multiple variants to account for environmental factors, such as whether the interface is light or dark. The image configuration object lets you override the current environment and render an image with specific attributes. For example, you might want to render a specific version of your image to your interface.

[`UIImage.Configuration`](uiimage/configuration-swift.class.md) objects are immutable and you don’t create them directly. Instead, get an existing image configuration object from a [`UITraitCollection`](uitraitcollection.md) or [`UIImage`](uiimage.md) object. To add attributes to your configuration object, use the [`applying(_:)`](uiimage/configuration-swift.class/applying(_:).md) method to create a new object that merges the existing object’s values with new values you supply. Assign the new object to the [`preferredSymbolConfiguration`](uiimageview/preferredsymbolconfiguration.md) property of the [`UIImageView`](uiimageview.md) object you use to display the image. If you draw the image directly, use the [`withConfiguration(_:)`](uiimage/withconfiguration(_:).md) method to create a new image that contains the new attributes.

## Topics

### Modifying a configuration object
- [func applying(UIImage.Configuration?) -> Self](uiimage/configuration-swift.class/applying(_:).md)
  Returns a configuration object that applies the specified configuration values on top of the current object’s values.
- [func withTraitCollection(UITraitCollection?) -> Self](uiimage/configuration-swift.class/withtraitcollection(_:).md)
  Returns a new configuration object that merges the current traits with the traits from the specified trait collection.
### Getting the configuration traits
- [var traitCollection: UITraitCollection?](uiimage/configuration-swift.class/traitcollection.md)
  The traits associated with the image configuration.
### Initializers
- [convenience init(locale: Locale?)](uiimage/configuration-swift.class/init(locale:).md)
- [convenience init(traitCollection: UITraitCollection?)](uiimage/configuration-swift.class/init(traitcollection:).md)
### Instance Properties
- [var locale: Locale?](uiimage/configuration-swift.class/locale.md)
### Instance Methods
- [func withLocale(Locale?) -> Self](uiimage/configuration-swift.class/withlocale(_:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIImage.SymbolConfiguration](uiimage/symbolconfiguration-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UIImage](uiimage.md)
  An object that manages image data in your app.
- [UIImage.SymbolConfiguration](uiimage/symbolconfiguration-swift.class.md)
  An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/configuration-swift.class)*