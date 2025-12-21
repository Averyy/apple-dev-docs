# hidesOthers

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether you want to hide all apps except the one that launched.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var hidesOthers: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), which leaves the visibility of other apps unchanged. Setting the property to [`true`](https://developer.apple.com/documentation/Swift/true) hides all apps except the one that launched.

## See Also

- [var activates: Bool](nsworkspace/openconfiguration/activates.md)
  A Boolean value indicating whether the system activates the app and brings it to the foreground.
- [var addsToRecentItems: Bool](nsworkspace/openconfiguration/addstorecentitems.md)
  A Boolean value indicating whether to add the app or documents to the Recent Items menu.
- [var allowsRunningApplicationSubstitution: Bool](nsworkspace/openconfiguration/allowsrunningapplicationsubstitution.md)
  A Boolean value that indicates whether to use a running instance of an application even if it’s at a different URL.
- [var createsNewApplicationInstance: Bool](nsworkspace/openconfiguration/createsnewapplicationinstance.md)
  A Boolean value indicating whether you want the system to launch a new instance of the app.
- [var hides: Bool](nsworkspace/openconfiguration/hides.md)
  A Boolean value indicating whether you want the app to hide itself after it launches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/hidesothers)*