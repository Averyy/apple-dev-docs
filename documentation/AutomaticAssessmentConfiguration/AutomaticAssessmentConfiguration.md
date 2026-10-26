# Automatic Assessment Configuration

**Framework**: Automatic Assessment Configuration  
**Kind**: module  
**Role**: Framework

Enter single-app mode and prevent students from accessing specific system features while taking an exam.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+

#### Overview

Use the AutomaticAssessmentConfiguration framework to create an assessment session that limits access to system features. The session prevents a user from using the device to retrieve information beyond that which your app provides, or distributing sensitive information from within your app. This limited access helps you protect the integrity of an assessment, like an exam, conducted by your app.

Apps that use the AutomaticAssessmentConfiguration framework must have the [`com.apple.developer.automatic-assessment-configuration`](../BundleResources/entitlements/com.apple.developer.automatic-assessment-configuration.md) entitlement. With the entitlement set, use an instance of the [`AEAssessmentSession`](./aeassessmentsession.md) class to start and stop assessment sessions.

A session provides protections by preventing access to desktop elements like:

- The Dock
- The Application Menu Bar
- Mission Control
- Notification Center
- Spaces other than the current one
- Other apps, except those that you selectively allow

Additionally, a session:

- Prevents screen recording and screen capture
- Disables Siri
- Stops media playing
- Allows network access for only your app
- Disables Handoff
- Clears the pasteboard buffer when starting and stopping the session

> **Note**:  If you publish an educational app that delivers exams to students, you can request permission to use the [`com.apple.developer.automatic-assessment-configuration`](../BundleResources/entitlements/com.apple.developer.automatic-assessment-configuration.md) entitlement by filling in the [Automatic Assessment Configuration Entitlement Request](https://developer.apple.com/contact/request/automatic-assessment-configuration/) form.

The framework reports an error if you try to start an assessment from an app running in visionOS.

## Topics

### Essentials
- [com.apple.developer.automatic-assessment-configuration](../BundleResources/entitlements/com.apple.developer.automatic-assessment-configuration.md)
  A Boolean value that indicates whether an app may create an assessment session.
### Sessions
- [Preparing an educational assessment app for distribution](./preparing-an-educational-assessment-app-for-distribution.md)
  Ensure your app maintains academic integrity by reviewing assessment practices and managing system capabilities.
- [Build an Educational Assessment App](./build-an-educational-assessment-app.md)
  Ensure the academic integrity of your assessment app by using Automatic Assessment Configuration.
- [class AEAssessmentConfiguration](./aeassessmentconfiguration.md)
  Configuration information for an assessment session.
- [class AEAssessmentSession](./aeassessmentsession.md)
  A session that your app uses to protect an assessment.
### Errors
- [struct AEAssessmentError](./aeassessmenterror.md)
  Errors issued by an assessment session to its delegate.
- [AEAssessmentError.Code](./aeassessmenterror/code.md)
  Error codes that the framework returns if a session fails.
- [let AEAssessmentErrorDomain: String](./aeassessmenterrordomain.md)
  A constant representing the error domain that the framework uses when issuing errors.
### Classes
- [class AEAssessmentBinaryExecutable](./aeassessmentbinaryexecutable.md)
  A non-bundled, non-UI executable (e.g. a launchd daemon) designated as an assessment participant by its on-disk path.
- [class AEAssessmentBinaryExecutableConfiguration](./aeassessmentbinaryexecutableconfiguration.md)
  The configuration applied to an [`AEAssessmentBinaryExecutable`](./aeassessmentbinaryexecutable.md) participant.
### Structures
- [struct AEAppleMenuItem](./aeapplemenuitem.md)
  Identifies an item in the Apple menu.
- [struct AEMenuBarItem](./aemenubaritem.md)
  Identifies a menu bar item that can remain visible during an assessment session.
### Enumerations
- [enum AEUserAccountType](./aeuseraccounttype.md)
  Specifies the type of account required for an assessment session.
### Variables
- [AEAppleMenuItemAboutThisMac](./aeapplemenuitem/aboutthismac.md)
  The About This Mac item, which remains visible during an assessment session whether or not [`allowedAppleMenuItems`](./aeassessmentconfiguration/allowedapplemenuitems.md) names it.
- [AEAppleMenuItemAppStore](./aeapplemenuitem/appstore.md)
  The App Store item.
- [AEAppleMenuItemForceQuit](./aeapplemenuitem/forcequit.md)
  The Force Quit item, covering both the Force Quit Applications window and quitting an app outright.
- [AEAppleMenuItemLocation](./aeapplemenuitem/location.md)
  The Location item.
- [AEAppleMenuItemLockScreen](./aeapplemenuitem/lockscreen.md)
  The Lock Screen item.
- [AEAppleMenuItemLogout](./aeapplemenuitem/logout.md)
  The Log Out item, covering both the command and its confirmation.
- [AEAppleMenuItemRecent](./aeapplemenuitem/recent.md)
  The Recent Items item.
- [AEAppleMenuItemRestart](./aeapplemenuitem/restart.md)
  The Restart item, covering both the command and its confirmation.
- [AEAppleMenuItemShutDown](./aeapplemenuitem/shutdown.md)
  The Shut Down item, covering both the command and its confirmation.
- [AEAppleMenuItemSleep](./aeapplemenuitem/sleep.md)
  The Sleep item.
- [AEAppleMenuItemSystemInformation](./aeapplemenuitem/systeminformation.md)
  The System Information item.
- [AEAppleMenuItemSystemSettings](./aeapplemenuitem/systemsettings.md)
  The System Settings item.
- [AEMenuBarItemBattery](./aemenubaritem/battery.md)
  The Battery system menu bar item.
- [AEMenuBarItemBluetooth](./aemenubaritem/bluetooth.md)
  The Bluetooth system menu bar item.
- [AEMenuBarItemClock](./aemenubaritem/clock.md)
  The Clock system menu bar item.
- [AEMenuBarItemDisplays](./aemenubaritem/displays.md)
  The Displays system menu bar item.
- [AEMenuBarItemKeyboard](./aemenubaritem/keyboard.md)
  The Input Menu system menu bar item, which selects keyboard layouts.
- [AEMenuBarItemVolume](./aemenubaritem/volume.md)
  The Volume system menu bar item.
- [AEMenuBarItemWifi](./aemenubaritem/wifi.md)
  The Wi-Fi system menu bar item.
- [AENotInstalledParticipantsKey](./aenotinstalledparticipantskey.md)
- [AERestrictedSystemParticipantsKey](./aerestrictedsystemparticipantskey.md)
### Macros
- [AE_HIDDEN](./ae_hidden.md)
- [AE_VISIBLE](./ae_visible.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AutomaticAssessmentConfiguration)*