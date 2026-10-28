# project

**Framework**: Professional-Video-Applications  
**Role**: Article

Represent a project timeline.

## Overview

A `project` element represents a timeline in a Final Cut Pro project.  A project sequence can also contain filters that apply effects to certain elements. For more information on how to apply effects to story elements, see Adjustment and Effects Elements.

A project element has the following attributes:

| Attribute | Description |
| --- | --- |
| `name` | Specifies the name of the project. |

A project element has the following subelements:

| Subelement | Description |
| --- | --- |
| `sequence` | Represents the clips that form a sequence in a Final Cut Pro project. |

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
- [event](./event.md)
  Represent a single event in a library.
- [import-options](./import-options.md)
  Contain options that describe how to import events and projects into Final Cut Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/project)*