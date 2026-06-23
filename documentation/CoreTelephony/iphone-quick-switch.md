# iPhone quick switch

**Framework**: Core Telephony

Enable seamless app transition between multiple iPhones.

#### Overview

iPhone quick switch enables your app to receive notifications from the system when someone activates a iPhone as their currently active device for a specific phone number or queries the system about a device’s current state.

> ❗ **Important**: Quick switch signals to your app that it needs to transition active services, such as login credentials and persistent state from a formerly active iPhone to a newly active iPhone. To ensure a high quality user experience, your app, as well as its supporting services need to handle this transition seamlessly, and keep track of both active and passive devices to ensure people aren’t locked out of services your app provides.

There are two ways adopt iPhone quick switching:

- Create a [`CTQuickSwitchManager`](ctquickswitchmanager.md) object, and, optionally, subscribe to the [`CTQuickSwitchManager.Delegate`](ctquickswitchmanager/delegate-swift.protocol.md) protocol to receive notification state changes.
- Query the a device’s `CTQuickSwitch` state directly.

The following example shows how to create a `CTQuickSwitchManager`, register and de-register for events, check the quick switch state for a specific phone number, and check the device’s current state.

**Swift**:

```swift
    
// Create an instance of the `CTQuickSwitchManager` and set the `delegate`.
let manager = CTQuickSwitchManager()
manager.delegate = self // assuming self conforms to CTQuickSwitchManager.Delegate

// Check the QuickSwitch state of a specific phone number.
manager.phoneNumberState(for: "5550") { state, error in
    if let error {
        // handle the error.
        return
    }
    switch state {
        case .active:
        // This device is active.
        case .passive:
        // This device is passive.
        case .notEnrolled:
        // Quick switching isn't configured for this number.
        case .failed:
        fallthrough
        @unknown default:
        break
    }
}

// Check the overall device QuickSwitch state.
manager.getDeviceState { state, error in
    if let error {
        // handle the error.
        return
    }
    if state == .passive {
        // Device is passive.
    }
}

// Register for background launch on QuickSwitch state changes.
CTQuickSwitchManager.registerForLaunchOnQuickSwitchStateEvents { error in
    if let error {
        // Handle the error — app may not be eligible.
        return
    }
    // Successfully registered; the system will wake app in the background on state changes.
}

// Unregister from background launch on QuickSwitch state changes.
CTQuickSwitchManager.unregisterForLaunchOnQuickSwitchStateEvents { error in
    if let error {
        // handle the error.
        return
    }
    // Successfully unregistered
}
```

**Objective-C**:

```objective-c
// Create an instance and optionally set a delegate to receive state change notifications.
CTQuickSwitchManager *manager = [[CTQuickSwitchManager alloc] init];
manager.delegate = self; // self conforms to `CTQuickSwitchManagerDelegate`.
// Check the quick switch state of a specific phone number.
[manager getPhoneNumberStateForSuffix:@"5550" completion:^(CTQuickSwitchState state, NSError * _Nullable error) {
    if (error) {
        // handle the error.
        return;
    }
    switch (state) {
        case CTQuickSwitchStateActive:
            // This device is active.
            break;
        case CTQuickSwitchStatePassive:
            // This device is passive.
            break;
        case CTQuickSwitchStateNotEnrolled:
            // Quick switching isn't configured for this number.
            break;
        case CTQuickSwitchStateFailed:
        default:
            break;
    }
}];
// Check the overall device QuickSwitch state
[manager getDeviceState:^(CTQuickSwitchState state, NSError * _Nullable error) {
    if (error) {
        // handle the error.
        return;
    }
    if (state == CTQuickSwitchStatePassive) {
        // Device is passive.
    }
}];

    // Implement a delegate callback for state changes.
    - (void)quickSwitchManager:(CTQuickSwitchManager *)quickSwitchManager didChangeToState:(CTQuickSwitchState)state {
        // Handle the updated state.
    }

    // Registering for background launch on QuickSwitch state changes.
    [CTQuickSwitchManager registerForLaunchOnQuickSwitchStateEvents:^(NSError * _Nullable error) {
        if (error) {
            // handle error — app may not be eligible.
            return;
        }
        // Successfully registered; the system will wake the app in the background on state changes.
    }];

    // Unregistering from background launch on QuickSwitch state changes.
    [CTQuickSwitchManager unregisterForLaunchOnQuickSwitchStateEvents:^(NSError * _Nullable error) {
        if (error) {
            // handle the error.
            return;
        }
        // Successfully unregistered.
    }];

```

The following examples show how to create a `CTQuickSwitchManager`, register and de-register for events, check the quick switch state for a specific phone number, and check the device’s current state using asynchronous calls in Swift.

```swift
    // Create an instance of the `CTQuickSwitchManager` and set the delegate.
    let manager = CTQuickSwitchManager()
    manager.delegate = self // Assuming `self` conforms to `CTQuickSwitchManager.Delegate`

    // Check the QuickSwitch state of a specific phone number.
    let state = try await manager.phoneNumberState(for: "5550")
    switch state {
        case .active:
        // This device is active.
        case .passive:
        // This device is passive.
        case .notEnrolled:
        // QuickSwitch is not configured for this number.
        case .failed:
        fallthrough
        @unknown default:
        break
    }
    
    // Check the overall device QuickSwitch state.
    let deviceState = try await manager.deviceState
    if deviceState == .passive {
        // Device is passive.
    }

    // Register for quick switch state events.
    if let _ = try? await CTQuickSwitchManager.registerForLaunchOnQuickSwitchStateEvents()  {
        print("Registration successful.")
    } else {
        print("Registration failed.")
    }

    
    // Un-register for quick switch state events.
    if let _ = try? await CTQuickSwitchManager.unregisterForLaunchOnQuickSwitchStateEvents() {
        print("De-registration successful.")
    } else {
        print("App wasn't registered for launch on quick switch events.")
    }
    
    // Implement the delegate callback to receive state changes.
    func quickSwitchManager(_ manager: CTQuickSwitchManager, didChangeToState state: CTQuickSwitchManager.State) {
        // Handle the updated state.
    }        
    
```

## Topics

### Adopting iPhone quick switch
- [class CTQuickSwitchManager](ctquickswitchmanager.md)
  An object that enables an app to register and query a device’s quick switch state.
- [var delegate: (any CTQuickSwitchManager.Delegate)?](ctquickswitchmanager/delegate-swift.property.md)
  An object the system notifies to respond to quick switch events.
- [CTQuickSwitchManager.Delegate](ctquickswitchmanager/delegate-swift.protocol.md)
  Methods you implement to respond to changes in a device’s quick switch state.
### Registering and unregistering for quick switch events
- [class func registerForLaunch(onQuickSwitchStateEvents: ((any Error)?) -> Void)](ctquickswitchmanager/registerforlaunch(onquickswitchstateevents:).md)
  Registers the calling app for background launch whenever the device’s quick switch state changes.
- [class func unregisterForLaunch(onQuickSwitchStateEvents: ((any Error)?) -> Void)](ctquickswitchmanager/unregisterforlaunch(onquickswitchstateevents:).md)
  Removes the calling app’s registration for background launch on quick switch state changes.
### Responding to quick switch state changes
- [func quickSwitchManager(CTQuickSwitchManager, didChangeTo: CTQuickSwitchState)](ctquickswitchmanager/delegate-swift.protocol/quickswitchmanager(_:didchangeto:).md)
  Indicates there’s been a change in device’s quick switch state.
### Checking the state of a device
- [func getDeviceState((CTQuickSwitchState, (any Error)?) -> Void)](ctquickswitchmanager/getdevicestate(_:).md)
  Gets the quick switch state of the current device.
- [func getPhoneNumberState(forSuffix: String, completion: (CTQuickSwitchState, (any Error)?) -> Void)](ctquickswitchmanager/getphonenumberstate(forsuffix:completion:).md)
  Queries the quick switch state for a phone number whose suffix matches the provided phone number suffix.
- [enum CTQuickSwitchState](ctquickswitchstate.md)
  Values that describe a device’s quick switch status.

## See Also

- [class CTTelephonyNetworkInfo](cttelephonynetworkinfo.md)
  An object that provides notifications of changes to the user’s cellular service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/iphone-quick-switch)*