# SafetyKit

**Framework**: SafetyKit  
**Kind**: module

Detect and respond to car crash events in your app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.1+
- macOS 13.0+
- watchOS 10.1+

#### Overview

SafetyKit provides Crash Detection, a feature that sends a crash event to an authorized app if a person is in a severe vehicular crash as detected by their iPhone 14, iPhone 14 Pro, Apple Watch Series 8, Apple Watch SE (2nd generation), or Apple Watch Ultra. These devices provide a feature called Emergency SOS - Call After Severe Crash. If enabled, Emergency SOS dials a municipal emergency service such as 911 in the event of a vehicular crash. After Emergency SOS places its call, Crash Detection can assist someone by initiating a call to a contact designated by the app, such as a roadside assistance provider.

SafetyKit supports three crash scenarios. In each scenario, Apple is the first party, and your app is the third party.

The first scenario has first-party Emergency SOS turned off and third-party sharing turned on. When the device detects a crash, a critical alert occurs and the third party receives the crash information.

![A timeline titled “first-party Emergency SOS turned off with third-party sharing” shows a sequence of events. When the device detects a crash, a critical alert occurs, and the third party receives the crash information.](https://docs-assets.developer.apple.com/published/bd4ea82d870aa79637f8de08241677a7/media-4257130%402x.png)

In the second scenario, first-party Emergency SOS and third-party sharing are turned on. When the device detects a crash, the first-party Emergency SOS runs automatically. After the first party completes its procedures, a critical alert occurs and the third party receives the crash information.

![A timeline titled “first-party Emergency SOS turned on with third-party sharing” shows a sequence of events. When the device detects a crash, the first-party SOS runs automatically. A critical alert occurs and the third party receives the crash information.](https://docs-assets.developer.apple.com/published/b1972da934fc92001f8ce7b9172fc4b6/media-4257129%402x.png)

In the third scenario, first-party Emergency SOS is turned on and there’s no third-party sharing. When the device detects a crash, the first-party Emergency SOS runs automatically.

![A timeline titled “first-party Emergency SOS only” shows a sequence of events. A device detects a crash, then the first-party SOS runs automatically.](https://docs-assets.developer.apple.com/published/02e4364ac1bff4c8bcdb7e3f8a19ef22/media-4257131%402x.png)

> ❗ **Important**:  Crash Detection requires the [`com.apple.developer.severe-vehicular-crash-event`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.severe-vehicular-crash-event) entitlement. To apply for this entitlement, see [`Request Access to the Vehicular Crash Event Entitlement`](https://developer.apple.comhttps://developer.apple.com/contact/request/vehicular-crash-events/).

To support Crash Detection, use [`SACrashDetectionManager`](sacrashdetectionmanager.md) to determine whether it’s available and if so, ask permission to allow your app to receive crash events. Then set [`delegate`](sacrashdetectionmanager/delegate.md) to the object that receives the events. Only one app on the device can receive Crash Detection events.

If your app receives a Crash Detection event, use [`SAEmergencyResponseManager`](saemergencyresponsemanager.md) to provide assistance.

## Topics

### Detecting a crash
- [class SACrashDetectionManager](sacrashdetectionmanager.md)
  Provides registration and management of Crash Detection events.
- [enum SAAuthorizationStatus](saauthorizationstatus.md)
  An enumeration that represents the current Crash Detection event authorization state.
- [class SACrashDetectionEvent](sacrashdetectionevent.md)
  Describes the information about a vehicular crash.
- [protocol SACrashDetectionDelegate](sacrashdetectiondelegate.md)
  The protocol that an object adopts to receive Crash Detection events and changes to the authorization status.
### Responding to a crash
- [class SAEmergencyResponseManager](saemergencyresponsemanager.md)
  Provides actions in response to a Crash Detection event.
- [protocol SAEmergencyResponseDelegate](saemergencyresponsedelegate.md)
  The interface for receiving updates about a requested emergency response action.
- [SACrashDetectionEvent.Response](sacrashdetectionevent/response-swift.enum.md)
  An enumeration that defines possible emergency responses to a Crash Detection event.
### Handling errors
- [let SAErrorDomain: String](saerrordomain.md)
  The domain for error objects that SafetyKit produces.
- [SAError.Code](saerror/code.md)
  Codes for identifying errors in SafetyKit.
- [struct SAError](saerror.md)
  An error reported by SafetyKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SafetyKit)*