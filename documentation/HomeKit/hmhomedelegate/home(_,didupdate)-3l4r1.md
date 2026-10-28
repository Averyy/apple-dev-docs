# home(_:didUpdate:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) home:(HMHome *) home didUpdateTrigger:(HMTrigger *) trigger;
```

## Discussion

Enabling or disabling a trigger or modifying its action sets will cause this method to be called.

## Parameters

- `home`: The home.
- `trigger`: The trigger that was updated.

## See Also

### Observing Action and Trigger Configuration
- [func home(HMHome, didAdd: HMActionSet)](./home%28_,didadd%29-9dcki.md)
  Tells the delegate that a home added an action set.
- [func home(HMHome, didUpdateNameFor: HMActionSet)](./home%28_,didupdatenamefor%29-7fxvl.md)
  Tells the delegate that a home updated the name of an action set.
- [func home(HMHome, didUpdateActionsFor: HMActionSet)](./home%28_,didupdateactionsfor%29.md)
  Tells the delegate that a home updated the actions for an action set.
- [func home(HMHome, didRemove: HMActionSet)](./home%28_,didremove%29-80ewx.md)
  Tells the delegate that a home removed an action set.
- [func home(HMHome, didAdd: HMTrigger)](./home%28_,didadd%29-64yxx.md)
  Tells the delegate that a home added a trigger.
- [func home(HMHome, didUpdateNameFor: HMTrigger)](./home%28_,didupdatenamefor%29-8vn79.md)
  Tells the delegate that a home updated the name of a trigger.
- [func home(HMHome, didRemove: HMTrigger)](./home%28_,didremove%29-4ujfa.md)
  Tells the delegate that a home removed a trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomedelegate/home(_:didupdate:)-3l4r1)*