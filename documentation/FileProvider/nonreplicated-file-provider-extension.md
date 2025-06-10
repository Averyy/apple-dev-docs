# Nonreplicated File Provider extension

**Framework**: File Provider

Build a File Provider extension that hosts and manages the user’s local files.

#### Overview

A nonreplicated File Provider extension must perform all of the following tasks:

- Create placeholders for remote files that you download only as needed.
- Intercept coordinated reads from the host app, so that your file provider can download or update the file with data from the remote server before the read occurs.
- Trigger a notification after coordinated writes from the host app, so that the extension can upload the changes to the remote server as needed.
- Enumerate the stored documents and folders.
- Execute actions—such as importing, moving, renaming, or deleting items—on the stored documents and folders.

Your File Provider extension can add custom actions to the file browser’s context menu using the [`File Provider UI`](https://developer.apple.com/documentation/FileProviderUI) framework. You can also define custom services to communicate with the host app using [`NSFileProviderService`](https://developer.apple.com/documentation/Foundation/NSFileProviderService). Use these interfaces to add features that aren’t provided by the base API.

##### Support Drag and Drop

If your application acts as a drag source for remote documents, override your [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) subclass’s [`registerFileRepresentation(forTypeIdentifier:fileOptions:visibility:loadHandler:)`](https://developer.apple.com/documentation/Foundation/NSItemProvider/registerFileRepresentation(forTypeIdentifier:fileOptions:visibility:loadHandler:)) method, and return the URL for the dragged item. This URL is the value returned by your extension’s [`urlForItem(withPersistentIdentifier:)`](nsfileproviderextension/urlforitem(withpersistentidentifier:).md) method. The URL may refer to a local file or, if you don’t have a local copy, to the file’s placeholder.

If the URL points to a placeholder, the system calls your File Provider extension’s [`startProvidingItem(at:completionHandler:)`](nsfileproviderextension/startprovidingitem(at:completionhandler:).md) method, giving you the opportunity to download the file.

## Topics

### Nonreplicated extension
- [class NSFileProviderExtension](nsfileproviderextension.md)
  The principal class for the nonreplicated File Provider extension.
- [Content and Change Tracking](content-and-change-tracking.md)
  Create enumerators to specify your file provider’s content, and track changes to that content.

## See Also

- [Replicated File Provider extension](replicated-file-provider-extension.md)
  Build a File Provider extension that syncs the local copies of your files with your remote storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nonreplicated-file-provider-extension)*