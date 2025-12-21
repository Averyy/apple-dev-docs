# crashDetectionManager(_:didDetect:)

**Framework**: SafetyKit  
**Kind**: method

Receive and process a Crash Detection event.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
optional func crashDetectionManager(_ crashDetectionManager: SACrashDetectionManager, didDetect event: SACrashDetectionEvent)
```

#### Discussion

To receive Crash Detection events, create a new [`SACrashDetectionManager`](sacrashdetectionmanager.md) instance and set its delegate early in the app life cycle, such as [`applicationDidFinishLaunching(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationDidFinishLaunching(_:)).

> ❗ **Important**:  Use the iOS Simulator to test Crash Detection events and the background functionality of your app.

Following a Crash Detection event, the system launches the app in the background. When the app launches, it performs critical tasks related to the Crash Detection event, such as placing a network request or scheduling a local notification. If the system generates multiple Crash Detection events while the app isn’t running, it reports the most recent event on the next app launch. The system may report the same Crash Detection event across different launches of your app, so always check [`date`](sacrashdetectionevent/date.md) before processing it.

## Parameters

- `crashDetectionManager`: The Crash Detection manager that detected the event.
- `event`: The Crash Detection event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/sacrashdetectiondelegate/crashdetectionmanager(_:diddetect:))*