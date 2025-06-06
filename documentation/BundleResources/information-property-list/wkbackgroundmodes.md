# WKBackgroundModes

**Framework**: Bundle Resources  
**Kind**: typealias

The services a watchOS app provides that require it to continue running in the background.

**Availability**:
- watchOS 3.0+

#### Discussion

To add this key to the Information Property List, enable your WatchKit extension’s Background Modes capability in Xcode.

> ❗ **Important**:  You can only enable one of the extended runtime session modes (`self-care`, `mindfulness`, `physical-therapy`, or `alarm`). However, you can enable both an extended runtime session mode and the `workout-processing` mode. If you set the background modes using Xcode’s Signing & Capabilities tab, Xcode ensures that these values are set properly.

 You can only enable one of the extended runtime session modes (`self-care`, `mindfulness`, `physical-therapy`, or `alarm`). However, you can enable both an extended runtime session mode and the `workout-processing` mode. If you set the background modes using Xcode’s Signing & Capabilities tab, Xcode ensures that these values are set properly.

## See Also

- [Using extended runtime sessions](../WatchKit/using-extended-runtime-sessions.md)
  Create an extended runtime session that continues running your app after the user stops interacting with it.
- [Running workout sessions](../HealthKit/running-workout-sessions.md)
  Track a workout on Apple Watch.
- [UIBackgroundModes](information-property-list/uibackgroundmodes.md)
  Services provided by an app that require it to run in the background.
- [BGTaskSchedulerPermittedIdentifiers](information-property-list/bgtaskschedulerpermittedidentifiers.md)
  An array of strings containing developer-specified task identifiers in reverse URL notation.
- [LSBackgroundOnly](information-property-list/lsbackgroundonly.md)
  A Boolean value indicating whether the app runs only in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/wkbackgroundmodes)*