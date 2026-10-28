# PHProjectRegionOfInterest

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

A representation of a region of interest in a photo asset.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class PHProjectRegionOfInterest
```

```objc
@interface PHProjectRegionOfInterest : NSObject
```

## Overview

A region of interest defines a rectangular portion of a photo corresponding to a face. Use a region of interest to determine where to focus, zoom, or crop your image in your project extension; for example, you can customize your slideshow’s transitions based on each photo’s highest-quality region of interest, as shown in [Creating a Slideshow Project Extension for Photos](../PhotoKit/creating-a-slideshow-project-extension-for-photos.md).

## Topics

### Identifying Regions of Interest
- [PHProjectRegionOfInterest.Identifier](./phprojectregionofinterest/identifier-swift.struct.md)
  A descriptor identifying a region of interest.
### Determining Region Properties
- [var rect: CGRect](./phprojectregionofinterest/rect.md)
  The rectangle representing the region’s location.
- [var identifier: PHProjectRegionOfInterest.Identifier](./phprojectregionofinterest/identifier-swift.property.md)
  The region’s unique identifier.
- [var weight: Double](./phprojectregionofinterest/weight.md)
  The face region’s weight.
- [var quality: Double](./phprojectregionofinterest/quality.md)
  The region’s quality.
### Initializers
- [init?(coder: NSCoder)](./phprojectregionofinterest/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### macOS Photos project extensions
- [Creating a Slideshow Project Extension for Photos](../PhotoKit/creating-a-slideshow-project-extension-for-photos.md)
  Augment the macOS Photos app with extensions that support project creation.
- [class PHProject](../Photos/phproject.md)
  A representation of a Photos app project extension.
- [class PHProjectInfo](./phprojectinfo.md)
  Information about the project extension.
- [class PHProjectExtensionContext](./phprojectextensioncontext.md)
  An object that provides Photos project extensions with access to the underlying project, as well as to the user’s photo library for editing.
- [class PHProjectElement](./phprojectelement.md)
  The superclass for all element objects.
- [class PHProjectSection](./phprojectsection.md)
  A collection of content representing curated asset and text elements.
- [class PHProjectChangeRequest](../Photos/phprojectchangerequest.md)
  A request to change asset data in a Photos project extension.
- [protocol PHProjectExtensionController](./phprojectextensioncontroller.md)
  A protocol defining the life cycle and supported types of project extensions.
- [struct PHProjectCategory](./phprojectcategory.md)
  A representation of Photos project extension categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectregionofinterest)*