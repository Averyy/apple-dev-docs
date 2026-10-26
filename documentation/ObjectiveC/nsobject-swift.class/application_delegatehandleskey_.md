# application:delegateHandlesKey:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Sent by Cocoa’s built-in scripting support during execution of `get` or `set` script commands to find out if the delegate can handle operations on the specified key-value key.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

> **Deprecated**: Use [`application(_:delegateHandlesKey:)`](../../AppKit/nsapplicationdelegate/application%28_,delegatehandleskey%29.md) instead.

## Declaration

```objc
- (BOOL) application:(NSApplication *) sender delegateHandlesKey:(NSString *) key;
```

#### Return Value

[`YES`](../yes.md) if your delegate handles the key or [`NO`](../no.md) if it does not.

#### Discussion

The method should return [`YES`](../yes.md) if the delegate for the app `sender` handles the key specified by `key`, which means it can get or set the scriptable property or element that corresponds to that key. The app implements methods for each of the keys that it handles, where the method name matches the key.

For example, a scriptable app that doesn’t use Cocoa’s document-based app architecture can implement this method to supply its own document ordering. Such an app might want to do this because the standard app delegate expects to work with a document-based app. The TextEdit app (whose source is distributed with macOS developer tools) provides the following implementation:

```objc
return [key isEqualToString:@"orderedDocuments"];
```

TextEdit then implements the `orderedDocuments` method in its controller class to return an ordered list of documents. An app with its own window ordering might add a test for the key `orderedWindows` so that its delegate can provide its own version of `orderedWindows`.

> ❗ **Important**:  Cocoa scripting does not invoke this method for script commands other than `get` or `set`. For information on working with other commands, see [Script Commands](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_script_cmds/SAppsScriptCmds.html#//apple_ref/doc/uid/20001242) in [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

## Parameters

- `sender`: The app object associated with the delegate.
- `key`: The key to be handled.

## See Also

### Related Documentation
- [var orderedWindows: [NSWindow]](../../AppKit/nsapplication/orderedwindows.md)
  An array of window objects arranged according to their front-to-back ordering on the screen.
- [var orderedDocuments: [NSDocument]](../../AppKit/nsapplication/ordereddocuments.md)
  An array of document objects arranged according to the front-to-back ordering of their associated windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/application:delegatehandleskey:)*