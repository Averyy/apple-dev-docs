# Discovering app extensions from your app

**Framework**: ExtensionFoundation

Find the app extensions that match your host app’s extension points and are available to use.

#### Overview

At runtime, apps rely on the system to provide the list of app extensions available for them to use. The system starts by looking for app extensions that support the host app’s extension points. It then determines which of those app extensions are enabled and ready to use. For security, the system disables app extensions that ship outside of the host app by default. The owner of the device can also disable app extensions using system-provided interfaces.

For each available app extension, the system provides an [`AppExtensionIdentity`](appextensionidentity.md) structure for you to launch that extension. This identity structure contains the name of the app extension, the name of the supported extension point, and the host app’s bundle identifier.

##### Retrieve the Current List of Available App Extensions

To retrieve the available app extensions for your app, create a [`AppExtensionPoint.Monitor`](appextensionpoint/monitor.md) type. A monitor provides two ways to access the available app extensions:

- The [`identities`](appextensionpoint/monitor/identities.md) property contains a snapshot of the app extensions currently available for you to use.
- The [`state`](appextensionpoint/monitor/state-swift.property.md) property contains the list of available app extensions and the number of disabled and unapproved app extensions.

To configure a monitor, initialize the [`AppExtensionPoint.Monitor`](appextensionpoint/monitor.md) type with one of your app’s extension points. To monitor additional extension points from the same instance, call the [`addAppExtensionPoint(_:)`](appextensionpoint/monitor/addappextensionpoint(_:).md) method. The creation of a monitor is an asynchronous operation. During creation, the system finds and validates the list of available app extensions. As soon as this process finishes, the system returns the initialized type to your code. As a result, you can fetch the list of app extensions immediately upon receiving the type, as shown in the following example:

```swift
// Get one of the app's defined AppExtensionPoint types.
let someExtensionPoint = AppExtensionPoint.myExampleExtensionPoint

// Get a snapshot of the available app extension identities.
let identitiesSnapshot = try await AppExtensionPoint.Monitor(someExtensionPoint).identities
```

The [`ExtensionKit`](https://developer.apple.com/documentation/ExtensionKit) framework contains a view controller that shows all of the known app extensions for your app, including ones that are disabled. Present this view controller from your interface to give people a way to enable and disable app extensions. For information about how to show this interface, see [`Displaying the app extensions available to your app`](https://developer.apple.com/documentation/ExtensionKit/displaying-the-app-extensions-available-to-your-app).

##### Detect Changes to the List of Available App Extensions

If your app supports app extensions from external developers, the list of available app extensions can change as someone installs or removes apps on their device. At app installation time, the system records the presence of its app extensions and associates them with the matching host app. The system similarly updates its records when someone removes an app. If your app is running when these changes occur, the system reports those changes to any active monitors.

To detect changes to app extensions, use the [`Observation`](https://developer.apple.com/documentation/Observation) framework to track changes to the [`identities`](appextensionpoint/monitor/identities.md) or [`state`](appextensionpoint/monitor/state-swift.property.md) properties of your monitor. Both properties support observation, which you can use to create an [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) of updates. The following code creates such a sequence for the [`identities`](appextensionpoint/monitor/identities.md) property, and then monitors that sequence asynchronously. As updates arrive, the task runs and delivers the new set of [`AppExtensionIdentity`](appextensionidentity.md) structures to the `update` variable.

```swift
let monitor = AppExtensionPoint.Monitor(appExtensionPoint:someExtensionPoint)

let identitiesUpdates = Observations { monitor.identities }
Task { 
    for await update in identitiesUpdates {
        // Process the new list of app extension identities.
    }
}
```

In addition to reporting the installation or removal of app extensions on the system, a monitor also reports changes to the status of an existing app extension. The [`identities`](appextensionpoint/monitor/identities.md) and [`state`](appextensionpoint/monitor/state-swift.property.md) properties contain only the app extensions that are installed and currently enabled. If someone enables or disables one of those app extensions, the monitor updates those lists to reflect the change.

## See Also

- [struct AppExtensionProcess](appextensionprocess.md)
  A type the host app creates to launch and manage an app extension.
- [struct AppExtensionIdentity](appextensionidentity.md)
  A type that uniquely identifies an app extension on the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/discovering-app-extensions-from-your-app)*