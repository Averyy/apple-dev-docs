# createsNewApplicationInstance

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether you want the system to launch a new instance of the app.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var createsNewApplicationInstance: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the system always launches a new version of the app, even if an existing copy is already running. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), which causes the system to open the already running app when present.

## See Also

- [var activates: Bool](nsworkspace/openconfiguration/activates.md)
  A Boolean value indicating whether the system activates the app and brings it to the foreground.
- [var addsToRecentItems: Bool](nsworkspace/openconfiguration/addstorecentitems.md)
  A Boolean value indicating whether to add the app or documents to the Recent Items menu.
- [var allowsRunningApplicationSubstitution: Bool](nsworkspace/openconfiguration/allowsrunningapplicationsubstitution.md)
  A Boolean value that indicates whether to use a running instance of an application even if it’s at a different URL.
- [var hides: Bool](nsworkspace/openconfiguration/hides.md)
  A Boolean value indicating whether you want the app to hide itself after it launches.
- [var hidesOthers: Bool](nsworkspace/openconfiguration/hidesothers.md)
  A Boolean value indicating whether you want to hide all apps except the one that launched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/createsnewapplicationinstance)*