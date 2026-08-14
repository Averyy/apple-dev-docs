# Debugging focus issues in your app

**Framework**: UIKit

Find errors and determine why the next focused item isn’t what you expected.

#### Overview

With the use of indirect controls for your tvOS app, it’s imperative that focus works correctly. To help you find focus problems, Apple provides two debugging tools: `UIFocusLoggingEnabled` and [`UIFocusDebugger`](uifocusdebugger.md).

##### Turn on Live Focus Logging

See how the focus engine determines which view is currently in focus by turning on live focus logging. As you move focus, the log updates, showing how the new view came into focus.

In your Xcode project, select Edit Scheme and add `-UIFocusLoggingEnabled YES` to the Arguments Passed On Launch section.

![Screenshot that shows adding the UIFocusLoggingEnabled argument in Xcode.](/images/com.apple.uikit/debugging-focus-issues-in-your-app-1@2x.png)

On launch, the debugger logs all focus events and displays the events in the Xcode console and the Console app. The debugger updates the log as focus changes in your app.

![Screenshot of focus debugging logs.](/images/com.apple.uikit/debugging-focus-issues-in-your-app-2@2x.png)

##### Find Focus Issues Using Uifocusdebugger

The [`UIFocusDebugger`](uifocusdebugger.md) class contains several methods to help you find focus issues. You don’t use this class or its methods directly from your code. Instead, during a debugging session, you call the methods of this class from the LLDB debugger command line to obtain information about the state of the focus system. For example, `po UIFocusDebugger.status()` returns the state of the focus engine.

## See Also

- [class UIFocusDebugger](uifocusdebugger.md)
  A runtime object for debugging focus-related interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/debugging-focus-issues-in-your-app)*