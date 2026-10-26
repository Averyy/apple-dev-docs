# fcpxml

**Framework**: Professional-Video-Applications  
**Role**: Article

Contain top-level elements in a document.

#### Overview

The root element in an FCPXML document is `fcpxml`, which can contain the following elements:

- A `resources` element, that contains descriptions of media assets and other resources.
- An optional `import-options` element, that controls how Final Cut Pro imports the FCPXML document.
- One of the following optional elements that describe how to organize and use media assets:  a `library` element that contains a list of `event` elements; a series of `event` elements that contain story elements and `project` elements; or a combination of story elements and `<project>` elements.

> **Note**:  Starting in FCPXML 1.9, the elements that describe how to organize and use media assets are optional. The only required element in the `fcpxml` root element is the `resources` element.

## See Also

### Document Structure and Root Elements
- [Creating FCPXML Documents](./creating-fcpxml-documents.md)
  Describe media assets, editing decisions, metadata, and other items in FCPXML so users can send and receive data between your app and Final Cut Pro.
- [FCPXML Bundle Reference](./fcpxml-bundle-reference.md)
  Keep an FCPXML document and any files it references together in a bundle.
- [Importing FCPXML Data](./importing-fcpxml-data.md)
  Import data from Final Cut Pro to your app by using FCPXML.
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

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/fcpxml)*