# hidesOthers

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether you want to hide all apps except the one that launched.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var hidesOthers: Bool { get set }
```

```objc
@property BOOL hidesOthers;
```

#### Discussion

The default value of this property is [`false`](../../../Swift/false.md), which leaves the visibility of other apps unchanged. Setting the property to [`true`](../../../Swift/true.md) hides all apps except the one that launched.

## See Also

### Specifying app-related behaviors
- [var activates: Bool](./activates.md)
  A Boolean value indicating whether the system activates the app and brings it to the foreground.
- [var addsToRecentItems: Bool](./addstorecentitems.md)
  A Boolean value indicating whether to add the app or documents to the Recent Items menu.
- [var allowsRunningApplicationSubstitution: Bool](./allowsrunningapplicationsubstitution.md)
  A Boolean value that indicates whether to use a running instance of an application even if it’s at a different URL.
- [var createsNewApplicationInstance: Bool](./createsnewapplicationinstance.md)
  A Boolean value indicating whether you want the system to launch a new instance of the app.
- [var hides: Bool](./hides.md)
  A Boolean value indicating whether you want the app to hide itself after it launches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/hidesothers)*