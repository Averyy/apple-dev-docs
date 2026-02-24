# Assessing your Safari web extension’s browser compatibility

**Framework**: Safari Services

Review your Safari web extension implementation plan, manifest keys, and JavaScript API usage for compatibility with other browsers.

#### Overview

Safari web extensions provide a number of features for compatibility with other browsers and a good developer experience, while ensuring the safety and privacy that users expect. Review your extension implementation or planned approach, `manifest.json` key usage, and selected JavaScript APIs for incompatibilities, and get suggestions and workarounds for potential issues.

##### Review Your Implementation Plan

Consider these factors when reviewing your implementation plan for your Safari web extension, and make adjustments as needed:

- Safari web extensions support both the `chrome.*` and `browser.*` namespaces. Use them as appropriate for your extension and your plan for browser compatibility.
- Safari web extensions support both the callback and `Promise` approaches for asynchronous APIs. Use the most suitable approach for your code quality and browser compatibility.
- Safari ignores file URL schemes in manifest permissions. If you use them, adjust your implementation.

##### Review Your Manifest

Generally, Safari web extensions ignore any unsupported manifest keys, but you may need to develop workarounds or alternative approaches for any incompatibilities. Check for these keys in your manifest and take action where needed:

- **`background`**: In iOS, you need to set the `persistent` attribute to `false`. With manifest version 3, all background pages are nonpersistent.
- **`devtools_page`**: Supported in Safari 16 or later.
- **`permissions.webRequestBlocking`**: Not supported. Use `permissions.webRequest` instead for macOS only.
- **`tabs`**: The extension needs host permission.
- **`update_url`**: Not supported. Handle Safari web extension updates with the App Store.
- **`externally_connectable`**: Supported in Safari 15.4 or later. `ids` not supported.

Safari 15.4 and later supports manifest versions 2 and 3. To evaluate compatibility for manifest keys in your extension, see Mozilla’s compatibility table at  [`Browser compatibility for manifest.json`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_compatibility_for_manifest.json).

##### Review Your Web Extension Api Usage

Generally, Safari ignores any unsupported JavaScript APIs, but you may need to develop workarounds or alternative approaches for any incompatibilities. Check for these APIs in your Safari web extension and take action where needed:

- **`storage.sync`**: Storage mechanism implemented, but syncing not supported.
- **`storage`**: Local storage limit is 5 MB. In Safari 15 or earlier, setting this to `unlimited` increases the extension’s storage limit to 10 MB. In Safari 16 or later, setting this to `unlimited` grants unlimited storage.
- **`storage.session`**: Supported in Safari 16.4 or later.
- **`identity`**: Not supported. Initiate an OAuth flow in a new tab.
- **`runtime`**: `setUninstallURL,` `onUpdateURL` not supported.
- **`cookies`**: `onChanged` not supported.
- **`webNavigation`**: `onCreatedNavigationTarget`, `onReferenceFragmentUpdated`, `onTabReplaced`, `onHistoryStateUpdated` not supported. `transitionType`, `transitionQualifiers` not supported.
- **`devtools`**: Supported in Safari 16 or later.
- **`scripting.executeScript`**: `injectImmediately` not supported.
- **`scripting.insertCSS`**: `origin`, `allFrames`, `frameIds` not supported.
- **`scripting.removeCSS`**: `origin`, `allFrames`, `frameIds` not supported.
- **`scripting`**: `registerContentScripts`, `getRegisteredContentScripts`, `unregisterContentScripts`, `updateContentScripts`  supported in Safari 16.4 or later.
- **`tabs.highlighted`**: Not supported.
- **`tabs.update`**: `highlighted` not supported.
- **`tabs.move`**: Not supported.
- **`tabs.detectLanguage`**: Returns `und` (undefined language) for macOS 10.15 and earlier. May include country code in the response; for example, `en-US` instead of `en`.
- **`tabs.captureVisibleTab`**: Doesn’t require `all_urls` permission.
- **`tabs.executeScript`**: `matchAboutBlank`, `runAt` not supported.
- **`tabs.insertCSS`**: `matchAboutBlank`, `runAt`, `cssOrigin`, `allFrames`, `frameId` not supported.
- **`tabs.removeCSS`**: `frameId`, `allFrames`, `matchAboutBlank`, `cssOrigin` not supported.
- **`tabs.getZoomSettings`, `tabs.setZoomSettings`, `tabs.onZoomChange`**: Extensions can’t change zoom settings on websites.
- **`webRequest`**: Not supported in iOS.

`BlockingResponse` not supported.

Blocking requests not supported.

`opt_extraInfoSpec` not supported for any of the events.

- **`webRequest.RequestFilter`, `webRequest.ResourceType`**: Supported.
- **`webRequest.HTTPHeaders`**: `cookies` not supported.
- **`WindowType`**: `panel`, `app`, and `devtool` types not supported.
- **`contextMenus, menus`**: Not supported in iOS.
- **`windows`**: `windows.create`, `windows.remove`, and `windows.update` not supported in iOS.

To evaluate compatibility for JavaScript extension APIs in your Safari web extension, see Mozilla’s compatibility table at [`Browser support for JavaScript APIs`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_support_for_JavaScript_APIs).

## See Also

- [Optimizing your web extension for Safari](optimizing-your-web-extension-for-safari.md)
  Support Dark Mode, reduce memory and power usage, and ensure feature compatibility to improve your web extension experience in Safari and web apps.
- [Adopting New Safari Web Extension APIs](adopting-new-safari-web-extension-apis.md)
  Improve your web extension in Safari with a non-persistent background page and new tab-override customization.
- [Syncing Safari web extensions across devices and platforms](syncing-safari-web-extensions-across-devices-and-platforms.md)
  Let users install your extension on one device and then use and manage the extension on all their other iOS and macOS devices.
- [Troubleshooting your Safari web extension](troubleshooting-your-safari-web-extension.md)
  Use developer resources to investigate and resolve common problems with Safari web extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/assessing-your-safari-web-extension-s-browser-compatibility)*