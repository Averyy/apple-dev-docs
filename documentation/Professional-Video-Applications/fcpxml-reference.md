# FCPXML Reference

**Framework**: Professional-Video-Applications

Create documents that describe the data your app or workflow extension exchanges with Final Cut Pro.

#### Overview

Use FCPXML to describe the media, metadata, and other items users send and receive between your app and Final Cut Pro.

FCPXML uses a basic XML document structure and specially defined elements, to describe the media assets, projects, and metadata users send to Final Cut Pro, and the rendered media, timeline sequences, editing decisions, and other data your app receives from Final Cut Pro.

This reference guide provides information about using FCPXML, including:

- Document structure
- Elements
- Resources

> **Note**:  FCPXML 1.9 requires Final Cut Pro 10.4.9 or later. It describes certain, but not all, aspects of projects and events useful for other applications. But, it’s not a substitute for a native Final Cut Pro project and event data organized in a library bundle.

The following resources are helpful as you work with the FCPXML format:

- [Final Cut Pro User Guide](https://support.apple.com/guide/final-cut-pro/welcome/mac)
- [Final Cut Pro Resources](https://www.apple.com/final-cut-pro/resources/)
- [Extensible Markup Language (XML) 1.0](https://www.xml.com/axml/testaxml.htm) specification

## Topics

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
- [import-options](./import-options.md)
  Contain options that describe how to import events and projects into Final Cut Pro.
### Media Elements and Effects
- [Story Elements](./story-elements.md)
  Describe Final Cut Pro events and project data and their associated effects.
### Shared Resources and Reference Elements
- [asset](./asset.md)
  Define file-based media managed in a Final Cut Pro library.
- [media](./media.md)
  Describe a compound clip or a multi-camera media definition.
- [format](./format.md)
  Reference a video-format definition.
- [effect](./effect.md)
  Reference visual, audio, or custom effects.
- [locator](./locator.md)
  Describe a URL-based resource.
- [object-tracker](./object-tracker.md)
  Describe a tracked object such as a face or other moving object in a video clip.
- [tracking-shape](./tracking-shape.md)
  Define a shape that the object-tracker uses to match the movement of an object.
### Clips and Project Collections
- [Describing Final Cut Pro Items in FCPXML](./describing-final-cut-pro-items-in-fcpxml.md)
  Describe clips, projects, and other items in FCPXML to exchange data with Final Cut Pro.
- [keyword-collection](./keyword-collection.md)
  Group clips and projects based on matching keywords.
- [smart-collection](./smart-collection.md)
  Describe smart collection filters that group clips and projects that match the criteria.
- [collection-folder](./collection-folder.md)
  Contain keyword and smart collections.
### Media Metadata
- [Associating Ratings, Keywords, Markers, and Metadata with Media](./associating-ratings-keywords-markers-and-metadata-with-media.md)
  Organize and annotate the media and projects your users send to and receive from Final Cut Pro.
- [Metadata](./metadata.md)
  Describe metadata about media that is of interest to other applications.
- [Metadata Keys and Sources](./metadata-keys-and-sources.md)
  Define metadata keys that identify each metadata item and its sources.
### Document Type Definition
- [Document Type Definition](./document-type-definition.md)
  Document Type Definition (DTD) for the latest Final Cut Pro XML interchange format.

## See Also

### XML Data Exchange
- [Content and Metadata Exchanges with Final Cut Pro](./content-and-metadata-exchanges-with-final-cut-pro.md)
  Send media assets and timeline sequences to Final Cut Pro for editing, and receive rendered media and editing decisions in your app.
- [Workflow Extensions](./workflow-extensions.md)
  Integrate your app’s workflow within the Final Cut Pro interface to streamline data exchange.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/fcpxml-reference)*