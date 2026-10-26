# sectionContents

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

An array containing PHProjectionSessionContent objects.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var sectionContents: [PHProjectSectionContent] { get }
```

```objc
@property (nonatomic, readonly) NSArray<PHProjectSectionContent *> * sectionContents;
```

#### Discussion

The content is ordered by number of elements, from fewest to most. Projects should present only one level of content to the user at a time, because assets are reused within individual content objects.

## See Also

### Determining Section Contents
- [var title: String](./title.md)
  The optional section title.
- [class PHProjectSectionContent](../phprojectsectioncontent.md)
  An object containing section elements and layout information for a single level of curation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectsection/sectioncontents)*