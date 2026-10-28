# FCPXML Bundle Reference

**Framework**: Professional-Video-Applications  
**Role**: Article

Keep an FCPXML document and any files it references together in a bundle.

## Overview

When a user shares data from Final Cut Pro with your app, Final Cut Pro exports the required files and packages them together in a bundle. The bundle format makes it easy for an app to keep FCPXML and referenced files together. FCPXML Bundles have a `.fcpxmld` extension.

![Illustration that shows a data flow from a Final Cut Pro icon on the right to an X  M L bundle in the middle, and then to your app on the left. ](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3878510@2x.png)

The simplest FCPXML bundle contains an `Info.fcpxml` file at the root level of the bundle. This file contains a structured description of the exported data. You use the file to retrieve information about the exported data and locate other relevant files in the bundle. The format of the `Info.fcpxml` file is defined in the [Document Type Definition](./document-type-definition.md) (DTD).

If your app already supports `.fcpxml` files, add support for the new bundle format to ensure full compatibility with exports from Final Cut Pro.

> **Note**:  FCPXML bundle support is available for Document Type Definition (DTD) 1.10 and later.

## See Also

### Document Structure and Root Elements
- [Creating FCPXML Documents](./creating-fcpxml-documents.md)
  Describe media assets, editing decisions, metadata, and other items in FCPXML so users can send and receive data between your app and Final Cut Pro.
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
- [import-options](./import-options.md)
  Contain options that describe how to import events and projects into Final Cut Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/fcpxml-bundle-reference)*