# Sending media to Final Cut Pro as it’s recorded

**Framework**: Professional-Video-Applications  
**Role**: Article

Designate media as a growing file to make it available to users while it’s still being recorded.

## Overview

Your users may want to start using a media file in Final Cut Pro even while your app continues recording a video stream into the same file. Before recording begins, your app should designate the file as a *growing* file — a file that continues to have media added to it. How to make this designation depends on the file format being used for the recording. Final Cut Pro supports editing growing media files in both QuickTime Movie and Material eXchange Format (MXF) file formats.

After your app sends a growing file to Final Cut Pro, Final Cut Pro periodically checks the file’s modification date. If Final Cut Pro determines that the file has been modified, it reads the file again. Once a file has been designated as a growing file, your users can drag it to Final Cut Pro (if your app supports drag and drop functionality) or your app can use an Apple event to send the growing file to Final Cut Pro programmatically. See [Supporting Drag and Drop for Data Sent to Final Cut Pro](./supporting-drag-and-drop-for-data-sent-to-final-cut-pro.md) and [Sending Data Programmatically to Final Cut Pro](./sending-data-programmatically-to-final-cut-pro.md).

### Designate a QuickTime Movie as a Growing File

A QuickTime Movie normally uses a *consolidated* table of contents that allows random access to media. However, to edit a QuickTime Movie while recording it, the movie must be created using *movie fragments*, which uses a *distributed* table of contents for the file. A distributed table of contents lets Final Cut Pro access the media file while content is still being added.

To create a QuickTime Movie that lets your users work on the file as it’s being recorded:

- Record the movie using movie fragments. (See “Working with Fragmented Movies” in [`AVAsset`](../AVFoundation/avasset.md).)
- Set the `movieFragmentInterval` property in the `AVAssetWriter` class instance that’s writing the media file to a value between 15 and 30 seconds. Or, if you’re recording with a connected device, set that same property (`movieFragmentInterval`) in the `AVCaptureMovieFileOutput` class instance.

### Designate Media in an MXF File Format as a Growing File

If your app records media in an MXF file, and you want your users to be able to use the media in Final Cut Pro while recording, your app must specify the `duration` of the recorded file as `"unknown"`.

For information about recording in MXF format, see the ST 377-1:2011 - SMPTE Standard - Material Exchange Format (MXF) - File Format Specification.

## See Also

### Data Sent from Your App to Final Cut Pro
- [Sending Media and Metadata to Final Cut Pro](./sending-media-and-metadata-to-final-cut-pro.md)
  Send media assets, timeline sequences, and metadata from your app to Final Cut Pro.
- [Supporting Drag and Drop for Data Sent to Final Cut Pro](./supporting-drag-and-drop-for-data-sent-to-final-cut-pro.md)
  Add drag and drop support so your users can drag media assets and timeline sequences from your app directly into Final Cut Pro.
- [Sending Data Programmatically to Final Cut Pro](./sending-data-programmatically-to-final-cut-pro.md)
  Manage and streamline the sending of batches of media assets and timeline sequences from your app using Apple events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/sending-media-to-final-cut-pro-as-it-s-recorded)*