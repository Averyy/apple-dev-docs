# MEContentBlocker

**Framework**: MailKit  
**Kind**: protocol  
**Role**: Protocol

An object that provides a set of rules to block content when displaying a message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol MEContentBlocker : NSObjectProtocol
```

```objc
@protocol MEContentBlocker <NSObject>
```

## Overview

A mail content blocker is similar to content blockers for Safari. Mail uses content blockers when it displays message content in a user’s mailbox. If your extension’s `Info.plist` file contains `MEContentBlocker` in the list of [`MEExtensionCapabilities`](../BundleResources/information-property-list/nsextension/nsextensionattributes/meextensioncapabilities.md), MailKit invokes [`handlerForContentBlocker()`](./meextension/handlerforcontentblocker%28%29.md) to get the object that provides content-blocking rules. The handler returns the content-blocking rules as JSON data from the [`contentRulesJSON()`](./mecontentblocker/contentrulesjson%28%29.md) method.

For more information about content blockers, see [Creating a content blocker](../SafariServices/creating-a-content-blocker.md).

> **Note**:  MailKit always applies content-blocking rules for enabled extensions. This is true even if the user clicks the “Load remote content” button on the banner that Mail displays when remote content isn’t loaded.

To indicate that your extension contains a content blocker, add `MEContentBlocker` to the `MEExtensionCapabilities` array in the extension’s `Info.plist` file:

```plist
<key>NSExtensionAttributes</key>
<dict>
    <key>MEExtensionCapabilities</key>
    <array>
        <string>MEContentBlocker</string>
    </array>
</dict>
```

## Topics

### Defining Rules to Block Content
- [func contentRulesJSON() -> Data](./mecontentblocker/contentrulesjson%28%29.md)
  The rules, as JSON data, that the system applies when it displays a message.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/mecontentblocker)*