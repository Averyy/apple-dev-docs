# hides

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether you want the app to hide itself after it launches.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var hides: Bool { get set }
```

```objc
@property BOOL hides;
```

## Discussion

The default value of this property is [`false`](../../../Swift/false.md), which leaves the app in its default state after launch. Setting the property to [`true`](../../../Swift/true.md) causes the app to hide itself.

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
- [var hidesOthers: Bool](./hidesothers.md)
  A Boolean value indicating whether you want to hide all apps except the one that launched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/hides)*