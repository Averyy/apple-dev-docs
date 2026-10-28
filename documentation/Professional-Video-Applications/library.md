# library

**Framework**: Professional-Video-Applications  
**Role**: Article

Contain events, clips, projects, and smart collections.

## Overview

The library element has the following attributes:

| Attributes | Description |
| --- | --- |
| `location` | Specifies the URL of a library on export; Final Cut Pro ignores this option during the XML import. To specify the target library for the XML import, see the `library location` key listed under the [import-options](./import-options.md) attributes. |
| `colorProcessing` | Specifies whether the library supports `standard`, `wide`, or `wide-hdr` color gamut. The default is `standard`. |

The library element has the following subelements:

| Subelements | Description |
| --- | --- |
| `smart-collection` | Describes smart collection filters that group clips and projects that match the criteria. |
| `event` | Represents a single event in a library. |

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
- [event](./event.md)
  Represent a single event in a library.
- [project](./project.md)
  Represent a project timeline.
- [import-options](./import-options.md)
  Contain options that describe how to import events and projects into Final Cut Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/library)*