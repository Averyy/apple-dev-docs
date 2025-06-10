# CMFallDetectionManager

**Framework**: Core Motion  
**Kind**: class

An object for managing fall detection events.

**Availability**:
- watchOS 7.2+

## Declaration

```swift
class CMFallDetectionManager
```

#### Overview

In Series 4 and later, Apple Watch can detect when a wearer falls, and contact emergency services if necessary. Using the `CMFallDetectionManager`, your app can request the user’s authorization, and set up a delegate to receive notifications about these . For more information, see [`Use fall detection with Apple Watch`](https://developer.apple.comhttps://support.apple.com/en-us/HT208944).

> ❗ **Important**:  To use this API, you must include the [`NSFallDetectionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSFallDetectionUsageDescription) key in your app’s `Info.plist` file and provide a usage description string for the key. The description appears in the prompt that the user receives when the system asks to access fall detection data for your app. If you don’t include a usage description string, your app crashes when you call this API.

`CMFallDetectionManager` requires an entitlement from Apple. To apply for the entitlement, see [`Fall Detection Entitlement Request`](https://developer.apple.comhttps://developer.apple.com/contact/request/fall-detection-api). This entitlement allows the app to run in the background without requiring any additional capabilities. However, you can add capabilities for other background modes, as needed by your app.

There are two approaches to detecting falls in your app. You can either query for [`numberOfTimesFallen`](https://developer.apple.com/documentation/HealthKit/HKQuantityTypeIdentifier/numberOfTimesFallen) samples in HealthKit, or you can use Core Motion’s `CMFallDetectionManager`.

##### Detect and Respond to Falls

The Core Motion fall detection manager is particularly useful for apps that need to respond to falls in a timely manner so that the app can provide help to the person who fell.

The fall detection manager:

- Notifies the app in real time
- Notifies the app of all fall events
- Provides background runtime so that your app can respond to the fall

##### Detect and Monitor Falls Over Time

The HealthKit sample is particularly useful for apps that monitor falls over longer time periods, because there can be a delay between the fall event and HealthKit updating its samples.

HealthKit provides:

- Samples that are available on all devices that can access the person’s HealthKit data—not just the device that detected the fall
- Samples for falls where the person who fell confirmed the fall, or the system escalated the fall to emergency services. If the person who fell dismisses the fall alert, HealthKit doesn’t record the fall.

##### Create the Manager

To receive fall detection notifications, ensure that the feature is available on the current device. If the feature is available, create the manager and set its delegate.

```swift
if CMFallDetectionManager.isAvailable  {
    
    // Create the manager.
    let manager = CMFallDetectionManager()
    
    // Assign a delegate that adopts the CMFallDetectionDelegte protocol.
    manager.delegate = myDelegate
    
    // Keep a reference to the manager.
    myManager = manager
}
```

Set the delegate as early as possible, ideally in your extension delegate’s [`applicationDidFinishLaunching()`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/applicationDidFinishLaunching()) method. The system may not instantiate your app’s user interface when launching your app in the background, so you can’t set the delegate from your user interface code, such as when an interface controller activates, or in response to a change in SwiftUI’s [`ScenePhase`](https://developer.apple.com/documentation/SwiftUI/ScenePhase) state.

> ❗ **Important**:  Create only a single instance of the detection manager. Store the manager in a variable so you can access it later. Be sure to use a variable that remains in memory throughout your app’s lifetime—for example, add the variable to your extension delegate.

##### Request User Authorization

After your user interface loads, check if you previously requested approval. If you haven’t, call [`requestAuthorization(handler:)`](cmfalldetectionmanager/requestauthorization(handler:).md) to initiate a request.

```swift
// Check to see if you have already asked the user to
// authorize fall detection event notifications.
if myManager?.authorizationStatus == .notDetermined {
    
    // Request Authorization.
    myManager?.requestAuthorization { (authorizationStatus) in
        
        // Respond to the authorization status.
    }
}
```

Your delegate only receives fall detection event notifications if the user authorizes your app. The user can change your app’s authorization state at any time from Settings > Privacy > Fall Detection.

After you set the delegate and the user grants authorization, your app checks for recent fall events. If the system finds an event, it calls your delegate’s [`fallDetectionManager(_:didDetect:completionHandler:)`](cmfalldetectiondelegate/falldetectionmanager(_:diddetect:completionhandler:).md) method and passes the most recent event. On subsequent launches, as long as your app remains authorized and the system has detected a recent fall event, the system calls `fallDetectionManager(_:didDetect:completionHandler:)` as soon as you set the delegate.

The system also wakes your app in the background to respond to any new fall detection events. The system only gives your app a short amount of time to respond to the event and call the completion handler. If the app exceeds the allotted time, the system may suspend it.

## Topics

### Checking Availability
- [class var isAvailable: Bool](cmfalldetectionmanager/isavailable.md)
  A Boolean value that indicates whether the current device supports fall detection.
### Requesting Authorization
- [func requestAuthorization(handler: (CMAuthorizationStatus) -> Void)](cmfalldetectionmanager/requestauthorization(handler:).md)
  Requests authorization to receive notifications about fall detection events.
- [var authorizationStatus: CMAuthorizationStatus](cmfalldetectionmanager/authorizationstatus.md)
  The authorization status for receiving fall detection event notifications.
- [enum CMAuthorizationStatus](cmauthorizationstatus.md)
  The authorization status for motion-related features.
### Handling Events
- [var delegate: (any CMFallDetectionDelegate)?](cmfalldetectionmanager/delegate.md)
  A delegate that can receive notifications about fall detection events.
- [protocol CMFallDetectionDelegate](cmfalldetectiondelegate.md)
  A delegate that receives information about fall detection events and authorization status changes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol CMFallDetectionDelegate](cmfalldetectiondelegate.md)
  A delegate that receives information about fall detection events and authorization status changes.
- [class CMFallDetectionEvent](cmfalldetectionevent.md)
  An object that contains data about a fall detection event.
- [NSFallDetectionUsageDescription](../BundleResources/Information-Property-List/NSFallDetectionUsageDescription.md)
  A message to the user that explains the app’s request for permission to access fall detection event data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager)*