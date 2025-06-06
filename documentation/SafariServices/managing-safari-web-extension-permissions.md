# Managing Safari web extension permissions

**Framework**: Safari Services

Respect user privacy by setting appropriate permissions for your Safari web extension.

#### Overview

Safari web extensions need permission from the user to access and update web pages, and to perform other tasks in Safari. Safari users have an expectation of safety and privacy when browsing and using extensions. Fulfill that expectation by requesting permissions for your Safari web extension that minimize access to user data while allowing your extension to work properly.

##### Request Permissions

Request permissions for your extension in `manifest.json`. There are a few options to evaluate when you decide how to approach requesting permissions:

- Declare host patterns, API, `activeTab`, or `<all_urls>` permissions in the `permissions` array in `manifest.json` to request permission for your Safari web extension to work in matching websites. If your extension uses manifest version 3, declare host patterns in the `host_permissions` array.
- Declare optional permissions in the `optional_permissions` array in `manifest.json` to request permission for optional features.
- Specify a `matches` array for desired URL patterns in the `content_script` key in `manifest.json` to request permission for your content script to work in matching websites.

Use options that request the least access necessary for your extension to function. Prioritize using `activeTab`, host permissions, and `optional_permissions`; only use `<all_urls>` if there is no other option.

##### Grant and Manage Permissions

When the user visits a page where they haven’t granted access to your Safari web extension, Safari shows a badge next to your extension’s item that indicates the user needs to interact with the extension to grant it permission. In macOS, the user clicks the toolbar button and selects an option to grant permission for a single use, for the day, or for all websites, or to deny permission. In iOS, the user selects the extension’s entry in the More menu, and selects a permission option.

The user may then manage permissions for your extension:

- In Safari in macOS, the user can choose Safari > Settings and click the Extensions tab to see a summary of permission status for each extension. They can click the app’s name in the menu bar, then choose Settings from the menu. Then they can click the Websites tab and select the extension to see which websites have been configured for the extension, and can change the permission status for a selected website to Ask, Allow, or Deny.
- In a web app in macOS, the user can click the app’s name in the menu bar, then choose Settings from the menu. Then they can click the Edit Websites button to check which websites have been configured for the extension, and can change the permission status for a selected website to Ask, Allow, or Deny. When a user enables an extension for a web app, that automatically grants access to the high-level domain for the web app.
- In iOS, the user can open the Settings app, then choose Safari > Extensions in the General group. Then they can tap an extension to see which websites have been configured for the extension, and can change the permission status for a selected website to Ask, Allow, or Deny.

In Safari 17 and later, when you grant access to an extension for a specific web site, that grants the extension access to the site across all profiles, private browsing, and browsing without a profile.

Use the `activeTab` permission to minimize access requests to the user.

## See Also

- [Updating a Safari web extension](updating-a-safari-web-extension.md)
  Add new features and fix bugs in your Safari web extension using Xcode tools.
- [Previewing Metadata using Open Graph](previewing-metadata-using-open-graph.md)
  Build a Safari Extension that displays metadata using Open Graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/managing-safari-web-extension-permissions)*