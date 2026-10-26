# Content and Metadata Exchanges with Final Cut Pro

**Framework**: Professional-Video-Applications

Send media assets and timeline sequences to Final Cut Pro for editing, and receive rendered media and editing decisions in your app.

#### Overview

Help your users exchange data between Final Cut Pro and your app, and avoid unwieldy manual processes. With FCPXML representing media, metadata, and Final Cut Pro items, your users can send data from your app to Final Cut Pro for editing, or receive rendered media (movies) and editing decisions from Final Cut Pro projects in your app for further processing.

![Illustration showing a two-way flow of data between Final Cut Pro and your app, with the Final Cut Pro icon and X M L (to indicate FCPXML) in the middle.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3878511@2x.png)

FCPXML is a specialized format that uses XML elements to describe the data going between your app and Final Cut Pro. With FCPXML simplifying the data exchange, app users can:

- Send large quantities of media from an asset management tool to be edited in Final Cut Pro.
- Send media clips—annotated with ratings, keywords, and metadata—and let Final Cut Pro organize the incoming media.
- Receive rendered media and editing decisions for a project—including lists of media used—from Final Cut Pro for further processing, such as color grading and correction.
- Receive rendered media (movies) in an app to finish and package for delivery, playout, or archiving.
- Record an audio/video stream and start editing the media in Final Cut Pro while the file is still being recorded.

## Topics

### Data Sent from Your App to Final Cut Pro
- [Sending Media and Metadata to Final Cut Pro](./sending-media-and-metadata-to-final-cut-pro.md)
  Send media assets, timeline sequences, and metadata from your app to Final Cut Pro.
- [Supporting Drag and Drop for Data Sent to Final Cut Pro](./supporting-drag-and-drop-for-data-sent-to-final-cut-pro.md)
  Add drag and drop support so your users can drag media assets and timeline sequences from your app directly into Final Cut Pro.
- [Sending Data Programmatically to Final Cut Pro](./sending-data-programmatically-to-final-cut-pro.md)
  Manage and streamline the sending of batches of media assets and timeline sequences from your app using Apple events.
- [Sending media to Final Cut Pro as it’s recorded](./sending-media-to-final-cut-pro-as-it-s-recorded.md)
  Designate media as a growing file to make it available to users while it’s still being recorded.
### Data Received in Your App from Final Cut Pro
- [Supporting Drag and Drop to Receive Final Cut Pro Data](./supporting-drag-and-drop-to-receive-final-cut-pro-data.md)
  Add drag and drop support in your app to give users an intuitive way to receive clips, projects, and other items from Final Cut Pro.
- [Receiving Media and Data Through a Custom Share Destination](./receiving-media-and-data-through-a-custom-share-destination.md)
  Receive rendered media (movies), editing descriptions for project timelines, library archives, and FCPXML for other Final Cut Pro items in your app.

## See Also

### XML Data Exchange
- [Workflow Extensions](./workflow-extensions.md)
  Integrate your app’s workflow within the Final Cut Pro interface to streamline data exchange.
- [FCPXML Reference](./fcpxml-reference.md)
  Create documents that describe the data your app or workflow extension exchanges with Final Cut Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/content-and-metadata-exchanges-with-final-cut-pro)*