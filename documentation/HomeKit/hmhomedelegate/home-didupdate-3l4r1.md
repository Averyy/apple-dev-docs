# home(_:didUpdate:)

**Framework**: HomeKit  
**Kind**: method

Tells the delegate that a home updated a trigger.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func home(_ home: HMHome, didUpdate trigger: HMTrigger)
```

#### Discussion

Enabling or disabling a trigger or modifying its action sets will cause this method to be called.

## Parameters

- `home`: The home.
- `trigger`: The trigger that was updated.

## See Also

- [func home(HMHome, didAdd: HMActionSet)](hmhomedelegate/home(_:didadd:)-9dcki.md)
  Tells the delegate that a home added an action set.
- [func home(HMHome, didUpdateNameFor: HMActionSet)](hmhomedelegate/home(_:didupdatenamefor:)-7fxvl.md)
  Tells the delegate that a home updated the name of an action set.
- [func home(HMHome, didUpdateActionsFor: HMActionSet)](hmhomedelegate/home(_:didupdateactionsfor:).md)
  Tells the delegate that a home updated the actions for an action set.
- [func home(HMHome, didRemove: HMActionSet)](hmhomedelegate/home(_:didremove:)-80ewx.md)
  Tells the delegate that a home removed an action set.
- [func home(HMHome, didAdd: HMTrigger)](hmhomedelegate/home(_:didadd:)-64yxx.md)
  Tells the delegate that a home added a trigger.
- [func home(HMHome, didUpdateNameFor: HMTrigger)](hmhomedelegate/home(_:didupdatenamefor:)-8vn79.md)
  Tells the delegate that a home updated the name of a trigger.
- [func home(HMHome, didRemove: HMTrigger)](hmhomedelegate/home(_:didremove:)-4ujfa.md)
  Tells the delegate that a home removed a trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomedelegate/home(_:didupdate:)-3l4r1)*