# UIImage.Configuration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIImageConfiguration : NSObject
```

#### Overview

Images may contain multiple variants to account for environmental factors, such as whether the interface is light or dark. The image configuration object lets you override the current environment and render an image with specific attributes. For example, you might want to render a specific version of your image to your interface.

[`UIImage.Configuration`](./configuration-swift.class.md) objects are immutable and you don’t create them directly. Instead, get an existing image configuration object from a [`UITraitCollection`](../uitraitcollection.md) or [`UIImage`](../uiimage.md) object. To add attributes to your configuration object, use the [`applying(_:)`](./configuration-swift.class/applying%28_%29.md) method to create a new object that merges the existing object’s values with new values you supply. Assign the new object to the [`preferredSymbolConfiguration`](../uiimageview/preferredsymbolconfiguration.md) property of the [`UIImageView`](../uiimageview.md) object you use to display the image. If you draw the image directly, use the [`withConfiguration(_:)`](./withconfiguration%28_%29.md) method to create a new image that contains the new attributes.

## Topics

### Modifying a configuration object
- [func applying(UIImage.Configuration?) -> Self](./configuration-swift.class/applying%28_%29.md)
  Returns a configuration object that applies the specified configuration values on top of the current object’s values.
- [func withTraitCollection(UITraitCollection?) -> Self](./configuration-swift.class/withtraitcollection%28_%29.md)
  Returns a new configuration object that merges the current traits with the traits from the specified trait collection.
### Getting the configuration traits
- [var traitCollection: UITraitCollection?](./configuration-swift.class/traitcollection.md)
  The traits associated with the image configuration.
### Initializers
- [init?(coder: NSCoder)](./configuration-swift.class/init%28coder%29.md)
- [convenience init(locale: Locale?)](./configuration-swift.class/init%28locale%29.md)
- [convenience init(traitCollection: UITraitCollection?)](./configuration-swift.class/init%28traitcollection%29.md)
### Instance Properties
- [var locale: Locale?](./configuration-swift.class/locale.md)
### Instance Methods
- [func withLocale(Locale?) -> Self](./configuration-swift.class/withlocale%28_%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [UIImage.SymbolConfiguration](./symbolconfiguration-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Representations
- [class UIImage](../uiimage.md)
  An object that manages image data in your app.
- [UIImage.SymbolConfiguration](./symbolconfiguration-swift.class.md)
  An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/configuration-swift.class)*