# allowsRunningApplicationSubstitution

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether to use a running instance of an application even if it’s at a different URL.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var allowsRunningApplicationSubstitution: Bool { get set }
```

#### Discussion

If an instance of an application is already running and is capable of opening the provided URLs, but the running instance is at a different URL, use the running application.

This property defaults to [`true`](https://developer.apple.com/documentation/Swift/true). Set this to [`false`](https://developer.apple.com/documentation/Swift/false) if you let the user select between specific versions of an application, or let them choose a particular installation.

## See Also

- [var activates: Bool](nsworkspace/openconfiguration/activates.md)
  A Boolean value indicating whether the system activates the app and brings it to the foreground.
- [var addsToRecentItems: Bool](nsworkspace/openconfiguration/addstorecentitems.md)
  A Boolean value indicating whether to add the app or documents to the Recent Items menu.
- [var createsNewApplicationInstance: Bool](nsworkspace/openconfiguration/createsnewapplicationinstance.md)
  A Boolean value indicating whether you want the system to launch a new instance of the app.
- [var hides: Bool](nsworkspace/openconfiguration/hides.md)
  A Boolean value indicating whether you want the app to hide itself after it launches.
- [var hidesOthers: Bool](nsworkspace/openconfiguration/hidesothers.md)
  A Boolean value indicating whether you want to hide all apps except the one that launched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/allowsrunningapplicationsubstitution)*