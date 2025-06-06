# applicationDockMenu(_:)

**Framework**: AppKit  
**Kind**: method

Returns the app’s dock menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func applicationDockMenu(_ sender: NSApplication) -> NSMenu?
```

#### Return Value

The menu to display in the dock.

#### Discussion

You can also connect a menu in Interface Builder to the `dockMenu` outlet. A third way for your application to specify a dock menu is to provide an `NSMenu` in a nib.

If this method returns a menu, this menu takes precedence over the `dockMenu` in the nib.

The target and action for each menu item are passed to the dock. On selection of the menu item the dock messages your application, which should invoke `[NSApp sendAction:selector to:target from:nil]`.

To specify an `NSMenu` in a nib, you add the nib name to the `info.plist`, using the key `AppleDockMenu`. The nib name is specified without an extension. You then create a connection from the file’s owner object (which by default is `NSApplication`) to the menu. Connect the menu to the `dockMenu` outlet of `NSApplication`. The menu is in its own nib file so it can be loaded lazily when the `dockMenu` is requested, rather than at launch time.

## Parameters

- `sender`: The application object associated with the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdockmenu(_:))*