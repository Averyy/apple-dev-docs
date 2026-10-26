# init(systemName:compatibleWith:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an image object that contains a system symbol image appropriate for the specified traits.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init?(systemName name: String, compatibleWith traitCollection: UITraitCollection?)
```

```objc
+ (UIImage *) systemImageNamed:(NSString *) name compatibleWithTraitCollection:(UITraitCollection *) traitCollection;
```

## Mentions

- [Configuring and displaying symbol images in your UI](../configuring-and-displaying-symbol-images-in-your-ui.md)

#### Return Value

The object containing the image variant that matches the specified trait collection, or `nil` if no suitable image was found.

#### Discussion

Use this method to retrieve system-defined symbol images. To retrieve a custom symbol image you store in an asset catalog, use the [`init(named:in:compatibleWith:)`](./init%28named,in,compatiblewith%29.md) method instead.

This method checks the system caches for an image with the name you specify and returns the variant of that image that’s best suited for traits.

If a matching image object isn’t in the cache, this method creates the image from the system symbol image. The system may purge cached image data at any time to free up memory. Purging occurs only for unused images that are in the cache.

To look up the names of system symbol images, download the SF Symbols app from [Apple Design Resources](https://developer.apple.com/design/resources/).

## Parameters

- `name`: The name of the system symbol image.
- `traitCollection`: The traits associated with the intended environment for the image. Use this parameter to ensure that the correct variant of the image is loaded. If you specify `nil`, this method uses the traits associated with the main screen.

## See Also

### Loading and caching images
- [Providing images for different appearances](../providing-images-for-different-appearances.md)
  Supply image resources appropriate for light and dark appearances and for high-contrast environments.
- [Configuring and displaying symbol images in your UI](../configuring-and-displaying-symbol-images-in-your-ui.md)
  Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [Creating custom symbols](../../TechnologyOverviews/custom-sf-symbols.md)
  Design a symbol image with the same behavior as system-provided symbols.
- [init?(named: String, in: Bundle?, compatibleWith: UITraitCollection?)](./init%28named,in,compatiblewith%29.md)
  Creates an image object using the named image asset that’s compatible with the specified trait collection.
- [init?(named: String, in: Bundle?, with: UIImage.Configuration?)](./init%28named,in,with%29.md)
  Creates an image by using the named image asset that’s compatible with the configuration you specify.
- [convenience init?(named: String, in: Bundle?, variableValue: Double, configuration: UIImage.Configuration?)](./init%28named,in,variablevalue,configuration%29.md)
  Creates an image by using the name, configuration, and variable value you specify.
- [init?(named: String)](./init%28named%29.md)
  Creates an image object from the specified named asset.
- [convenience init(imageLiteralResourceName: String)](./init%28imageliteralresourcename%29.md)
  Returns the image object for the specified resource.
- [init?(systemName: String, withConfiguration: UIImage.Configuration?)](./init%28systemname,withconfiguration%29.md)
  Creates an image object that contains a system symbol image with the specified configuration.
- [convenience init?(systemName: String, variableValue: Double, configuration: UIImage.Configuration?)](./init%28systemname,variablevalue,configuration%29.md)
  Creates an image object that contains a system symbol image with the configuration and variable value you specify.
- [init?(systemName: String)](./init%28systemname%29.md)
  Creates an image object that contains a system symbol image.
- [convenience init(resource: ImageResource)](./init%28resource%29.md)
- [Building high-performance lists and collection views](../building-high-performance-lists-and-collection-views.md)
  Improve the performance of lists and collections in your app with prefetching and image preparation.
- [+ imageNamed:inBundle:variableValue:withConfiguration:](./imagenamed_inbundle_variablevalue_withconfiguration_.md)
  Creates an image by using the name, configuration, and variable value you specify.
- [+ systemImageNamed:variableValue:withConfiguration:](./systemimagenamed_variablevalue_withconfiguration_.md)
  Creates an image object that contains a system symbol image with the configuration and variable value you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/init(systemname:compatiblewith:))*