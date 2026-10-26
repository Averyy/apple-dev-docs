# init(named:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an image object from the specified named asset.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(named name: String)
```

```objc
+ (UIImage *) imageNamed:(NSString *) name;
```

## Mentions

- [Configuring and displaying symbol images in your UI](../configuring-and-displaying-symbol-images-in-your-ui.md)

#### Return Value

An object containing an unconfigured version of the image, or `nil` if the method could not find the specified image.

#### Discussion

When searching the asset catalog, this method prefers an asset containing a symbol image over an asset with the same name containing a bitmap image. Because the system supports symbol images iOS 13 or later, you may include both types of assets in the same asset catalog. In iOS 12 or earlier, the system automatically chooses the bitmap image.

You can’t use this method to load system symbol images; use the [`init(systemName:)`](./init%28systemname%29.md) method instead.

This method checks the system caches for an image object with the name you specify, and returns the variant of that image that’s best suited for the main screen. If a matching image object isn’t in the cache, this method creates the image from an available asset catalog or loads the image from disk.

The system may purge cached image data at any time to free up memory. Purging occurs only for unused images that are in the cache.

In iOS 9 and later, this method is thread safe.

##### Special Considerations

If you intend to display an image only once and don’t want it added to the system’s cache, create it using the [`imageWithContentsOfFile:`](./imagewithcontentsoffile_.md) method instead. Keeping single-use images out of the system image cache can potentially improve the memory use characteristics of your app.

## Parameters

- `name`: The name of the image asset or file.

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
- [convenience init(imageLiteralResourceName: String)](./init%28imageliteralresourcename%29.md)
  Returns the image object for the specified resource.
- [init?(systemName: String, withConfiguration: UIImage.Configuration?)](./init%28systemname,withconfiguration%29.md)
  Creates an image object that contains a system symbol image with the specified configuration.
- [convenience init?(systemName: String, variableValue: Double, configuration: UIImage.Configuration?)](./init%28systemname,variablevalue,configuration%29.md)
  Creates an image object that contains a system symbol image with the configuration and variable value you specify.
- [init?(systemName: String, compatibleWith: UITraitCollection?)](./init%28systemname,compatiblewith%29.md)
  Creates an image object that contains a system symbol image appropriate for the specified traits.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/init(named:))*