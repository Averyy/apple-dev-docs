# Creating a content blocker

**Framework**: Safari Services

Create a content blocker for Safari in Xcode.

#### Overview

Content blockers are app extensions that you build using Xcode. They indicate to Safari a set of rules to use to block content in the browser window. Blocking behaviors include hiding elements, blocking loads, and stripping cookies from Safari requests.

You use a containing app to contain and deliver a content blocker in the App Store. The containing app defines the context to provide to the extension and initiates the extension life cycle  by sending a request in response to a user action.

When the content blocker launches, it communicates with its containing app through a set of shared resources, and it communicates directly with Safari.

![An image showing a content blocker communicating with various resources.](https://docs-assets.developer.apple.com/published/f6abb4e38e5784ce33805c31812e484a/media-4047829%402x.png)

Apps tell Safari in advance what kinds of content to block. Because Safari doesn’t have to consult with the app during loading, and because Xcode compiles content blockers into bytecode, this model runs efficiently. Additionally, content blockers have no knowledge of users’ history or the websites they visit.

##### Add the Extension Target to Your Containing App

Choose File > New > Target and select Content Blocker Extension. Click Next and give your content blocker a name.

![An Xcode screenshot showing the Content Blocker Extension option selected in the Choose a template for your new target dialog.](https://docs-assets.developer.apple.com/published/63322313c509c7bdb7bb2ba0e49da099/media-4047980%402x.png)

##### Add Behaviors to Your Content Blocker

In your Xcode project, open the folder with the same title as your content blocker. This folder contains the action request handler and a JSON file, along with a property list file and an entitlements file. Open the `blockerList.json` file.

In the JSON file, write rules to define content-blocking behaviors. Each rule is a JSON object containing action and trigger dictionaries. The action tells Safari what to do when it encounters a match for the trigger. The trigger tells Safari when to perform the corresponding action. Content blockers are JSON arrays of these rules.

```javascript
[
    {
        "trigger": {
            ...
        },
        "action": {
            ...
        }
    },
    {
        "trigger": {
            ...
        },
        "action": {
            ...
        }
    }
]
```

##### Add Triggers to Your Content Blocker

A trigger dictionary must include a `url-filter` key, which specifies a pattern to match the URL against. The remaining keys are optional and modify the behavior of the trigger. For example, you can limit the trigger to specific domains or have it not apply when Safari finds a match for a specific domain.

For example, to write a trigger for image and style sheet resources that Safari finds on any domain except those specified, add the following to the JSON file:

```swift
"trigger": {
        "url-filter": ".*",
        "resource-type": ["image", "style-sheet"],
        "unless-domain": ["your-content-server.com", "trusted-content-server.com"]
}
```

###### Capture Urls By Pattern

In `url-filter`, match more than just a specific URL, using regular expressions.

| Syntax | Description |
| --- | --- |
| `.*` | Matches all strings with a dot appearing zero or more times. Use this syntax to match every URL. |
| `.` | Matches any character. |
| `\.` | Explicitly matches the dot character. |
| `[a-b]` | Matches a range of alphabetic characters. |
| `(abc)` | Matches groups of the specified characters. |
| `+` | Matches the preceding term one or more times. |
| `*` | Matches the preceding character zero or more times. |
| `?` | Matches the preceding character zero or one time. |

###### Use Trigger Fields to Define Patterns

There are many valid trigger fields you can use to define patterns.

| Trigger | Description |
| --- | --- |
| `url-filter-is-case-sensitive` | A Boolean value. The default value is `false`. |
| `if-domain` | An array of strings to match to a URL’s domain; limits the action to a list of specific domains. The values must be lowercase ASCII, or Punycode for non-ASCII. Add `*` in front to match domain and subdomains. You can’t use this with `unless-domain`. |
| `unless-domain` | An array of strings to match to a URL’s domain; acts on any site except domains in a provided list. The values must be lowercase ASCII, or Punycode for non-ASCII. Add `*` in front to match domain and subdomains. You can’t use this with `if-domain`. |
| `resource-type` | An array of strings representing the resource types (how the browser intends to use the resource) that the rule needs to match. If you don’t specify this, the rule matches all resource types. Valid values are `document`, `image`, `style-sheet`, `script`, `font`, `raw` (any untyped load), `svg-document`, `media`, `popup`, `ping`, `fetch`, `websocket`, and `other` (like `raw`, but doesn’t include `fetch` or `websocket`). |
| `load-type` | An array of strings that can include one of two mutually exclusive values. If you don’t specify this, the rule matches all load types. `first-party` triggers only if the resource has the same scheme, domain, and port as the main page resource. `third-party` triggers if the resource isn’t from the same domain as the main page resource. |
| `if-top-url` | An array of strings to match to the entire main document URL; limits the action to a specific list of URL patterns. The values must be lowercase ASCII, or Punycode for non-ASCII. You can’t use this with `unless-top-url`. |
| `unless-top-url` | An array of strings to match to the entire main document URL; acts on any site except URL patterns in the provided list. The values must be lowercase ASCII, or Punycode for non-ASCII. You can’t use this with `if-top-url`. |
| `load-context` | An array of strings that specify loading contexts. Valid values are `top-frame` and `child-frame`. |

##### Add Actions to Your Content Blocker

When a trigger matches a resource, the browser queues the associated action for execution. Safari evaluates all the triggers, and executes the actions in order. When a domain matches a trigger, Safari skips all rules after the triggered rule that specify the same action.

Group the rules with similar actions together to improve performance. For example, first specify rules that block content loading, followed by rules that block cookies. The trigger evaluation continues at the first rule that specifies a different action.

There are only two valid fields for actions: `type` and `selector`. An action type is required. If the type is `css-display-none`, a `selector` is required as well; otherwise, the `selector` is optional.

For example, you can specify the following type and selector:

```swift
"action": {
        "type": "css-display-none",
        "selector": "#newsletter, :matches(.main-page, .article) .news-overlay"
}
```

###### Select Values for the Type Field

| Syntax | Description |
| --- | --- |
| `block` | Stops loading of the resource. If Safari caches the resource, it ignores the cache. |
| `block-cookies` | Strips cookies from the header before sending it to the server. This only blocks cookies otherwise acceptable to Safari’s privacy policy. Combining with `ignore-previous-rules` doesn’t override the browser’s privacy settings. |
| `css-display-none` | Hides elements of the page based on a CSS selector. A `selector` field contains the selector list. Any matching element has its `display` property set to `none`, which hides it. |
| `ignore-previous-rules` | Ignores previously triggered actions. |
| `make-https` | Changes a URL from `http` to `https`. This doesn’t affect URLs with a specified (nondefault) port and links using other protocols. |

For the `selector` field, specify a string that defines a selector list. This value is required when the action type is `css-display-none`. If it’s not, Safari ignores the `selector` field. Use CSS identifiers as the individual selector values, separated by commas. Safari and WebKit support all of the CSS selectors for Safari content-blocking rules.

## See Also

- [class SFContentBlockerManager](sfcontentblockermanager.md)
  A class that your app uses to interact with a content blocker extension.
- [class SFContentBlockerState](sfcontentblockerstate.md)
  The state of a content blocker extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/creating-a-content-blocker)*