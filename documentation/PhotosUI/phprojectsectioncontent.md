# PHProjectSectionContent

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

An object containing section elements and layout information for a single level of curation.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class PHProjectSectionContent
```

```objc
@interface PHProjectSectionContent : NSObject
```

## Overview

A section content object contains suggested layout information for every element at a specific level of curation within a [`PHProjectSection`](./phprojectsection.md). A single section can provide multiple content objects, but only one is used at a time, depending on the level of curation and the amount of content detail.

## Topics

### Determining Content Properties
- [var elements: [PHProjectElement]](./phprojectsectioncontent/elements.md)
  An array of asset, text, or journal entry elements contained in the content.
- [var numberOfColumns: Int](./phprojectsectioncontent/numberofcolumns.md)
  The number of columns if section content is displayed in a grid layout.
- [var aspectRatio: Double](./phprojectsectioncontent/aspectratio.md)
  The aspect ratio of the full content layout, defined as width over height.
- [var cloudAssetIdentifiers: [PHCloudIdentifier]](./phprojectsectioncontent/cloudassetidentifiers.md)
  An array containing all cloud asset identifiers referenced in the content.
- [var backgroundColor: NSColor?](./phprojectsectioncontent/backgroundcolor.md)
  The background color of the section content when created from an Apple Print Product.
### Initializers
- [init?(coder: NSCoder)](./phprojectsectioncontent/init%28coder%29.md)

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Determining Section Contents
- [var title: String](./phprojectsection/title.md)
  The optional section title.
- [var sectionContents: [PHProjectSectionContent]](./phprojectsection/sectioncontents.md)
  An array containing PHProjectionSessionContent objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectsectioncontent)*