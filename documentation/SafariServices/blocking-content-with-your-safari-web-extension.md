# Blocking content with your Safari web extension

**Framework**: Safari Services

Build content blocking with declarative net request into your Safari web extension.

#### Overview

Add declarative content blocking that works in Safari, Mac web apps, and other browsers to your Safari web extension. This approach blocks content quickly and ensures privacy for users, because the web extension doesn’t need access to the entire web request to make blocking decisions.

Safari web extensions implement declarative content blocking with the Declarative Net Request API common to web extensions on other browsers.

##### Request Permission to Block Content

To use the Declarative Net Request API in your Safari web extension, first request permission. In your Xcode project, add the declarative net request permission to the permissions list in your `manifest.js` file.

```javascript
{
 ...
   "permissions": [
    "declarativeNetRequest",
    "activeTab"
  ],
  ...
}
```

For more information about permissions, see [`Managing Safari web extension permissions`](managing-safari-web-extension-permissions.md).

##### Add Rulesets to Your Extension and Manifest

You specify rules for content blocking in rulesets, which are files with `json` describing the content blocking rules. Add references to ruleset files that you create in your `manifest.js` file to tell Safari to use them. For example:

```javascript
{
   ...
   "declarative_net_request" : {
    "rule_resources" : [{
      "id": "ruleset_for_images",
      "enabled": true,
      "path": "image_rules.json"
    }, {
      "id": "ruleset_for_scripts",
      "enabled": false,
      "path": "script_rules.json"
    }]
  },
  ...
}
```

Build your rules describing how you want to block content, and add them to your ruleset files. For example:

```javascript
{
    "id": 1,
    "priority": 1,
    "action": { "type": "block" },
    "condition": {
        "regexFilter": ".*",
        "resourceTypes": [ "script" ]
    }
}

```

Review Safari’s support for specifying rules:

##### Adjust Rules Dynamically for the Extension or Session

After a user installs and uses your extension, adjust content blocking using dynamic rules. Add, change, or remove rules that persist between browser sessions using `updateDynamicRules`. Add, change, or remove rules that apply only to the current session using `updateSessionRules`.

```swift
var rule = {
    id: 1,
    priority: 1,
    action: { type: "block" },
    condition: {
        urlFilter: "||example.com",
        resourceTypes: [ "main_frame", "script" ]
    }
};

await browser.declarativeNetRequest.updateDynamicRules({ addRules: [ rule ] });

```

## See Also

- [Adopting Declarative Content Blocking in Safari Web Extensions](adopting-declarative-content-blocking-in-safari-web-extensions.md)
  Block web content with your web extension using the declarative net request API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/blocking-content-with-your-safari-web-extension)*