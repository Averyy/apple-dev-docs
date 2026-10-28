# Enabling Security-Scoped Bookmark and URL Access

**Framework**: Professional-Video-Applications  
**Role**: Article

Enable sandboxed apps to use security-scoped bookmark data.

## Overview

If you want to provide your sandboxed app with persistent access to file-system resources, you must enable security-scoped bookmark and URL access. Security-scoped bookmarks are available starting in macOS v10.7.3.

To add the `bookmarks.app-scope` or `bookmarks.document-scope` entitlement, edit your app’s  `.entitlements` property list file using the Xcode property list editor. Based on the type of access you want, use the entitlement keys shown in the table below. Use a value of `true` for each entitlement you want to enable. You can enable either or both entitlements.

For more information on security-scoped bookmarks, see [Security-Scoped Bookmarks and Persistent Resource Access](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AppSandboxInDepth/AppSandboxInDepth.html#//apple_ref/doc/uid/TP40011183-CH3-SW16) in [App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183).

| Entitlement key | Description |
| --- | --- |
| `com.apple.security.files.bookmarks.app-scope` | Enables use of app-scoped bookmarks and URLs. |
| `com.apple.security.files.bookmarks.document-scope` | Enables use of document-scoped bookmarks and URLs. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) **Version note**: In macOS v10.7.3, this entitlement key was named `com.apple.security.files.bookmarks.collection-scope`. |

## See Also

### Creating and Using Bookmark Data
- [Using Bookmark Data](./using-bookmark-data.md)
  Access file-system resources using the security-scoped bookmark data.
- [Creating Bookmark Data](./creating-bookmark-data.md)
  Create bookmark data to access file-system resources in a sandboxed app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/enabling-security-scoped-bookmark-and-url-access)*