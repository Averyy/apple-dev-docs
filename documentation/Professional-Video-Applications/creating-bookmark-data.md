# Creating Bookmark Data

**Framework**: Professional-Video-Applications  
**Role**: Article

Create bookmark data to access file-system resources in a sandboxed app.

## Overview

When you export an FCPXML document as a file, you create a security-scoped bookmark relative to the containing document. When you export an FCPXML document for drag-and-drop, you create an unscoped bookmark.

Follow these steps to create bookmark data:

1. Access the security-scoped resource. This ensures that the relevant operating system resources are available.
2. Create bookmark data for the media asset URL. Use the `NSURLBookmarkCreationWithSecurityScope` option if you are generating a security-scoped bookmark for an FCPXML document stored in a file. The URL for the containing document file is required. For drag-and-drop there is no containing file, so set the option to 0 to generate an un-scoped bookmark.
3. Stop accessing the security scoped resource. This releases the relevant operating system resources required to create the bookmark data.

These steps are outlined in the following code snippet. For more information on the NSURL methods used, see  [`NSURL`](../Foundation/nsurl.md) Class Reference.

```swift
NSURL *assetURL = myAssetURL ();NSURL *documentURL = useSecurityScopedBookmark ? myDocumentURL () : nil;
     NSURLBookmarkCreationOptions
       options =
       useSecurityScopedBookmark ? NSURLBookmarkCreationWithSecurityScope : 0;
     NSError *
       err = nil;

// Start accessing security scoped resource
[assetURL startAccessingSecurityScopedResource];

// Create bookmark
     NSData *
   bookmark =[assetURL bookmarkDataWithOptions: options includingResourceValuesForKeys: nil relativeToURL: documentURL error:&err];

// Stop accessing security scoped resource
[assetURL stopAccessingSecurityScopedResource];

```

## See Also

### Creating and Using Bookmark Data
- [Using Bookmark Data](./using-bookmark-data.md)
  Access file-system resources using the security-scoped bookmark data.
- [Enabling Security-Scoped Bookmark and URL Access](./enabling-security-scoped-bookmark-and-url-access.md)
  Enable sandboxed apps to use security-scoped bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/creating-bookmark-data)*