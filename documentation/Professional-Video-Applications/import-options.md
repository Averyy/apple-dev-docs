# import-options

**Framework**: Professional-Video-Applications  
**Role**: Article

Contain options that describe how to import events and projects into Final Cut Pro.

## Overview

The `import-options` element can contain zero or more `option` elements. The `option` element describes options for importing events and projects into Final Cut Pro through the key-value pair in the attributes listed below.

| Attributes | Description |
| --- | --- |
| `key` | A string that identifies one of the following import options: ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `copy assets`: Copy or link assets referenced in the imported XML. Valid values are `1` (copy) and `0` (link).   ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `library location`: Specifies the location (URL) of the library to which to add the event or project. If the specified URL represents a directory, Final Cut Pro uses the default library name. If no library exists at the location specified in the XML, Final Cut Pro creates a new library. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `suppress warnings`: Suppress or show warnings generated during import. Valid values are `≥1` (suppress) and `0` (show)  ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) `base url`: A URL to resolve a relative URL given in the XML as the value of the `src` attribute of a `resources` element. |
| `value` | The value for the import option. |

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
- [project](./project.md)
  Represent a project timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/import-options)*