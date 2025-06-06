# init(named:in:variableValue:configuration:)

**Framework**: UIKit  
**Kind**: init

Creates an image by using the name, configuration, and variable value you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
convenience init?(named name: String, in bundle: Bundle? = nil, variableValue: Double, configuration: UIImage.Configuration? = nil)
```

#### Return Value

An object that contains the image variant that matches the configuration data; otherwise, `nil` if the system didn’t find a suitable image.

#### Discussion

When searching the asset catalog, this method prefers an asset containing a symbol image over an asset with the same name containing a bitmap image. Because the system supports symbol images in iOS 13 or later, you may include both types of assets in the same asset catalog. In iOS 12 or earlier, the system automatically chooses the bitmap image.

You can’t use this method to load system symbol images; use the [`init(systemName:variableValue:configuration:)`](uiimage/init(systemname:variablevalue:configuration:).md) method instead.

This method checks the system caches for an image object with the name you specify, and returns the variant of that image that best matches the trait collection you specify. If a matching image object isn’t in the cache, this method creates the image from an available asset catalog or loads the image from disk.

The system may purge cached image data at any time to free up memory. Purging occurs only for unused images that are in the cache.

## Parameters

- `name`: The name of the image asset or file.
- `bundle`: The bundle that contains the image file or asset catalog.
- `variableValue`: The value the system uses to customize the image content, between   and  .
- `configuration`: The image configuration the system applies to the image.

## See Also

- [Providing images for different appearances](providing-images-for-different-appearances.md)
  Supply image resources appropriate for light and dark appearances and for high-contrast environments.
- [Configuring and displaying symbol images in your UI](configuring-and-displaying-symbol-images-in-your-ui.md)
  Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [Creating custom symbol images for your app](creating-custom-symbol-images-for-your-app.md)
  Create, organize, and annotate symbol images using SF Symbols.
- [init?(named: String, in: Bundle?, compatibleWith: UITraitCollection?)](uiimage/init(named:in:compatiblewith:).md)
  Creates an image object using the named image asset that’s compatible with the specified trait collection.
- [init?(named: String, in: Bundle?, with: UIImage.Configuration?)](uiimage/init(named:in:with:).md)
  Creates an image by using the named image asset that’s compatible with the configuration you specify.
- [init?(named: String)](uiimage/init(named:).md)
  Creates an image object from the specified named asset.
- [convenience init(imageLiteralResourceName: String)](uiimage/init(imageliteralresourcename:).md)
  Returns the image object for the specified resource.
- [init?(systemName: String, withConfiguration: UIImage.Configuration?)](uiimage/init(systemname:withconfiguration:).md)
  Creates an image object that contains a system symbol image with the specified configuration.
- [convenience init?(systemName: String, variableValue: Double, configuration: UIImage.Configuration?)](uiimage/init(systemname:variablevalue:configuration:).md)
  Creates an image object that contains a system symbol image with the configuration and variable value you specify.
- [init?(systemName: String, compatibleWith: UITraitCollection?)](uiimage/init(systemname:compatiblewith:).md)
  Creates an image object that contains a system symbol image appropriate for the specified traits.
- [init?(systemName: String)](uiimage/init(systemname:).md)
  Creates an image object that contains a system symbol image.
- [convenience init(resource: ImageResource)](uiimage/init(resource:).md)
- [Building high-performance lists and collection views](building-high-performance-lists-and-collection-views.md)
  Improve the performance of lists and collections in your app with prefetching and image preparation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/init(named:in:variablevalue:configuration:))*