# collection-folder

**Framework**: Professional-Video-Applications  
**Role**: Article

Contain keyword and smart collections.

#### Overview

Use a `collection-folder` element to describe a collection folder in an event. A `collection-folder` element contains a series of `keyword-collection` elements or `smart-collection` elements, and can also include other `collection-folder` elements. The following example represents a collection folder that contains a keyword collection and a smart collection:

```swift
<collection-folder name="MyCollection">
   <keyword-collection name="MyKeyword" />
   <smart-collection name="Compound Clips" match="all">
      <match-clip rule="is" type="compound" />
   </smart-collection>
</collection-folder>

```

## See Also

### Clips and Project Collections
- [Describing Final Cut Pro Items in FCPXML](./describing-final-cut-pro-items-in-fcpxml.md)
  Describe clips, projects, and other items in FCPXML to exchange data with Final Cut Pro.
- [keyword-collection](./keyword-collection.md)
  Group clips and projects based on matching keywords.
- [smart-collection](./smart-collection.md)
  Describe smart collection filters that group clips and projects that match the criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/collection-folder)*