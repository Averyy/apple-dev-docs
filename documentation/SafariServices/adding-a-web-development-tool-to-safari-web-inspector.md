# Adding a web development tool to Safari Web Inspector

**Framework**: Safari Services

Expand the built-in Safari Web Inspector to include your custom tool, augmenting developers’ options for inspecting, testing, and debugging webpages.

#### Overview

Safari provides Web Inspector, a set of tools that web developers use to inspect and debug their webpages. These built-in development tools are useful for analyzing basic issues in HTML, CSS, and JavaScript.

In Safari 16 or later, you can create a custom web development tool that can inspect and interact with a webpage in a target window. You design the tool’s user interface to meet to your web development approach and needs.

For example, you may build webpages with a custom web framework or architecture, where the built-in web development tools are not sufficient to see how components interact, how state is managed, or how events are processed. Your tool could provide support that specifically addresses the development needs of that custom web framework or architecture.

You deliver your tool in a Safari web extension. When a user downloads your extension, your tool appears as a new tab in Web Inspector. For more information about creating a new extension, see [`Creating a Safari web extension`](creating-a-safari-web-extension.md). For more information about converting an existing web extension that works in another browser, see [`Converting a web extension for Safari`](converting-a-web-extension-for-safari.md). After you create or convert the extension, configure your Safari web extension manifest so that Safari adds your tool to Web Inspector, and satisfy requirements for Safari user permissions.

##### Add the Web Development Tool to Your Extension

Add an HTML file to your extension that contains the code for your web development tool and user interface, and add any supporting JavaScript files that contain additional code your web development tool uses. For more information on adding files, see [`Updating a Safari web extension`](updating-a-safari-web-extension.md).

Then, in your extension’s `manifest.json` file, do the following:

- Add the `devtools_page` key, and specify your tool’s HTML file.
- Add or update the `permissions` entry to include the `devtools` permission.

```javascript
{
    ...
    "devtools_page": "example_devtool.html",
    "permissions": "devtools"
    ...
}
```

For more information on development tools’ capabilities and how to build them, see [`Extending the developer tools`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Extending_the_developer_tools).

##### Satisfy Safari User Permission Requirements

Safari requires user permission for each target page that the user inspects with your development tool. Optimize your development tool approach to support this requirement:

- To tell Safari to add your tool as a tab in Web Inspector, you must create the inspector tab in your extension using `browser.devtools.panel.create()`. Don’t conditionally create the inspector tab after you check permissions; if you do, Safari won’t add a tab for your tool.
- Let Safari handle permissions with its dialogs; then update your user interface based on permission status.

For more information on requesting permissions in your extension, see [`Managing Safari web extension permissions`](managing-safari-web-extension-permissions.md).

Install and run your extension. For more information, see [`Running your Safari web extension`](running-your-safari-web-extension.md). To view your development tool in Safari, choose Develop > Show Web Inspector. For more information on enabling development tools in Safari, see [`Web development tools`](https://developer.apple.comhttps://developer.apple.com/safari/tools/).

## See Also

- [Creating a Safari web extension](creating-a-safari-web-extension.md)
  Build a Safari web extension in Xcode.
- [Converting a web extension for Safari](converting-a-web-extension-for-safari.md)
  Convert your existing extension to a Safari web extension using Xcode’s command-line tool.
- [Updating a Safari web extension](updating-a-safari-web-extension.md)
  Add new features and fix bugs in your Safari web extension using Xcode tools.
- [Managing Safari web extension permissions](managing-safari-web-extension-permissions.md)
  Respect user privacy by setting appropriate permissions for your Safari web extension.
- [Running your Safari web extension](running-your-safari-web-extension.md)
  Install and update your extension in Safari as you make changes in development.
- [Creating Safari Web Inspector extensions](creating-safari-web-inspector-extensions.md)
  Learn how to make custom Safari Web Inspector extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/adding-a-web-development-tool-to-safari-web-inspector)*