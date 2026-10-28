# Sending Media and Metadata to Final Cut Pro

**Framework**: Professional-Video-Applications  
**Role**: Article

Send media assets, timeline sequences, and metadata from your app to Final Cut Pro.

## Overview

Make content in your app available to Final Cut Pro, whether it’s a timeline sequence from an asset-management app or raw footage from video capture software. With FCPXML, your users have options for getting data from your app to Final Cut Pro for editing. Your app can send media assets as Final Cut Pro clips, events, projects, and other items. An FCPXML document can also contain markers, ratings, keywords, keyword collections, and metadata.

![Illustration showing the types of items users can send from your ap to Final Cut Pro using F C P X M L.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3878512@2x.png)

### Choose How to Send Data to Final Cut Pro

Send your users’ data to Final Cut Pro based on how much and what kind of data they have to send, how often they need to send it, and how they approach their tasks. For example:

- If your users often send small batches of individual clips to different areas of Final Cut Pro and go back and forth frequently between your app and Final Cut Pro, set up drag and drop in your app to make sending media to Final Cut Pro more intuitive. See [Supporting Drag and Drop for Data Sent to Final Cut Pro](./supporting-drag-and-drop-for-data-sent-to-final-cut-pro.md).
- If your users have a lot of assets to edit, and their workflow has them send everything to Final Cut Pro before starting to edit, use Apple events to help them manage that workflow more efficiently. See [Sending Data Programmatically to Final Cut Pro](./sending-data-programmatically-to-final-cut-pro.md).
- If your users want to send media to Final Cut Pro for editing while they’re recording it, make sure your app designates the file as a *growing* file. You can then choose how to send the growing media file to Final Cut Pro. See [Sending media to Final Cut Pro as it’s recorded](./sending-media-to-final-cut-pro-as-it-s-recorded.md).

### Create an FCPXML Document

No matter how your app sends content to Final Cut Pro, it must create an FCPXML document to describe your users’ data. FCPXML—an XML-based language—describes the media, metadata, and timeline sequences (rough cuts as well as more-polished sequences) in terms that Final Cut Pro understands. Using FCPXML, your app can also take advantage of Final Cut Pro features, such as keywords, and use metadata to set up content for your users to edit. For more information, see [Creating FCPXML Documents](./creating-fcpxml-documents.md).

## See Also

### Data Sent from Your App to Final Cut Pro
- [Supporting Drag and Drop for Data Sent to Final Cut Pro](./supporting-drag-and-drop-for-data-sent-to-final-cut-pro.md)
  Add drag and drop support so your users can drag media assets and timeline sequences from your app directly into Final Cut Pro.
- [Sending Data Programmatically to Final Cut Pro](./sending-data-programmatically-to-final-cut-pro.md)
  Manage and streamline the sending of batches of media assets and timeline sequences from your app using Apple events.
- [Sending media to Final Cut Pro as it’s recorded](./sending-media-to-final-cut-pro-as-it-s-recorded.md)
  Designate media as a growing file to make it available to users while it’s still being recorded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/sending-media-and-metadata-to-final-cut-pro)*