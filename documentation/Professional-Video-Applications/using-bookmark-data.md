# Using Bookmark Data

**Framework**: Professional-Video-Applications  
**Role**: Article

Access file-system resources using the security-scoped bookmark data.

## Overview

Follow these steps to use a security-scoped bookmark in a sandboxed application:

1. Decode the bookmark data. The bookmark data in the bookmark element is Base64-encoded, so decode the bookmark before using it.
2. Resolve the decoded bookmark data into a security-scoped URL that points to the media asset.
3. Indicate that you want to use the security-scoped URL to access the file-system resource by calling the `startAccessingSecurityScopedResource` method.
4. Access the file-system resource using the security-scoped URL in your application.
5. Release the file-system resource by calling the `stopAccessingSecurityScopedResource` method.

The above steps are outlined in the following code snippet. For more information on the NSURL methods used, see [`NSURL`](../Foundation/nsurl.md) Class Reference.

```swift
// Decode the Base64 bookmark data
NSData *decodedBookmark =[[NSData alloc] initWithBase64EncodedString: bookmark options:NSDataBase64DecodingIgnoreUnknownCharacters];

// Resolve the decoded bookmark data into a security-scoped URL.
NSError *err = nil;
NSURL *url =[NSURL URLByResolvingBookmarkData: decodedBookmark options: NSURLBookmarkResolutionWithSecurityScope relativeToURL: sourceURL bookmarkDataIsStale: nil error:&err];

if (url)
  {
    // Indicate that you want to access the file-system resource.
    [url startAccessingSecurityScopedResource];

    // Use the resolved security scoped URL.
    ...
      // Release the file-system resource when you are done.
      [url stopAccessingSecurityScopedResource];
  }

// Release the decoded bookmark data
[decodedBookmark release];

```

> **Note**:  To use security-scoped bookmarks, your application must have the `com.apple.security.files.bookmarks.document-scope` entitlement set to `true`. For more details on enabling security-scoperd bookmarks,  see Enabling Security-Scoped Bookmark and URL Access.

## See Also

### Creating and Using Bookmark Data
- [Creating Bookmark Data](./creating-bookmark-data.md)
  Create bookmark data to access file-system resources in a sandboxed app.
- [Enabling Security-Scoped Bookmark and URL Access](./enabling-security-scoped-bookmark-and-url-access.md)
  Enable sandboxed apps to use security-scoped bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/using-bookmark-data)*