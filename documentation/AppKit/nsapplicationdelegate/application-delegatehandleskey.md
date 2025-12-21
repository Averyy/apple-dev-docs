# application(_:delegateHandlesKey:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates if the app supports the specified scripting key.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if your delegate handles the key or [`false`](https://developer.apple.com/documentation/Swift/false) if it does not.

#### Discussion

Implement this method and return [`true`](https://developer.apple.com/documentation/Swift/true) if your delegate handles the specified `key`, Your delegate must be able get or set the scriptable property or element that corresponds to that key. You need to handle only your app’s custom commands. The app already implements methods for each of the keys that it handles, where the method name matches the key.

For example, a scriptable app that doesn’t use Cocoa’s document-based app architecture can implement this method to supply its own document ordering. You want to do this because the standard app delegate expects to work with a document-based app. The TextEdit app (whose source is distributed with macOS developer tools) provides the following implementation:

```objc
return [key isEqualToString:@"orderedDocuments"];
```

TextEdit then implements the `orderedDocuments` method in its controller class to return an ordered list of documents. An app with its own window ordering might add a test for the key `orderedWindows` so that its delegate can provide its own version of `orderedWindows`.

> ❗ **Important**:  Cocoa scripting does not invoke this method for script commands other than `get` or `set`. For information on working with other commands, see [`Script Commands`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_script_cmds/SAppsScriptCmds.html#//apple_ref/doc/uid/20001242) in [`Cocoa Scripting Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

## Parameters

- `sender`: The app object associated with the delegate.
- `key`: The key to be handled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:delegatehandleskey:))*