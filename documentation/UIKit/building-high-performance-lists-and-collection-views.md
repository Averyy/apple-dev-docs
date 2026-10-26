# Building high-performance lists and collection views

**Framework**: UIKit  
**Role**: Sample Code  
**Download**: [BuildingHighPerformanceListsAndCollectionViews.zip](https://docs-assets.developer.apple.com/published/7f5574e912c4/BuildingHighPerformanceListsAndCollectionViews.zip)

Improve the performance of lists and collections in your app with prefetching and image preparation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- Xcode 13.0+

#### Overview

> **Note**: This sample code project is associated with WWDC21 session [10252: Make Blazing Fast Lists and Collection Views](https://developer.apple.com/wwdc21/10252/).

## See Also

### Loading and caching images
- [Providing images for different appearances](./providing-images-for-different-appearances.md)
  Supply image resources appropriate for light and dark appearances and for high-contrast environments.
- [Configuring and displaying symbol images in your UI](./configuring-and-displaying-symbol-images-in-your-ui.md)
  Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [Creating custom symbols](../TechnologyOverviews/custom-sf-symbols.md)
  Design a symbol image with the same behavior as system-provided symbols.
- [init?(named: String, in: Bundle?, compatibleWith: UITraitCollection?)](./uiimage/init%28named,in,compatiblewith%29.md)
  Creates an image object using the named image asset that’s compatible with the specified trait collection.
- [init?(named: String, in: Bundle?, with: UIImage.Configuration?)](./uiimage/init%28named,in,with%29.md)
  Creates an image by using the named image asset that’s compatible with the configuration you specify.
- [convenience init?(named: String, in: Bundle?, variableValue: Double, configuration: UIImage.Configuration?)](./uiimage/init%28named,in,variablevalue,configuration%29.md)
  Creates an image by using the name, configuration, and variable value you specify.
- [init?(named: String)](./uiimage/init%28named%29.md)
  Creates an image object from the specified named asset.
- [convenience init(imageLiteralResourceName: String)](./uiimage/init%28imageliteralresourcename%29.md)
  Returns the image object for the specified resource.
- [init?(systemName: String, withConfiguration: UIImage.Configuration?)](./uiimage/init%28systemname,withconfiguration%29.md)
  Creates an image object that contains a system symbol image with the specified configuration.
- [convenience init?(systemName: String, variableValue: Double, configuration: UIImage.Configuration?)](./uiimage/init%28systemname,variablevalue,configuration%29.md)
  Creates an image object that contains a system symbol image with the configuration and variable value you specify.
- [init?(systemName: String, compatibleWith: UITraitCollection?)](./uiimage/init%28systemname,compatiblewith%29.md)
  Creates an image object that contains a system symbol image appropriate for the specified traits.
- [init?(systemName: String)](./uiimage/init%28systemname%29.md)
  Creates an image object that contains a system symbol image.
- [convenience init(resource: ImageResource)](./uiimage/init%28resource%29.md)
- [+ imageNamed:inBundle:variableValue:withConfiguration:](./uiimage/imagenamed_inbundle_variablevalue_withconfiguration_.md)
  Creates an image by using the name, configuration, and variable value you specify.
- [+ systemImageNamed:variableValue:withConfiguration:](./uiimage/systemimagenamed_variablevalue_withconfiguration_.md)
  Creates an image object that contains a system symbol image with the configuration and variable value you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/building-high-performance-lists-and-collection-views)*