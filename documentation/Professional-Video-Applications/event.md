# event

**Framework**: Professional-Video-Applications  
**Role**: Article

Represent a single event in a library.

#### Overview

An event may contain clips as story elements and projects, along with keyword collections and smart collections. The `keyword-collection` and `smart-collection` elements organize clips by keywords and other matching criteria listed under the [Smart Collection Match Elements](./smart-collection.md#Smart-Collection-Match-Elements).

An event element has the following attributes:

| Attribute | Description |
| --- | --- |
| `name` | Specifies name of the event. |

An event element has the following subelements:

| Subelements | Description |
| --- | --- |
| `clip` | Represents a basic unit of editing. |
| `audition` | Contains one active story element followed by alternative story elements in the audition container. |
| `mc-clip` | References a multicam media. |
| `ref-clip` | References a compound clip media. |
| `sync-clip` | Contains a clip with its contained and anchored items synchronized. |
| `asset-clip` | References a single media asset. |
| `project` | Represents a project timeline. |
| `keyword-collection` | Groups clips and projects based on matching keywords. |
| `smart-collection` | Describes smart collection filters that group clips and projects that match the criteria. |
| `collection-folder` | Contains keyword and smart collections. |

## See Also

### Document Structure and Root Elements
- [Creating FCPXML Documents](./creating-fcpxml-documents.md)
  Describe media assets, editing decisions, metadata, and other items in FCPXML so users can send and receive data between your app and Final Cut Pro.
- [FCPXML Bundle Reference](./fcpxml-bundle-reference.md)
  Keep an FCPXML document and any files it references together in a bundle.
- [Importing FCPXML Data](./importing-fcpxml-data.md)
  Import data from Final Cut Pro to your app by using FCPXML.
- [fcpxml](./fcpxml.md)
  Contain top-level elements in a document.
- [resources](./resources.md)
  Contain shared resources on which events and projects depend.
- [library](./library.md)
  Contain events, clips, projects, and smart collections.
- [project](./project.md)
  Represent a project timeline.
- [import-options](./import-options.md)
  Contain options that describe how to import events and projects into Final Cut Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/event)*