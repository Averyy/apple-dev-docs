# Deprecated symbols

**Framework**: AppKit

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated symbols
- [static var andPrint: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/andprint.md)
  Print items instead of opening them.
- [static var withErrorPresentation: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/witherrorpresentation.md)
  Display an error panel to the user if a failure occurs.
- [static var inhibitingBackgroundOnly: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/inhibitingbackgroundonly.md)
  Causes launch to fail if the target is background-only.
- [static var withoutAddingToRecents: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/withoutaddingtorecents.md)
  Do not add the app or documents to the Recents menu.
- [static var withoutActivation: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/withoutactivation.md)
  Launch the app but do not bring it into the foreground.
- [static var async: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/async.md)
  Launch the app and return the results asynchronously.
- [static var allowingClassicStartup: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/allowingclassicstartup.md)
  Start up the Classic compatibility environment, if it is required by the app.
- [static var preferringClassic: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/preferringclassic.md)
  Force the app to launch in the Classic compatibility environment.
- [static var newInstance: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/newinstance.md)
  Create a new instance of the app, even if one is already running.
- [static var andHide: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/andhide.md)
  Tell the app to hide itself as soon as it finishes launching.
- [static var andHideOthers: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/andhideothers.md)
  Hide all apps except the newly launched one.
- [static var `default`: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/default.md)
  Launch the app asynchronously and launch it in the Classic environment, if required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/launchoptions-deprecated-symbols)*