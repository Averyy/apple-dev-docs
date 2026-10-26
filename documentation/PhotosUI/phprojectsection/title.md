# title

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The optional section title.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var title: String { get }
```

```objc
@property (nonatomic, readonly) NSString * title;
```

#### Discussion

By default, the title should relate to the content, like the Moment’s name or the geographical location where content was captured. The title can also be an empty string.

## See Also

### Determining Section Contents
- [var sectionContents: [PHProjectSectionContent]](./sectioncontents.md)
  An array containing PHProjectionSessionContent objects.
- [class PHProjectSectionContent](../phprojectsectioncontent.md)
  An object containing section elements and layout information for a single level of curation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectsection/title)*