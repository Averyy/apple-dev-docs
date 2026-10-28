# userTabbingPreference

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A value that indicates the user’s preference for window tabbing.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class var userTabbingPreference: NSWindow.UserTabbingPreference { get }
```

```objc
@property (class, readonly) NSWindowUserTabbingPreference userTabbingPreference;
```

## Discussion

This value indicates the user’s preference for window tabbing as set in System Preferences. Check this preference any time you create a new window. For a list of possible values, see [`NSWindow.UserTabbingPreference`](./usertabbingpreference-swift.enum.md).

## See Also

### Managing Window Tabs
- [class var allowsAutomaticWindowTabbing: Bool](./allowsautomaticwindowtabbing.md)
  A Boolean value that indicates whether the app can automatically organize windows into tabs.
- [var tab: NSWindowTab](./tab.md)
  An object that represents information about a window when it displays as a tab.
- [var tabbingIdentifier: NSWindow.TabbingIdentifier](./tabbingidentifier-swift.property.md)
  A value that allows a group of related windows.
- [typealias TabbingIdentifier](./tabbingidentifier-swift.typealias.md)
  A value that allows a group of related windows.
- [func addTabbedWindow(NSWindow, ordered: NSWindow.OrderingMode)](./addtabbedwindow%28_,ordered%29.md)
  Adds the provided window as a new tab in a tabbed window using the specified ordering instruction.
- [var tabbingMode: NSWindow.TabbingMode](./tabbingmode-swift.property.md)
  A value that indicates when a window displays tabs.
- [var tabbedWindows: [NSWindow]?](./tabbedwindows.md)
  An array of windows that display as tabs.
- [func mergeAllWindows(Any?)](./mergeallwindows%28_%29.md)
  Merges all open windows into a single tabbed window.
- [func selectNextTab(Any?)](./selectnexttab%28_%29.md)
  Selects the next tab in the tab group in the trailing direction.
- [func selectPreviousTab(Any?)](./selectprevioustab%28_%29.md)
  Selects the previous tab in the tab group in the leading direction.
- [func moveTabToNewWindow(Any?)](./movetabtonewwindow%28_%29.md)
  Moves the tab to a new containing window.
- [func toggleTabBar(Any?)](./toggletabbar%28_%29.md)
  Shows or hides the tab bar.
- [func toggleTabOverview(Any?)](./toggletaboverview%28_%29.md)
  Shows or hides the tab overview.
- [var tabGroup: NSWindowTabGroup?](./tabgroup.md)
  A group of windows that display together as a tab group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/usertabbingpreference-swift.type.property)*