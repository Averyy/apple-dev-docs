# activates

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the system activates the app and brings it to the foreground.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var activates: Bool { get set }
```

#### Discussion

The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), which causes the system to bring the app to the foreground.

## See Also

- [var addsToRecentItems: Bool](nsworkspace/openconfiguration/addstorecentitems.md)
  A Boolean value indicating whether to add the app or documents to the Recent Items menu.
- [var allowsRunningApplicationSubstitution: Bool](nsworkspace/openconfiguration/allowsrunningapplicationsubstitution.md)
  A Boolean value that indicates whether to use a running instance of an application even if it’s at a different URL.
- [var createsNewApplicationInstance: Bool](nsworkspace/openconfiguration/createsnewapplicationinstance.md)
  A Boolean value indicating whether you want the system to launch a new instance of the app.
- [var hides: Bool](nsworkspace/openconfiguration/hides.md)
  A Boolean value indicating whether you want the app to hide itself after it launches.
- [var hidesOthers: Bool](nsworkspace/openconfiguration/hidesothers.md)
  A Boolean value indicating whether you want to hide all apps except the one that launched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/activates)*