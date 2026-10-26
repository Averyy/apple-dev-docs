# PHProject

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A representation of a Photos app project extension.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class PHProject
```

```objc
@interface PHProject : PHAssetCollection
```

#### Overview

This class represents the project when extended from macOS Photos. Projects can have the following types:

- Book
- Calendar
- Card
- Prints
- Slideshow
- Wall decor

Users create projects by selecting one or more assets, right-clicking the selection, and grouping the assets, much like an album collection. Your app treats the project as a separate entity, represented as a [`PHProject`](./phproject.md).

## Topics

### Project Extension Properties
- [var hasProjectPreview: Bool](./phproject/hasprojectpreview.md)
  A property that indicates whether a project preview was previously set.
- [var projectExtensionData: Data](./phproject/projectextensiondata.md)
  Data associated with the project extension.

## Relationships

### Inherits From
- [PHAssetCollection](./phassetcollection.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Classes
- [class PHProjectChangeRequest](./phprojectchangerequest.md)
  A request to change asset data in a Photos project extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phproject)*