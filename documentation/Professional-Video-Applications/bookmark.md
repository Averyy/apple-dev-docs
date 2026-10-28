# bookmark

**Framework**: Professional-Video-Applications

Represents security-scoped bookmark data in a base64-encoded string.

## Overview

A bookmark is associated with a `media-rep` element. Bookmark data is required for sandboxed applications that need to access a media file outside the sandboxed environment. Because of this requirement, Final Cut Pro creates a document-scoped bookmark for the media file for each media representation to which the user grants access and includes this bookmark data in the `media-rep` element when exporting an FCPXML document. When your application exports an FCPXML document, it’s recommended that you add bookmark data to each `media-rep` element.

For information on security-scoped bookmark, see the *Security-Scoped Bookmarks and Persistent Resource Access* section in the [App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183).

> **Note**:  In FCPXML 1.8 or earlier, the `bookmark` element appears as a child of the `asset` element, and the bookmark data is for the asset’s original media file.

## Topics

### Creating and Using Bookmark Data
- [Using Bookmark Data](./using-bookmark-data.md)
  Access file-system resources using the security-scoped bookmark data.
- [Creating Bookmark Data](./creating-bookmark-data.md)
  Create bookmark data to access file-system resources in a sandboxed app.
- [Enabling Security-Scoped Bookmark and URL Access](./enabling-security-scoped-bookmark-and-url-access.md)
  Enable sandboxed apps to use security-scoped bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/bookmark)*