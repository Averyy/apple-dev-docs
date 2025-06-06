# Using content script and style sheet keys

**Framework**: Safari Services

Learn about controlling style sheet and script injection with information property list keys.

#### Overview

Content scripts and style sheets have similar functionality. Safari injects content scripts (as `.js` files) and style sheets (as `.css` files) into webpages to customize web content. Injected scripts and styles have the same access privileges as the scripts and styles that execute from the webpage’s host. The scripts can also send messages to, and receive messages from, the extension.

The following table describes the `SFSafariContentScript` subkeys:

| Subkey | Type | Description |
| --- | --- | --- |
| `Script` | String | Required. A string that specifies the path to the content script relative to the Resources folder in the extension’s bundle, such as `script.js`. |
| `Allowed URL Patterns` | Array | Optional. An array of URL patterns that describe which pages Safari can inject the script into. |
| `Excluded URL Patterns` | Array | Optional. An array of URL patterns that describe which pages Safari can’t inject the script into. |

The following table describes the `SFSafariStyleSheet` subkeys:

| Subkey | Type | Description |
| --- | --- | --- |
| `Style Sheet` | String | Required. A string that specifies the path to the style sheet relative to the Resources folder in the extension’s bundle. |
| `Allowed URL Patterns` | Array | Optional. An array of URL patterns that describe which pages Safari can inject the style sheet into. |
| `Excluded URL Patterns` | Array | Optional. An array of URL patterns that describe which pages Safari can’t inject the style sheet into. |

To adjust permissions for scripts and style sheets, see [`Using permissions for scripts and style sheets`](using-permissions-for-scripts-and-style-sheets.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/using-content-script-and-style-sheet-keys)*