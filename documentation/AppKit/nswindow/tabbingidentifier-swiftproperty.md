# tabbingIdentifier

**Framework**: AppKit  
**Kind**: property

A value that allows a group of related windows.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
var tabbingIdentifier: NSWindow.TabbingIdentifier { get set }
```

#### Discussion

By default, a window generates a tabbing identifier from inherent window properties, such as the window class name, the delegate class name, the window controller class name, and some additional state. Group windows together by using the same tabbing identifier.

## See Also

- [class var allowsAutomaticWindowTabbing: Bool](nswindow/allowsautomaticwindowtabbing.md)
  A Boolean value that indicates whether the app can automatically organize windows into tabs.
- [class var userTabbingPreference: NSWindow.UserTabbingPreference](nswindow/usertabbingpreference-swift.type.property.md)
  A value that indicates the user’s preference for window tabbing.
- [var tab: NSWindowTab](nswindow/tab.md)
  An object that represents information about a window when it displays as a tab.
- [typealias TabbingIdentifier](nswindow/tabbingidentifier-swift.typealias.md)
  A value that allows a group of related windows.
- [func addTabbedWindow(NSWindow, ordered: NSWindow.OrderingMode)](nswindow/addtabbedwindow(_:ordered:).md)
  Adds the provided window as a new tab in a tabbed window using the specified ordering instruction.
- [var tabbingMode: NSWindow.TabbingMode](nswindow/tabbingmode-swift.property.md)
  A value that indicates when a window displays tabs.
- [var tabbedWindows: [NSWindow]?](nswindow/tabbedwindows.md)
  An array of windows that display as tabs.
- [func mergeAllWindows(Any?)](nswindow/mergeallwindows(_:).md)
  Merges all open windows into a single tabbed window.
- [func selectNextTab(Any?)](nswindow/selectnexttab(_:).md)
  Selects the next tab in the tab group in the trailing direction.
- [func selectPreviousTab(Any?)](nswindow/selectprevioustab(_:).md)
  Selects the previous tab in the tab group in the leading direction.
- [func moveTabToNewWindow(Any?)](nswindow/movetabtonewwindow(_:).md)
  Moves the tab to a new containing window.
- [func toggleTabBar(Any?)](nswindow/toggletabbar(_:).md)
  Shows or hides the tab bar.
- [func toggleTabOverview(Any?)](nswindow/toggletaboverview(_:).md)
  Shows or hides the tab overview.
- [var tabGroup: NSWindowTabGroup?](nswindow/tabgroup.md)
  A group of windows that display together as a tab group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/tabbingidentifier-swift.property)*