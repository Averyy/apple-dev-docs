# Optimizing your web extension for Safari

**Framework**: Safari Services

Support Dark Mode, reduce memory and power usage, and ensure feature compatibility to improve your web extension experience in Safari and web apps.

#### Overview

Add support for Dark Mode in your user interface so that your web extension fits in with the user’s selection of a light or dark overall scheme. Use a nonpersistent background page or service worker so that Safari can determine when to keep it in memory or unload it based on system memory usage.

As you update your Safari web extension to take advantage of new features that Safari supports, specify the Safari versions that your web extension is compatible with to avoid confusing your users.

##### Improve Your Extension Experience in Ios

There are important differences in Safari between macOS and iOS that your extension needs to address to give users the best possible experience in iOS:

- Users interact with the screen using their fingers instead of a mouse. Use pointer events instead of mouse events to handle touch interactions.
- There are a number of different screen sizes for different devices and orientations. Make full page extensions and pop-up pages responsive to different sizes.
- Some users prefer larger type on small screens. Support Dynamic Type in your web pages to let the user specify type size.
- iOS doesn’t support some APIs. To prevent throwing exceptions, check for the existence of APIs in iOS before using them.

##### Edit the Css Files to Support Dark Mode

To enable basic support for Dark Mode in your extension’s visual elements, add the following code to your CSS files:

```other
:root {
    color-scheme: light dark;
}
```

This allows Safari to automatically adjust the visual element’s background color, text colors, and form element colors. For more information about how to customize your Dark Mode experience, see [`Dark Mode Support in WebKit`](https://developer.apple.comhttps://webkit.org/blog/8840/dark-mode-support-in-webkit/).

##### Reduce Memory and Power Usage with a Nonpersistent Background Page

Consider making your background page nonpersistent in macOS when it’s primarily event-driven and responds to user interactions. In iOS, you must make your background page nonpersistent. Safari unloads your nonpersistent background page when the user isn’t directly interacting with the extension, which reduces memory usage and improves battery life. Your background page must be nonpersistent or you must declare your background script as a service worker if you’re using manifest version 3. Use a service worker for better compatibility with other browsers.

Make your background page nonpersistent by setting the `persistent` attribute to `false` in your extension’s `manifest.json` file.

```javascript
"background": {
    "scripts": ["background.js"],
    "persistent": false
}
```

Or, declare your background script as a service worker.

```javascript
"background": {
    "service_worker": "background.js"
}
```

When you make your background page nonpersistent:

- Add event listeners in the top level of your background page.
- Use the `Storage` API to save and restore state.
- Use the `Alarms` API instead of `setTimeout`.

> **Note**:  Make your background page persistent in macOS if you use the `webRequest` API in it, due to the frequency of callbacks that might fail if Safari unloads the background page.

 Make your background page persistent in macOS if you use the `webRequest` API in it, due to the frequency of callbacks that might fail if Safari unloads the background page.

##### Ensure Feature Compatibility By Specifying Versions

When you build features in your web extension that need a specific version of Safari, specify the required versions in your `manifest.json` file.

```javascript
"browser_specific_settings": {
    "safari": {
        "strict_min_version": "14.0",
        "strict_max_version": "14.*"
    }
}
```

Provide a specific version number in `strict_min_version` if you have a minimum Safari version requirement. Provide a specific version number in `strict_max_version` to limit the latest version of Safari that can use your Safari web extension. Use a wildcard symbol (`*`) in `strict_max_version` (for example, `14.*)` to indicate that your extension works in any minor version of Safari 14, but isn’t compatible with newer versions of Safari.

> **Note**:  In iOS, the iOS version and Safari version numbers are the same.

 In iOS, the iOS version and Safari version numbers are the same.

Review your manifest and web extension API usage periodically to see if there are new features Safari supports that you want to implement in your web extension. See [`Assessing your Safari web extension’s browser compatibility`](assessing-your-safari-web-extension-s-browser-compatibility.md) for more information.

## See Also

- [Adopting New Safari Web Extension APIs](adopting-new-safari-web-extension-apis.md)
  Improve your web extension in Safari with a non-persistent background page and new tab-override customization.
- [Syncing Safari web extensions across devices and platforms](syncing-safari-web-extensions-across-devices-and-platforms.md)
  Let users install your extension on one device and then use and manage the extension on all their other iOS and macOS devices.
- [Assessing your Safari web extension’s browser compatibility](assessing-your-safari-web-extension-s-browser-compatibility.md)
  Review your Safari web extension implementation plan, manifest keys, and JavaScript API usage for compatibility with other browsers.
- [Troubleshooting your Safari web extension](troubleshooting-your-safari-web-extension.md)
  Use developer resources to investigate and resolve common problems with Safari web extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/optimizing-your-web-extension-for-safari)*