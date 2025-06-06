# Accessing files in browser extensions

**Framework**: BrowserEngineKit

Grant extensions access to files from within your browser app.

#### Overview

To share access to a file with one of your browser’s extensions, your browser app creates a file bookmark with implicit security scope. It sends the bookmark to the extension process, which resolves the bookmark to get a URL that the extension can use to access the file.

The bookmark your browser app sends is valid for the lifetime of the receiving extension process. If you invalidate the extension process or restart it because of a problem, your browser app needs to send the bookmark again for the extension to regain access to the file.

##### Create a File Bookmark

In your browser app, call [`bookmarkData(options:includingResourceValuesForKeys:relativeTo:)`](https://developer.apple.com/documentation/foundation/url/2143023-bookmarkdata) on a URL for the file to which you want to share access. Use the [`minimalBookmark`](https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions/1409050-minimalbookmark) option to get a minimal bookmark that uses fewer resources when you send it to your extension.

```swift
let url = URL(fileURLWithFileSystemRepresentation: thePath,
  isDirectory: false,
  relativeTo: nil);
let bookmark = url.bookmarkData(options: .minimalBookmark)
```

To give access to a directory, use the value `true` for the `isDirectory` parameter when you create the URL.

##### Send the Bookmark to the Extension

Use your browser’s interprocess communication (IPC) protocol to send the bookmark to your extension process. For information on using [`XPC`](https://developer.apple.com/documentation/XPC) as the IPC mechanism, see [`Using XPC to communicate with browser extensions`](using-xpc-to-communicate-with-browser-extensions.md).

##### Resolve the Bookmark

In your extension, create a URL for the file by resolving the bookmark data you receive from the browser app. Resolving the bookmark causes the operating system to automatically start your extension’s access to the resource, which extends your extension process’s sandbox to include the bookmarked file. When you finish accessing the file, you must call [`stopAccessingSecurityScopedResource()`](https://developer.apple.com/documentation/foundation/url/1780153-stopaccessingsecurityscopedresou) to avoid leaking kernel resources.

```swift
let url = try URL(resolvingBookmarkData: bookmark,
  options: .withoutUI)
// Use the file.
url.stopAccessingSecurityScopedResource()
```

If the resolved URL identifies a directory, your extension process receives access to that directory and all of its contents, including contents located recursively in subdirectories.

## See Also

- [Limiting resource access in web content extensions](limiting-resource-access-in-content-extensions.md)
  Reduce the impact of vulnerabilities in web content extensions by limiting privileges.
- [Attributing memory to a content extension](attributing-memory-to-a-content-extension.md)
  Adhere to operating-system limits on GPU memory use.
- [protocol RestrictedSandboxAppliable](restrictedsandboxappliable.md)
  A protocol that browser extensions implement to opt into a more restricted sandbox.
- [enum RestrictedSandboxRevision](restrictedsandboxrevision.md)
  Revisions to the restricted sandbox rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/accessing-files-in-browser-extensions)*