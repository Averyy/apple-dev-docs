# ProcessInfo

**Framework**: Foundation  
**Kind**: class

A collection of information about the current process.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class ProcessInfo
```

#### Overview

Each process has a single, shared [`ProcessInfo`](processinfo.md) object known as a  that can return information such as arguments, environment variables, host name, and process name. The [`processInfo`](processinfo/processinfo.md) class method returns the shared agent for the current process. For example, the following line returns the [`ProcessInfo`](processinfo.md) object, which then provides the name of the current process:

> **Note**:  [`ProcessInfo`](processinfo.md) is thread-safe in macOS 10.7 and later.

The [`ProcessInfo`](processinfo.md) class also includes the [`operatingSystemVersion`](processinfo/operatingsystemversion.md) property, which returns an [`OperatingSystemVersion`](operatingsystemversion.md) structure identifying the operating system version on which the process is executing.

[`ProcessInfo`](processinfo.md) objects attempt to interpret environment variables and command-line arguments in the user’s default C string encoding if they can’t convert to Unicode as UTF-8 strings. If neither the Unicode nor C string conversion works, the [`ProcessInfo`](processinfo.md) object ignores these values.

##### Manage Activities

The system has heuristics to improve battery life, performance, and responsiveness of applications for the benefit of the user. You can use the following methods to manage  that give hints to the system that your application has special requirements:

- [`beginActivity(options:reason:)`](processinfo/beginactivity(options:reason:).md)
- [`endActivity(_:)`](processinfo/endactivity(_:).md)
- [`performActivity(options:reason:using:)`](processinfo/performactivity(options:reason:using:).md)

In response to creating an activity, the system disables some or all of the heuristics so your application can finish quickly while still providing responsive behavior if the user needs it.

You use activities when your application performs a long-running operation. If the activity can take different amounts of time (for example, calculating the next move in a chess game), it should use this API to ensure correct behavior when the amount of data or the capabilities of the user’s computer varies. Activities fall into two major categories:

-  activities are explicitly started by the user. Examples include exporting or downloading a user-specified file.
-  activities perform the normal operations of your application and aren’t explicitly started by the user. Examples include autosaving, indexing, and automatic downloading of files.

In addition, if your application requires high priority input/output (I/O), you can include the [`latencyCritical`](processinfo/activityoptions/latencycritical.md) flag (using a bitwise `OR`). You should only use this flag for activities like audio or video recording that require high priority I/O.

If your activity takes place synchronously inside an event callback on the main thread, you don’t need to use this API.

Be aware that failing to end these activities for an extended period of time can have significant negative impacts on the performance of your user’s computer, so be sure to use only the minimum amount of time required. User preferences may override your application’s request.

You can also use this API to control automatic termination or sudden termination (see [`Support Sudden Termination`](processinfo#Support-Sudden-Termination.md)). For example, the following code brackets the work to protect it from sudden termination:

The above example is equivalent to the following code, which uses the [`disableAutomaticTermination(_:)`](processinfo/disableautomatictermination(_:).md) method:

Because this API returns an object, it may be easier to pair begins and ends than when using the automatic termination API. If your app deallocates the object before the [`endActivity(_:)`](processinfo/endactivity(_:).md) call, the activity ends automatically.

This API also provides a mechanism to disable system-wide idle sleep and display idle sleep. These can have a large impact on the user experience, so be careful to end activities that disable sleep (including [`userInitiated`](processinfo/activityoptions/userinitiated.md)).

##### Support Sudden Termination

macOS 10.6 and later includes a mechanism that allows the system to log out or shut down more quickly by, whenever possible, killing applications instead of requesting that they quit themselves.

Your application can enable this capability on a global basis and then manually override its availability during actions that could cause data corruption or a poor user experience by allowing sudden termination.

Alternatively, your application can manually enable and disable this functionality. Creating a process assigns a counter that indicates if the process is safe to terminate. You decrement and increment the counter using the methods [`enableSuddenTermination()`](processinfo/enablesuddentermination().md) and [`disableSuddenTermination()`](processinfo/disablesuddentermination().md). A value of `0` enables the system to terminate the process without first sending a notification or event.

Your application can support sudden termination upon launch by adding a key to the application’s `Info.plist` file. If the [`NSSupportsSuddenTermination`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSupportsSuddenTermination) key exists in the `Info.plist` file and has a value of [`true`](https://developer.apple.com/documentation/swift/true), it’s the equivalent of calling [`enableSuddenTermination()`](processinfo/enablesuddentermination().md) during your application launch. This allows the system to terminate the process immediately. You can still override this behavior by invoking [`disableSuddenTermination()`](processinfo/disablesuddentermination().md).

Typically, you disable sudden termination whenever your app defers work that the app must complete before it terminates. If, for example, your app defers writing data to disk and enables sudden termination, you should bracket the sensitive operations with a call to [`disableSuddenTermination()`](processinfo/disablesuddentermination().md), perform the necessary operations, and then send a balancing [`enableSuddenTermination()`](processinfo/enablesuddentermination().md) message.

In agents or daemon executables that don’t depend on AppKit, you can manually invoke [`enableSuddenTermination()`](processinfo/enablesuddentermination().md) right away. You can then use the enable and disable methods whenever the process has work it must do before it terminates.

Some AppKit functionality automatically disables sudden termination on a temporary basis to ensure data integrity.

- [`UserDefaults`](userdefaults.md) temporarily disables sudden termination to prevent the process from terminating between the time at which it sets the default and the time at which it writes the preferences file — including that default — to disk.
- [`NSDocument`](https://developer.apple.com/documentation/AppKit/NSDocument) temporarily disables sudden termination to prevent the process from terminating between the time at which the user has made a change to a document and the time at which [`NSDocument`](https://developer.apple.com/documentation/AppKit/NSDocument) writes the user’s change to disk.

> 💡 **Tip**:  You can determine the value of the sudden termination using the following LLDB command. ```objc
print (long)[[NSClassFromString(@"NSProcessInfo") processInfo] _suddenTerminationDisablingCount]
``` Don’t attempt to invoke or override `suddenTerminationDisablingCount` (a private method) in your application. It’s there for this debugging purpose and may disappear at any time.

##### Monitor Thermal State to Adjust App Performance

 indicates the level of heat generated by logic components as they run apps. As the thermal state increases, the system decreases heat by reducing the speed of the processors. Optimize your app’s performance by monitoring the thermal state and reducing system usage as the thermal state increases. Query the current state with [`thermalState`](processinfo/thermalstate-swift.property.md) to determine if your app needs to reduce system usage. You can register the [`thermalStateDidChangeNotification`](processinfo/thermalstatedidchangenotification.md) for notifications of a change in thermal state. For recommended actions, see [`ProcessInfo.ThermalState`](processinfo/thermalstate-swift.enum.md).

## Topics

### Getting the Process Information Agent
- [class var processInfo: ProcessInfo](processinfo/processinfo.md)
  Returns the process information agent for the process.
### Accessing Process Information
- [var arguments: [String]](processinfo/arguments.md)
  Array of strings with the command-line arguments for the process.
- [var environment: [String : String]](processinfo/environment.md)
  The variable names (keys) and their values in the environment from which the process was launched.
- [var globallyUniqueString: String](processinfo/globallyuniquestring.md)
  Global unique identifier for the process.
- [var isMacCatalystApp: Bool](processinfo/ismaccatalystapp.md)
  A Boolean value that indicates whether the process originated as an iOS app and runs on macOS.
- [var isiOSAppOnMac: Bool](processinfo/isiosapponmac.md)
  A Boolean value that indicates whether the process is an iPhone or iPad app running on a Mac.
- [var processIdentifier: Int32](processinfo/processidentifier.md)
  The identifier of the process (often called process ID).
- [var processName: String](processinfo/processname.md)
  The name of the process.
### Accessing User Information
- [var userName: String](processinfo/username.md)
  Returns the account name of the current user.
- [var fullUserName: String](processinfo/fullusername.md)
  Returns the full name of the current user.
### Sudden Application Termination
- [func disableSuddenTermination()](processinfo/disablesuddentermination.md)
  Disables the application for quickly killing using sudden termination.
- [func enableSuddenTermination()](processinfo/enablesuddentermination.md)
  Enables the application for quick killing using sudden termination.
### Controlling Automatic Termination
- [func disableAutomaticTermination(String)](processinfo/disableautomatictermination(_:).md)
  Disables automatic termination for the application.
- [func enableAutomaticTermination(String)](processinfo/enableautomatictermination(_:).md)
  Enables automatic termination for the application.
- [var automaticTerminationSupportEnabled: Bool](processinfo/automaticterminationsupportenabled.md)
  A Boolean value indicating whether the app supports automatic termination.
### Getting Host Information
- [var hostName: String](processinfo/hostname.md)
  The name of the host computer on which the process is executing.
- [var operatingSystemVersionString: String](processinfo/operatingsystemversionstring.md)
  A string containing the version of the operating system on which the process is executing.
- [var operatingSystemVersion: OperatingSystemVersion](processinfo/operatingsystemversion.md)
  The version of the operating system on which the process is executing.
- [func isOperatingSystemAtLeast(OperatingSystemVersion) -> Bool](processinfo/isoperatingsystematleast(_:).md)
  Returns a Boolean value indicating whether the version of the operating system on which the process is executing is the same or later than the given version.
- [func operatingSystem() -> Int](processinfo/operatingsystem.md)
  Returns a constant to indicate the operating system on which the process is executing.
- [func operatingSystemName() -> String](processinfo/operatingsystemname.md)
  Returns a string containing the name of the operating system on which the process is executing.
### Getting Computer Information
- [var processorCount: Int](processinfo/processorcount.md)
  The number of processing cores available on the computer.
- [var activeProcessorCount: Int](processinfo/activeprocessorcount.md)
  The number of active processing cores available on the computer.
- [var physicalMemory: UInt64](processinfo/physicalmemory.md)
  The amount of physical memory on the computer in bytes.
- [func isDeviceCertified(for: NSDeviceCertification) -> Bool](processinfo/isdevicecertified(for:).md)
  Indicates whether the device supports the requested performance tier.
- [func hasPerformanceProfile(NSProcessPerformanceProfile) -> Bool](processinfo/hasperformanceprofile(_:).md)
  Indicates whether an app is running under a known performance profile.
- [var systemUptime: TimeInterval](processinfo/systemuptime.md)
  The amount of time the system has been awake since the last time it was restarted.
### Managing Activities
- [func beginActivity(options: ProcessInfo.ActivityOptions, reason: String) -> any NSObjectProtocol](processinfo/beginactivity(options:reason:).md)
  Begin an activity using the given options and reason.
- [func endActivity(any NSObjectProtocol)](processinfo/endactivity(_:).md)
  Ends the given activity.
- [func performActivity(options: ProcessInfo.ActivityOptions, reason: String, using: () -> Void)](processinfo/performactivity(options:reason:using:).md)
  Synchronously perform an activity defined by a given block using the given options.
- [func performExpiringActivity(withReason: String, using: (Bool) -> Void)](processinfo/performexpiringactivity(withreason:using:).md)
  Performs the specified block asynchronously and notifies you if the process is about to be suspended.
### Getting the Thermal State
- [var thermalState: ProcessInfo.ThermalState](processinfo/thermalstate-swift.property.md)
  The current thermal state of the system.
### Determining Whether Low Power Mode is Enabled
- [var isLowPowerModeEnabled: Bool](processinfo/islowpowermodeenabled.md)
  A Boolean value that indicates the current state of Low Power Mode.
### Constants
- [struct OperatingSystemVersion](operatingsystemversion.md)
  A structure that contains version information about the currently executing operating system, including major, minor, and patch version numbers.
- [ProcessInfo.ActivityOptions](processinfo/activityoptions.md)
  Option flags used with [`beginActivity(options:reason:)`](processinfo/beginactivity(options:reason:).md) and [`performActivity(options:reason:using:)`](processinfo/performactivity(options:reason:using:).md).
- [ProcessInfo.ThermalState](processinfo/thermalstate-swift.enum.md)
  Values used to indicate the system’s thermal state.
- [Anonymous](1552984-anonymous.md)
  The following constants are provided by the `NSProcessInfo` class as return values for [`operatingSystem()`](processinfo/operatingsystem().md).
### Notifications
- [class let thermalStateDidChangeNotification: NSNotification.Name](processinfo/thermalstatedidchangenotification.md)
  Posts when the thermal state of the system changes.
- [static let NSProcessInfoPowerStateDidChange: NSNotification.Name](nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange.md)
  Posts when the power state of a device changes.

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
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation/processinfo)*