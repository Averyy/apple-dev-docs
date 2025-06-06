# Supporting live updates in SwiftUI and Mac Catalyst apps

**Framework**: Core Location

Enable background events by adding lifecycle event support.

#### Overview

In iOS 17 and later, Core Location supports live updates using Swift concurrency’s async/await capability. In order to adopt live updates, SwiftUI and Mac Catalyst apps need to implement lifecycle event support that enables an app’s `@main app` to have explicit support for the creation and resumption of background run-loops. This enables the system to deliver Core Location events to the app and allows the delivery of events to resume in the event of return from background, launch of the app, or relaunch after a crash.

##### Adding Lifecycle Events to Swiftui

To add support for life cycle events, you need to add three components to your app:

1. A shared state using an [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) that maintains instances of [`CLLocationManager`](cllocationmanager.md) and [`CLBackgroundActivitySession`](clbackgroundactivitysession-3mzv3.md)
2. An `AppDelegate` object that provides the [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didFinishLaunchingWithOptions:)) method that handles resuming background activities on return from background or an app relaunch
3. An `AppDelegate` object in the SwiftUI or Mac Catalyst app’s `@main` structure

In your SwiftUI or Mac Catalyst App, add support for the `AppDelegate` by adding a shared state through an [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject), and a [`UIApplicationDelegateAdaptor`](https://developer.apple.com/documentation/SwiftUI/UIApplicationDelegateAdaptor) as an object the app’s `@main` structure maintains, as shown in the following example:

```swift
    import SwiftUI

    // Shared state that manages the `CLLocationManager` and `CLBackgroundActivitySession`.
    @MainActor class LocationsHandler: ObservableObject {
    
        static let shared = LocationsHandler()  // Create a single, shared instance of the object.
        private let manager: CLLocationManager
        private var background: CLBackgroundActivitySession?

        @Published var lastLocation = CLLocation()
        @Published var isStationary = false
        @Published var count = 0
    
        @Published
        var updatesStarted: Bool = UserDefaults.standard.bool(forKey: "liveUpdatesStarted") {
            didSet { UserDefaults.standard.set(updatesStarted, forKey: "liveUpdatesStarted") }
        }
    
        @Published
        var backgroundActivity: Bool = UserDefaults.standard.bool(forKey: "BGActivitySessionStarted") {
            didSet {
                backgroundActivity ? self.background = CLBackgroundActivitySession() : self.background?.invalidate()
                UserDefaults.standard.set(backgroundActivity, forKey: "BGActivitySessionStarted")
            }
        }
    
    
        private init() {
            self.manager = CLLocationManager()  // Creating a location manager instance is safe to call here in `MainActor`.
        }
    
        func startLocationUpdates() {
            if self.manager.authorizationStatus == .notDetermined {
                self.manager.requestWhenInUseAuthorization()
            }
            self.logger.info("Starting location updates")
            Task() {
                do {
                    self.updatesStarted = true
                    let updates = CLLocationUpdate.liveUpdates()
                    for try await update in updates {
                        if !self.updatesStarted { break }  // End location updates by breaking out of the loop.
                        if let loc = update.location {
                            self.lastLocation = loc
                            self.isStationary = update.isStationary
                            self.count += 1
                            print("Location \(self.count): \(self.lastLocation)")
                        }
                    }
                } catch {
                    print("Could not start location updates")
                }
                return
            }
        }
    
        func stopLocationUpdates() {
            print("Stopping location updates")
            self.updatesStarted = false
            self.updatesStarted = false
        } 
    }
```

Next, create an instance of a UIKit `AppDelegate` class that conforms to SwiftUI’s [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) protocol; this enables the `AppDelegate` to participate in the SwiftUI’s app-level shared state and manages the resumption of Core Location activities when needed.

```swift
    import Foundation
    import UIKit

    class AppDelegate: NSObject, UIApplicationDelegate, ObservableObject {   
    
        func application(_ application: UIApplication, didFinishLaunchingWithOptions
                         launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil) -> Bool {
            let locationsHandler = LocationsHandler.shared
        
            // If location updates were previously active, restart them after the background launch.
            if locationsHandler.updatesStarted {
                locationsHandler.startLocationUpdates()
            }
            // If a background activity session was previously active, reinstantiate it after the background launch.
            if locationsHandler.backgroundActivity {
                locationsHandler.backgroundActivity = true
            }
            return true
        }
    }
```

Finally, include the `AppDelegate` functionality in your app’s `@main` structure using a [`UIApplicationDelegateAdaptor`](https://developer.apple.com/documentation/SwiftUI/UIApplicationDelegateAdaptor):

```swift
    @main
    struct MyApp: App {
        @UIApplicationDelegateAdaptor private var appDelegate: AppDelegate
        var body: some Scene {
            WindowGroup {
                ContentView()
            }
        }
    }
```

## See Also

- [Configuring your app to use location services](configuring-your-app-to-use-location-services.md)
  Prepare your app to start collecting location data.
- [class CLLocationManager](cllocationmanager.md)
  The object you use to start and stop the delivery of location-related events to your app.
- [class CLBackgroundActivitySession](clbackgroundactivitysession-3mzv3.md)
  An object that manages a visual indicator that keeps your app in use in the background, allowing it to receive updates or events.
- [struct CLLocationUpdate](cllocationupdate.md)
  A structure that contains the location information the framework delivers with each update.
- [Adopting live updates in Core Location](adopting-live-updates-in-core-location.md)
  Simplify location delivery using asynchronous events in Swift.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md)
  Define boundaries and act on user location updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/supporting-live-updates-in-swiftui-and-mac-catalyst-apps)*