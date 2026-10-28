# NotificationCenter.MessageIdentifier

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

An optional identifier to associate a given message with a given type.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol MessageIdentifier
```

## Overview

Implement a `MessageIdentifier` to provide a typed, ergonomic experience at the call point, as described in [SE-0299](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0299-extend-generic-static-member-lookup.md).

For example, given `ExampleMessage` with a `Subject` called `ExampleSubject`:

```swift
extension NotificationCenter.MessageIdentifier where Self == NotificationCenter.BaseMessageIdentifier<ExampleMessage> {
    static var eventDidOccur: Self { .init() }
}
```

This simplifies the call point for clients, as seen here:

```swift
let token = center.addObserver(of: exampleSubject, for: .eventDidOccur) { ... }
```

## Topics

### Declaring the message type
- [associatedtype MessageType](./messageidentifier/messagetype.md)
### Identifying cookie storage messages
- [static var cookiesChanged: NotificationCenter.BaseMessageIdentifier<HTTPCookieStorage.CookiesChangedMessage>](./messageidentifier/cookieschanged.md)
  An identifier for a message about a cookie storage instance’s cookies changing.
### Identifying undo manager messages
- [static var willUndoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.WillUndoChangeMessage>](./messageidentifier/willundochange.md)
  An identifier for a message about an undo manager preparing to perform an undo.
- [static var didUndoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.DidUndoChangeMessage>](./messageidentifier/didundochange.md)
  An identifier for a message about an undo manager having performed an undo.
- [static var willRedoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.WillRedoChangeMessage>](./messageidentifier/willredochange.md)
  An identifier for a message about an undo manager preparing to perform a redo.
- [static var didRedoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.DidRedoChangeMessage>](./messageidentifier/didredochange.md)
  An identifier for a message about an undo manager having performed a redo.
- [static var checkpoint: NotificationCenter.BaseMessageIdentifier<UndoManager.CheckpointMessage>](./messageidentifier/checkpoint.md)
  An identifier for a message about an undo manager reaching a checkpoint.
- [static var didOpenUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.DidOpenUndoGroupMessage>](./messageidentifier/didopenundogroup.md)
  An identifier for a message about an undo manager having opened an undo group.
- [static var willCloseUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.WillCloseUndoGroupMessage>](./messageidentifier/willcloseundogroup.md)
  An identifier for a message about an undo manager preparing to close an undo group.
- [static var didCloseUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.DidCloseUndoGroupMessage>](./messageidentifier/didcloseundogroup.md)
  An identifier for a message about an undo manager having closed an undo group.
### Identifying defaults messages
- [static var didChange: NotificationCenter.BaseMessageIdentifier<UserDefaults.DidChangeMessage>](./messageidentifier/didchange-187tw.md)
  An identifier for a message about a change in a user defaults setting.
- [static var sizeLimitExceeded: NotificationCenter.BaseMessageIdentifier<UserDefaults.SizeLimitExceededMessage>](./messageidentifier/sizelimitexceeded.md)
  An identifier for a message about a user defaults database exceeding its maximum size.
### Identifying metadata query messages
- [static var didStartGathering: NotificationCenter.BaseMessageIdentifier<NSMetadataQuery.DidStartGatheringMessage>](./messageidentifier/didstartgathering.md)
  An identifier for a message about a metadata query that is starting its initial result gathering.
- [static var didFinishGathering: NotificationCenter.BaseMessageIdentifier<NSMetadataQuery.DidFinishGatheringMessage>](./messageidentifier/didfinishgathering.md)
  An identifier for a message about a metadata query that finished its initial result gathering.
### Identifying calendar, date, and time zone messages
- [static var calendarDayChanged: NotificationCenter.BaseMessageIdentifier<Calendar.CalendarDayChangedMessage>](./messageidentifier/calendardaychanged.md)
  An identifier for a message about a change in calendar day.
- [static var systemClockDidChange: NotificationCenter.BaseMessageIdentifier<Date.SystemClockDidChangeMessage>](./messageidentifier/systemclockdidchange.md)
  An identifier for a message about a change in the system clock.
- [static var systemTimeZoneDidChange: NotificationCenter.BaseMessageIdentifier<TimeZone.SystemTimeZoneDidChangeMessage>](./messageidentifier/systemtimezonedidchange.md)
  An identifier for a message about a change in the system time zone.
### Identifying locale messages
- [static var currentLocaleDidChange: NotificationCenter.BaseMessageIdentifier<Locale.CurrentLocaleDidChangeMessage>](./messageidentifier/currentlocaledidchange.md)
  An identifier for a message about a change in current locale.
### Identifying bundle messages
- [static var didLoad: NotificationCenter.BaseMessageIdentifier<Bundle.DidLoadMessage>](./messageidentifier/didload.md)
  An identifier for a message about a bundle dynamically loading a class.
### Identifying process info messages
- [static var powerStateDidChange: NotificationCenter.BaseMessageIdentifier<ProcessInfo.PowerStateDidChangeMessage>](./messageidentifier/powerstatedidchange.md)
  An identifier for a message about a power state change.
- [static var thermalStateDidChange: NotificationCenter.BaseMessageIdentifier<ProcessInfo.ThermalStateDidChangeMessage>](./messageidentifier/thermalstatedidchange.md)
  An identifier for a message about a thermal state change.
- [static var didTerminate: NotificationCenter.BaseMessageIdentifier<Process.DidTerminateMessage>](./messageidentifier/didterminate.md)
  An identifier for a message about a stopped task.
### Identifying file handle messages
- [static var connectionAccepted: NotificationCenter.BaseMessageIdentifier<FileHandle.ConnectionAcceptedMessage>](./messageidentifier/connectionaccepted.md)
  An identifier for a message about a file handle accepting a connection.
- [static var dataAvailable: NotificationCenter.BaseMessageIdentifier<FileHandle.DataAvailableMessage>](./messageidentifier/dataavailable.md)
  An identifier for a message about a file handle having data available for reading.
- [static var readToEndOfFileCompletion: NotificationCenter.BaseMessageIdentifier<FileHandle.ReadToEndOfFileCompletionMessage>](./messageidentifier/readtoendoffilecompletion.md)
  An identifier for a message about a file handle having reached the end of a file or communication channel.
- [static var readCompletion: NotificationCenter.BaseMessageIdentifier<FileHandle.ReadCompletionMessage>](./messageidentifier/readcompletion.md)
  An identifier for a message about a file handle having read the currently available data from a file or communication channel.
### Identifying port messages
- [static var didBecomeInvalid: NotificationCenter.BaseMessageIdentifier<Port.DidBecomeInvalidMessage>](./messageidentifier/didbecomeinvalid.md)
  An identifier for a message about a port becoming invalid.
### Identifying file manager messages
- [static var ubiquityIdentityDidChange: NotificationCenter.BaseMessageIdentifier<FileManager.UbiquityIdentityDidChangeMessage>](./messageidentifier/ubiquityidentitydidchange.md)
  An identifier for a message about a file manager’s ubiquity identity changing.
### Identifying bundle resource request messages
- [static var lowDiskSpace: NotificationCenter.BaseMessageIdentifier<NSBundleResourceRequest.LowDiskSpaceMessage>](./messageidentifier/lowdiskspace.md)
  An identifier for a message about the available disk space getting low.
### Identifying extension messages
- [static var didBecomeActive: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.DidBecomeActiveMessage>](./messageidentifier/didbecomeactive-79dvm.md)
  An identifier for a message about a host app moving from the inactive to the active state.
- [static var willResignActive: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.WillResignActiveMessage>](./messageidentifier/willresignactive-9z4xc.md)
  An identifier for a message about a host app moving from the active to the inactive state.
- [static var didEnterBackground: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.DidEnterBackgroundMessage>](./messageidentifier/didenterbackground-5gdtk.md)
  An identifier for a message about a host app beginning to run in the background.
- [static var willEnterForeground: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.WillEnterForegroundMessage>](./messageidentifier/willenterforeground-p1og.md)
  An identifier for a message about a host app preparing to run in the foreground.
### Identifying UIKit accessibility messages
- [static var switchControlStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.SwitchControlStatusDidChangeMessage>](./messageidentifier/switchcontrolstatusdidchange.md)
- [static var elementFocused: NotificationCenter.BaseMessageIdentifier<UIAccessibility.ElementFocusedMessage>](./messageidentifier/elementfocused.md)
- [static var reduceTransparencyStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.ReduceTransparencyStatusDidChangeMessage>](./messageidentifier/reducetransparencystatusdidchange.md)
- [static var announcementDidFinish: NotificationCenter.BaseMessageIdentifier<UIAccessibility.AnnouncementDidFinishMessage>](./messageidentifier/announcementdidfinish.md)
- [static var boldTextStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.BoldTextStatusDidChangeMessage>](./messageidentifier/boldtextstatusdidchange.md)
- [static var closedCaptioningStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.ClosedCaptioningStatusDidChangeMessage>](./messageidentifier/closedcaptioningstatusdidchange.md)
- [static var darkerSystemColorsStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.DarkerSystemColorsStatusDidChangeMessage>](./messageidentifier/darkersystemcolorsstatusdidchange.md)
- [static var grayscaleStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.GrayscaleStatusDidChangeMessage>](./messageidentifier/grayscalestatusdidchange.md)
- [static var invertColorsStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.InvertColorsStatusDidChangeMessage>](./messageidentifier/invertcolorsstatusdidchange.md)
- [static var assistiveTouchStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.AssistiveTouchStatusDidChangeMessage>](./messageidentifier/assistivetouchstatusdidchange.md)
- [static var guidedAccessStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.GuidedAccessStatusDidChangeMessage>](./messageidentifier/guidedaccessstatusdidchange.md)
- [static var monoAudioStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.MonoAudioStatusDidChangeMessage>](./messageidentifier/monoaudiostatusdidchange.md)
- [static var speakScreenStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.SpeakScreenStatusDidChangeMessage>](./messageidentifier/speakscreenstatusdidchange.md)
- [static var speakSelectionStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.SpeakSelectionStatusDidChangeMessage>](./messageidentifier/speakselectionstatusdidchange.md)
- [static var hearingDevicePairedEarDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.HearingDevicePairedEarDidChangeMessage>](./messageidentifier/hearingdevicepairedeardidchange.md)
- [static var reduceMotionStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.ReduceMotionStatusDidChangeMessage>](./messageidentifier/reducemotionstatusdidchange.md)
- [static var shakeToUndoDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.ShakeToUndoDidChangeMessage>](./messageidentifier/shaketoundodidchange.md)
- [static var voiceOverStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.VoiceOverStatusDidChangeMessage>](./messageidentifier/voiceoverstatusdidchange.md)
- [static var buttonShapesEnabledStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.ButtonShapesEnabledStatusDidChangeMessage>](./messageidentifier/buttonshapesenabledstatusdidchange.md)
### Identifying UIKit app life cycle messages
- [static var didFinishLaunching: NotificationCenter.BaseMessageIdentifier<UIApplication.DidFinishLaunchingMessage>](./messageidentifier/didfinishlaunching.md)
- [static var didBecomeActive: NotificationCenter.BaseMessageIdentifier<UIApplication.DidBecomeActiveMessage>](./messageidentifier/didbecomeactive-2hcfs.md)
- [static var didEnterBackground: NotificationCenter.BaseMessageIdentifier<UIApplication.DidEnterBackgroundMessage>](./messageidentifier/didenterbackground-1u5sm.md)
- [static var willEnterForeground: NotificationCenter.BaseMessageIdentifier<UIApplication.WillEnterForegroundMessage>](./messageidentifier/willenterforeground-95zi8.md)
- [static var willResignActive: NotificationCenter.BaseMessageIdentifier<UIApplication.WillResignActiveMessage>](./messageidentifier/willresignactive-4rf2p.md)
- [static var didReceiveMemoryWarning: NotificationCenter.BaseMessageIdentifier<UIApplication.DidReceiveMemoryWarningMessage>](./messageidentifier/didreceivememorywarning.md)
- [static var significantTimeChange: NotificationCenter.BaseMessageIdentifier<UIApplication.SignificantTimeChangeMessage>](./messageidentifier/significanttimechange.md)
- [static var backgroundRefreshStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIApplication.BackgroundRefreshStatusDidChangeMessage>](./messageidentifier/backgroundrefreshstatusdidchange.md)
- [static var userDidTakeScreenshot: NotificationCenter.BaseMessageIdentifier<UIApplication.UserDidTakeScreenshotMessage>](./messageidentifier/userdidtakescreenshot.md)
### Identifying UIKit content size messages
- [static var contentSizeCategoryDidChange: NotificationCenter.BaseMessageIdentifier<UIContentSizeCategory.DidChangeMessage>](./messageidentifier/contentsizecategorydidchange.md)
### Identifying UIKIt device messages
- [static var batteryLevelDidChange: NotificationCenter.BaseMessageIdentifier<UIDevice.BatteryLevelDidChangeMessage>](./messageidentifier/batteryleveldidchange.md)
- [static var batteryStateDidChange: NotificationCenter.BaseMessageIdentifier<UIDevice.BatteryStateDidChangeMessage>](./messageidentifier/batterystatedidchange.md)
- [static var orientationDidChange: NotificationCenter.BaseMessageIdentifier<UIDevice.OrientationDidChangeMessage>](./messageidentifier/orientationdidchange.md)
- [static var proximityStateDidChange: NotificationCenter.BaseMessageIdentifier<UIDevice.ProximityStateDidChangeMessage>](./messageidentifier/proximitystatedidchange.md)
### Identifying UIKit document messages
- [static var stateChanged: NotificationCenter.BaseMessageIdentifier<UIDocument.StateChangedMessage>](./messageidentifier/statechanged.md)
### Identifying UIKit pasteboard messages
- [static var changed: NotificationCenter.BaseMessageIdentifier<UIPasteboard.ChangedMessage>](./messageidentifier/changed-28zxj.md)
- [static var removed: NotificationCenter.BaseMessageIdentifier<UIPasteboard.RemovedMessage>](./messageidentifier/removed.md)
### Identifying UIKit responder messages
- [static var keyboardWillChangeFrame: NotificationCenter.BaseMessageIdentifier<UIResponder.KeyboardWillChangeFrameMessage>](./messageidentifier/keyboardwillchangeframe.md)
- [static var keyboardDidChangeFrame: NotificationCenter.BaseMessageIdentifier<UIResponder.KeyboardDidChangeFrameMessage>](./messageidentifier/keyboarddidchangeframe.md)
- [static var keyboardWillHide: NotificationCenter.BaseMessageIdentifier<UIResponder.KeyboardWillHideMessage>](./messageidentifier/keyboardwillhide.md)
- [static var keyboardDidHide: NotificationCenter.BaseMessageIdentifier<UIResponder.KeyboardDidHideMessage>](./messageidentifier/keyboarddidhide.md)
- [static var keyboardWillShow: NotificationCenter.BaseMessageIdentifier<UIResponder.KeyboardWillShowMessage>](./messageidentifier/keyboardwillshow.md)
- [static var keyboardDidShow: NotificationCenter.BaseMessageIdentifier<UIResponder.KeyboardDidShowMessage>](./messageidentifier/keyboarddidshow.md)
### Identifying UIKit screen messages
- [static var brightnessDidChange: NotificationCenter.BaseMessageIdentifier<UIScreen.BrightnessDidChangeMessage>](./messageidentifier/brightnessdidchange.md)
- [static var modeDidChange: NotificationCenter.BaseMessageIdentifier<UIScreen.ModeDidChangeMessage>](./messageidentifier/modedidchange.md)
- [static var capturedDidChange: NotificationCenter.BaseMessageIdentifier<UIScreen.CapturedDidChangeMessage>](./messageidentifier/captureddidchange.md)
- [static var referenceDisplayModeStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIScreen.ReferenceDisplayModeStatusDidChangeMessage>](./messageidentifier/referencedisplaymodestatusdidchange.md)
### Identifying UIKit text field messages
- [static var textDidBeginEditing: NotificationCenter.BaseMessageIdentifier<UITextField.TextDidBeginEditingMessage>](./messageidentifier/textdidbeginediting-7lt1k.md)
- [static var textDidChange: NotificationCenter.BaseMessageIdentifier<UITextField.TextDidChangeMessage>](./messageidentifier/textdidchange-9363k.md)
- [static var textDidEndEditing: NotificationCenter.BaseMessageIdentifier<UITextField.TextDidEndEditingMessage>](./messageidentifier/textdidendediting-4r8fw.md)
### Identifying UIKit text input mode messages
- [static var currentInputModeDidChange: NotificationCenter.BaseMessageIdentifier<UITextInputMode.CurrentInputModeDidChangeMessage>](./messageidentifier/currentinputmodedidchange.md)
### Identifying UIKit text view messages
- [static var textDidBeginEditing: NotificationCenter.BaseMessageIdentifier<UITextView.TextDidBeginEditingMessage>](./messageidentifier/textdidbeginediting-9y8tn.md)
- [static var textDidChange: NotificationCenter.BaseMessageIdentifier<UITextView.TextDidChangeMessage>](./messageidentifier/textdidchange-8ns63.md)
- [static var textDidEndEditing: NotificationCenter.BaseMessageIdentifier<UITextView.TextDidEndEditingMessage>](./messageidentifier/textdidendediting-6cmke.md)
### Identifying UIKit view controller messages
- [static var didBecomeVisible: NotificationCenter.BaseMessageIdentifier<UIWindow.DidBecomeVisibleMessage>](./messageidentifier/didbecomevisible.md)
- [static var didBecomeHidden: NotificationCenter.BaseMessageIdentifier<UIWindow.DidBecomeHiddenMessage>](./messageidentifier/didbecomehidden.md)
- [static var showDetailTargetDidChange: NotificationCenter.BaseMessageIdentifier<UIViewController.ShowDetailTargetDidChangeMessage>](./messageidentifier/showdetailtargetdidchange.md)
### Identifying UIKit focus messages
- [static var movementDidFail: NotificationCenter.BaseMessageIdentifier<UIFocusSystem.MovementDidFailMessage>](./messageidentifier/movementdidfail.md)
### Identifying UIKit pointer lock state messages
- [static var didChange: NotificationCenter.BaseMessageIdentifier<UIPointerLockState.DidChangeMessage>](./messageidentifier/didchange-7wty5.md)
### Identifying UIKit scene messages
- [static var systemProtectionDidChange: NotificationCenter.BaseMessageIdentifier<UIScene.SystemProtectionDidChangeMessage>](./messageidentifier/systemprotectiondidchange.md)
- [static var willConnect: NotificationCenter.BaseMessageIdentifier<UIScene.WillConnectMessage>](./messageidentifier/willconnect.md)
- [static var willEnterForeground: NotificationCenter.BaseMessageIdentifier<UIScene.WillEnterForegroundMessage>](./messageidentifier/willenterforeground-992xq.md)
- [static var didActivate: NotificationCenter.BaseMessageIdentifier<UIScene.DidActivateMessage>](./messageidentifier/didactivate.md)
- [static var willDeactivate: NotificationCenter.BaseMessageIdentifier<UIScene.WillDeactivateMessage>](./messageidentifier/willdeactivate.md)
- [static var didEnterBackground: NotificationCenter.BaseMessageIdentifier<UIScene.DidEnterBackgroundMessage>](./messageidentifier/didenterbackground-5fqw0.md)
### Identifying AppKit workspace messages
- [static var didHideApplication: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidHideApplicationMessage>](./messageidentifier/didhideapplication.md)
- [static var didUnhideApplication: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidUnhideApplicationMessage>](./messageidentifier/didunhideapplication.md)
- [static var willLaunchApplication: NotificationCenter.BaseMessageIdentifier<NSWorkspace.WillLaunchApplicationMessage>](./messageidentifier/willlaunchapplication.md)
- [static var didLaunchApplication: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidLaunchApplicationMessage>](./messageidentifier/didlaunchapplication.md)
- [static var willSleep: NotificationCenter.BaseMessageIdentifier<NSWorkspace.WillSleepMessage>](./messageidentifier/willsleep.md)
- [static var didWake: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidWakeMessage>](./messageidentifier/didwake.md)
- [static var didTerminateApplication: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidTerminateApplicationMessage>](./messageidentifier/didterminateapplication.md)
- [static var didMountVolume: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidMountVolumeMessage>](./messageidentifier/didmountvolume.md)
- [static var willUnmountVolume: NotificationCenter.BaseMessageIdentifier<NSWorkspace.WillUnmountVolumeMessage>](./messageidentifier/willunmountvolume.md)
- [static var didUnmountVolume: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidUnmountVolumeMessage>](./messageidentifier/didunmountvolume.md)
- [static var didActivateApplication: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidActivateApplicationMessage>](./messageidentifier/didactivateapplication.md)
- [static var didDeactivateApplication: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidDeactivateApplicationMessage>](./messageidentifier/diddeactivateapplication.md)
- [static var didRenameVolume: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidRenameVolumeMessage>](./messageidentifier/didrenamevolume.md)
- [static var sessionDidBecomeActive: NotificationCenter.BaseMessageIdentifier<NSWorkspace.SessionDidBecomeActiveMessage>](./messageidentifier/sessiondidbecomeactive.md)
- [static var sessionDidResignActive: NotificationCenter.BaseMessageIdentifier<NSWorkspace.SessionDidResignActiveMessage>](./messageidentifier/sessiondidresignactive.md)
- [static var didChangeFileLabels: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidChangeFileLabelsMessage>](./messageidentifier/didchangefilelabels.md)
- [static var screensDidSleep: NotificationCenter.BaseMessageIdentifier<NSWorkspace.ScreensDidSleepMessage>](./messageidentifier/screensdidsleep.md)
- [static var screensDidWake: NotificationCenter.BaseMessageIdentifier<NSWorkspace.ScreensDidWakeMessage>](./messageidentifier/screensdidwake.md)
- [static var activeSpaceDidChange: NotificationCenter.BaseMessageIdentifier<NSWorkspace.ActiveSpaceDidChangeMessage>](./messageidentifier/activespacedidchange.md)
- [static var accessibilityDisplayOptionsDidChange: NotificationCenter.BaseMessageIdentifier<NSWorkspace.AccessibilityDisplayOptionsDidChangeMessage>](./messageidentifier/accessibilitydisplayoptionsdidchange.md)
- [static var shouldBeginSuppressingHighDynamicRangeContent: NotificationCenter.BaseMessageIdentifier<NSApplication.ShouldBeginSuppressingHighDynamicRangeContent>](./messageidentifier/shouldbeginsuppressinghighdynamicrangecontent.md)
- [static var shouldEndSuppressingHighDynamicRangeContent: NotificationCenter.BaseMessageIdentifier<NSApplication.ShouldEndSuppressingHighDynamicRangeContent>](./messageidentifier/shouldendsuppressinghighdynamicrangecontent.md)
### Identifying EventKit messages
- [static var changed: NotificationCenter.BaseMessageIdentifier<EKEventStore.EventStoreChanged>](./messageidentifier/changed-50yz5.md)
  A notification posted when changes are made to the Calendar or Reminders database.
### Identifying iTunes library messages
- [static var didChange: NotificationCenter.BaseMessageIdentifier<DidChangeLibraryMessage>](./messageidentifier/didchange-1coqh.md)
### Type Properties
- [static var accessoryDidConnect: NotificationCenter.BaseMessageIdentifier<EAAccessoryManager.AccessoryDidConnectMessage>](./messageidentifier/accessorydidconnect.md)
- [static var accessoryDidDisconnect: NotificationCenter.BaseMessageIdentifier<EAAccessoryManager.AccessoryDidDisconnectMessage>](./messageidentifier/accessorydiddisconnect.md)
- [static var applicationAccessibilityEnabledDidChange: NotificationCenter.BaseMessageIdentifier<AccessibilitySettings.ApplicationAccessibilityEnabledDidChangeMessage>](./messageidentifier/applicationaccessibilityenableddidchange.md)
  Shorthand identifier for `AccessibilitySettings/ApplicationAccessibilityEnabledDidChangeMessage`.
- [static var boundsDidChange: NotificationCenter.BaseMessageIdentifier<NSView.BoundsDidChangeMessage>](./messageidentifier/boundsdidchange.md)
- [static var colorDidChange: NotificationCenter.BaseMessageIdentifier<NSColorPanel.ColorDidChangeMessage>](./messageidentifier/colordidchange.md)
- [static var colorSpaceDidChange: NotificationCenter.BaseMessageIdentifier<NSScreen.ColorSpaceDidChangeMessage>](./messageidentifier/colorspacedidchange.md)
- [static var columnConfigurationDidChange: NotificationCenter.BaseMessageIdentifier<NSBrowser.ColumnConfigurationDidChangeMessage>](./messageidentifier/columnconfigurationdidchange.md)
- [static var columnDidMove: NotificationCenter.BaseMessageIdentifier<NSOutlineView.ColumnDidMoveMessage>](./messageidentifier/columndidmove-78e2d.md)
- [static var columnDidMove: NotificationCenter.BaseMessageIdentifier<NSTableView.ColumnDidMoveMessage>](./messageidentifier/columndidmove-9tkq6.md)
- [static var columnDidResize: NotificationCenter.BaseMessageIdentifier<NSOutlineView.ColumnDidResizeMessage>](./messageidentifier/columndidresize-5pxs4.md)
- [static var columnDidResize: NotificationCenter.BaseMessageIdentifier<NSTableView.ColumnDidResizeMessage>](./messageidentifier/columndidresize-7ktag.md)
- [static var contextHelpModeDidActivate: NotificationCenter.BaseMessageIdentifier<NSHelpManager.ContextHelpModeDidActivateMessage>](./messageidentifier/contexthelpmodedidactivate.md)
- [static var contextHelpModeDidDeactivate: NotificationCenter.BaseMessageIdentifier<NSHelpManager.ContextHelpModeDidDeactivateMessage>](./messageidentifier/contexthelpmodediddeactivate.md)
- [static var conversationHistoryDidUpdateMessage: NotificationCenter.BaseMessageIdentifier<ConversationHistoryManager.ConversationHistoryDidUpdate>](./messageidentifier/conversationhistorydidupdatemessage.md)
- [static var didAddItem: NotificationCenter.BaseMessageIdentifier<NSMenu.DidAddItemMessage>](./messageidentifier/didadditem.md)
- [static var didBecomeActive: NotificationCenter.BaseMessageIdentifier<NSApplication.DidBecomeActiveMessage>](./messageidentifier/didbecomeactive-2y311.md)
- [static var didBecomeActive: NotificationCenter.BaseMessageIdentifier<AVAudioSession.DidBecomeActiveMessage>](./messageidentifier/didbecomeactive-546kc.md)
- [static var didBecomeCurrent: NotificationCenter.BaseMessageIdentifier<GCController.DidBecomeCurrentMessage>](./messageidentifier/didbecomecurrent-9p0n4.md)
  The identifier of the message that posts after a game controller becomes the most recently used controller.
- [static var didBecomeCurrent: NotificationCenter.BaseMessageIdentifier<GCMouse.DidBecomeCurrentMessage>](./messageidentifier/didbecomecurrent-9zfc.md)
  The identifier of the message that posts after a mouse becomes the most recently used mouse.
- [static var didBecomeInactive: NotificationCenter.BaseMessageIdentifier<AVAudioSession.DidBecomeInactiveMessage>](./messageidentifier/didbecomeinactive.md)
- [static var didBecomeKey: NotificationCenter.BaseMessageIdentifier<NSWindow.DidBecomeKeyMessage>](./messageidentifier/didbecomekey-3qijm.md)
- [static var didBecomeKey: NotificationCenter.BaseMessageIdentifier<UIWindow.DidBecomeKeyMessage>](./messageidentifier/didbecomekey-6kgub.md)
- [static var didBecomeMain: NotificationCenter.BaseMessageIdentifier<NSWindow.DidBecomeMainMessage>](./messageidentifier/didbecomemain.md)
- [static var didBeginEditing: NotificationCenter.BaseMessageIdentifier<NSTextView.DidBeginEditingMessage>](./messageidentifier/didbeginediting.md)
- [static var didBeginTracking: NotificationCenter.BaseMessageIdentifier<NSMenu.DidBeginTrackingMessage>](./messageidentifier/didbegintracking.md)
- [static var didChange: NotificationCenter.BaseMessageIdentifier<NSFontCollection.DidChangeMessage>](./messageidentifier/didchange-1ebzb.md)
- [static var didChange: NotificationCenter.BaseMessageIdentifier<NSColorList.DidChangeMessage>](./messageidentifier/didchange-96f1i.md)
- [static var didChange: NotificationCenter.BaseMessageIdentifier<NSTextView.DidChangeMessage>](./messageidentifier/didchange-ywl6.md)
- [static var didChangeAutomaticCapitalization: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticCapitalizationMessage>](./messageidentifier/didchangeautomaticcapitalization.md)
- [static var didChangeAutomaticDashSubstitution: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticDashSubstitutionMessage>](./messageidentifier/didchangeautomaticdashsubstitution.md)
- [static var didChangeAutomaticInlinePrediction: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticInlinePredictionMessage>](./messageidentifier/didchangeautomaticinlineprediction.md)
- [static var didChangeAutomaticPeriodSubstitution: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticPeriodSubstitutionMessage>](./messageidentifier/didchangeautomaticperiodsubstitution.md)
- [static var didChangeAutomaticQuoteSubstitution: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticQuoteSubstitutionMessage>](./messageidentifier/didchangeautomaticquotesubstitution.md)
- [static var didChangeAutomaticSpellingCorrection: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticSpellingCorrectionMessage>](./messageidentifier/didchangeautomaticspellingcorrection.md)
- [static var didChangeAutomaticTextCompletion: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticTextCompletionMessage>](./messageidentifier/didchangeautomatictextcompletion.md)
- [static var didChangeAutomaticTextReplacement: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticTextReplacementMessage>](./messageidentifier/didchangeautomatictextreplacement.md)
- [static var didChangeBackingProperties: NotificationCenter.BaseMessageIdentifier<NSWindow.DidChangeBackingPropertiesMessage>](./messageidentifier/didchangebackingproperties.md)
- [static var didChangeItem: NotificationCenter.BaseMessageIdentifier<NSMenu.DidChangeItemMessage>](./messageidentifier/didchangeitem.md)
- [static var didChangeOcclusionState: NotificationCenter.BaseMessageIdentifier<NSWindow.DidChangeOcclusionStateMessage>](./messageidentifier/didchangeocclusionstate-5853a.md)
- [static var didChangeOcclusionState: NotificationCenter.BaseMessageIdentifier<NSApplication.DidChangeOcclusionStateMessage>](./messageidentifier/didchangeocclusionstate-99vn6.md)
- [static var didChangeScreen: NotificationCenter.BaseMessageIdentifier<NSWindow.DidChangeScreenMessage>](./messageidentifier/didchangescreen.md)
- [static var didChangeScreenParameters: NotificationCenter.BaseMessageIdentifier<NSApplication.DidChangeScreenParametersMessage>](./messageidentifier/didchangescreenparameters.md)
- [static var didChangeScreenProfile: NotificationCenter.BaseMessageIdentifier<NSWindow.DidChangeScreenProfileMessage>](./messageidentifier/didchangescreenprofile.md)
- [static var didChangeSelection: NotificationCenter.BaseMessageIdentifier<NSTextView.DidChangeSelectionMessage>](./messageidentifier/didchangeselection.md)
- [static var didChangeTypingAttributes: NotificationCenter.BaseMessageIdentifier<NSTextView.DidChangeTypingAttributesMessage>](./messageidentifier/didchangetypingattributes.md)
- [static var didClose: NotificationCenter.BaseMessageIdentifier<NSPopover.DidCloseMessage>](./messageidentifier/didclose.md)
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCMouse.DidConnectMessage>](./messageidentifier/didconnect-2pidr.md)
  The identifier of the message that posts after a mouse accessory connects to the device.
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCRacingWheel.DidConnectMessage>](./messageidentifier/didconnect-39qlx.md)
  The identifier of the message that posts after a racing wheel accessory connects to the device.
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCController.DidConnectMessage>](./messageidentifier/didconnect-3d7x9.md)
  The identifier of the message that posts after a game controller accessory connects to the device.
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCKeyboard.DidConnectMessage>](./messageidentifier/didconnect-6zuxs.md)
  The identifier of the message that posts after a keyboard accessory connects to the device.
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCSpatialAccessory.DidConnectMessage>](./messageidentifier/didconnect-oq29.md)
  The identifier of the message that posts after a spatial accessory connects to the device.
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCStylus.DidConnectMessage>](./messageidentifier/didconnect-wf9.md)
  The identifier of the message that posts after a stylus accessory connects to the device.
- [static var didDeminiaturize: NotificationCenter.BaseMessageIdentifier<NSWindow.DidDeminiaturizeMessage>](./messageidentifier/diddeminiaturize.md)
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCRacingWheel.DidDisconnectMessage>](./messageidentifier/diddisconnect-127wj.md)
  The identifier of the message that posts after a racing wheel accessory disconnects from the device.
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCStylus.DidDisconnectMessage>](./messageidentifier/diddisconnect-3p6qi.md)
  The identifier of the message that posts after a stylus accessory disconnects from the device.
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCMouse.DidDisconnectMessage>](./messageidentifier/diddisconnect-5s9vw.md)
  The identifier of the message that posts after a mouse accessory disconnects from the device.
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCKeyboard.DidDisconnectMessage>](./messageidentifier/diddisconnect-97jtl.md)
  The identifier of the message that posts after a keyboard accessory disconnects from the device.
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCSpatialAccessory.DidDisconnectMessage>](./messageidentifier/diddisconnect-9qi2f.md)
  The identifier of the message that posts after a spatial accessory disconnects from the device.
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCController.DidDisconnectMessage>](./messageidentifier/diddisconnect-9ymbl.md)
  The identifier of the message that posts after a game controller accessory disconnects from the device.
- [static var didEndEditing: NotificationCenter.BaseMessageIdentifier<NSTextView.DidEndEditingMessage>](./messageidentifier/didendediting.md)
- [static var didEndLiveMagnify: NotificationCenter.BaseMessageIdentifier<NSScrollView.DidEndLiveMagnifyMessage>](./messageidentifier/didendlivemagnify.md)
- [static var didEndLiveResize: NotificationCenter.BaseMessageIdentifier<NSWindow.DidEndLiveResizeMessage>](./messageidentifier/didendliveresize.md)
- [static var didEndLiveScroll: NotificationCenter.BaseMessageIdentifier<NSScrollView.DidEndLiveScrollMessage>](./messageidentifier/didendlivescroll.md)
- [static var didEndSheet: NotificationCenter.BaseMessageIdentifier<NSWindow.DidEndSheetMessage>](./messageidentifier/didendsheet.md)
- [static var didEndTracking: NotificationCenter.BaseMessageIdentifier<NSMenu.DidEndTrackingMessage>](./messageidentifier/didendtracking.md)
- [static var didEnterFullScreen: NotificationCenter.BaseMessageIdentifier<NSWindow.DidEnterFullScreenMessage>](./messageidentifier/didenterfullscreen.md)
- [static var didEnterVersionBrowser: NotificationCenter.BaseMessageIdentifier<NSWindow.DidEnterVersionBrowserMessage>](./messageidentifier/didenterversionbrowser.md)
- [static var didExitFullScreen: NotificationCenter.BaseMessageIdentifier<NSWindow.DidExitFullScreenMessage>](./messageidentifier/didexitfullscreen.md)
- [static var didExitVersionBrowser: NotificationCenter.BaseMessageIdentifier<NSWindow.DidExitVersionBrowserMessage>](./messageidentifier/didexitversionbrowser.md)
- [static var didExpose: NotificationCenter.BaseMessageIdentifier<NSWindow.DidExposeMessage>](./messageidentifier/didexpose.md)
- [static var didFinishRestoringWindows: NotificationCenter.BaseMessageIdentifier<NSApplication.DidFinishRestoringWindowsMessage>](./messageidentifier/didfinishrestoringwindows.md)
- [static var didHide: NotificationCenter.BaseMessageIdentifier<NSApplication.DidHideMessage>](./messageidentifier/didhide.md)
- [static var didLiveScroll: NotificationCenter.BaseMessageIdentifier<NSScrollView.DidLiveScrollMessage>](./messageidentifier/didlivescroll.md)
- [static var didMergeChanges: NotificationCenter.BaseMessageIdentifier<NSManagedObjectContext.DidMergeChangesMessage>](./messageidentifier/didmergechanges.md)
- [static var didMergeChangesAsync: NotificationCenter.BaseMessageIdentifier<NSManagedObjectContext.DidMergeChangesAsyncMessage>](./messageidentifier/didmergechangesasync.md)
- [static var didMiniaturize: NotificationCenter.BaseMessageIdentifier<NSWindow.DidMiniaturizeMessage>](./messageidentifier/didminiaturize.md)
- [static var didMove: NotificationCenter.BaseMessageIdentifier<NSWindow.DidMoveMessage>](./messageidentifier/didmove.md)
- [static var didMoveToWritableLocation: NotificationCenter.BaseMessageIdentifier<UIDocument.DidMoveToWritableLocationMessage>](./messageidentifier/didmovetowritablelocation.md)
- [static var didRemoveItem: NotificationCenter.BaseMessageIdentifier<NSToolbar.DidRemoveItemMessage>](./messageidentifier/didremoveitem-4hapv.md)
- [static var didRemoveItem: NotificationCenter.BaseMessageIdentifier<NSMenu.DidRemoveItemMessage>](./messageidentifier/didremoveitem-bimz.md)
- [static var didResignActive: NotificationCenter.BaseMessageIdentifier<NSApplication.DidResignActiveMessage>](./messageidentifier/didresignactive.md)
- [static var didResignKey: NotificationCenter.BaseMessageIdentifier<UIWindow.DidResignKeyMessage>](./messageidentifier/didresignkey-11hzh.md)
- [static var didResignKey: NotificationCenter.BaseMessageIdentifier<NSWindow.DidResignKeyMessage>](./messageidentifier/didresignkey-2dgp0.md)
- [static var didResignMain: NotificationCenter.BaseMessageIdentifier<NSWindow.DidResignMainMessage>](./messageidentifier/didresignmain.md)
- [static var didResize: NotificationCenter.BaseMessageIdentifier<NSWindow.DidResizeMessage>](./messageidentifier/didresize.md)
- [static var didResizeSubviews: NotificationCenter.BaseMessageIdentifier<NSSplitView.DidResizeSubviewsMessage>](./messageidentifier/didresizesubviews.md)
- [static var didSave: NotificationCenter.BaseMessageIdentifier<NSManagedObjectContext.DidSaveMessage>](./messageidentifier/didsave.md)
- [static var didSaveObjectIDs: NotificationCenter.BaseMessageIdentifier<NSManagedObjectContext.DidSaveObjectIDsMessage>](./messageidentifier/didsaveobjectids.md)
- [static var didSaveObjectIDsAsync: NotificationCenter.BaseMessageIdentifier<NSManagedObjectContext.DidSaveObjectIDsAsyncMessage>](./messageidentifier/didsaveobjectidsasync.md)
- [static var didSendAction: NotificationCenter.BaseMessageIdentifier<NSMenu.DidSendActionMessage>](./messageidentifier/didsendaction.md)
- [static var didShow: NotificationCenter.BaseMessageIdentifier<NSPopover.DidShowMessage>](./messageidentifier/didshow.md)
- [static var didStopBeingCurrent: NotificationCenter.BaseMessageIdentifier<GCMouse.DidStopBeingCurrentMessage>](./messageidentifier/didstopbeingcurrent-2sc31.md)
  The identifier of the message that posts after a mouse stops being longer the most recently used mouse.
- [static var didStopBeingCurrent: NotificationCenter.BaseMessageIdentifier<GCController.DidStopBeingCurrentMessage>](./messageidentifier/didstopbeingcurrent-9pdq9.md)
  The identifier of the message that posts after a game controller stops being longer the most recently used controller.
- [static var didUnhide: NotificationCenter.BaseMessageIdentifier<NSApplication.DidUnhideMessage>](./messageidentifier/didunhide.md)
- [static var didUpdate: NotificationCenter.BaseMessageIdentifier<UIFocusSystem.DidUpdateMessage>](./messageidentifier/didupdate-p3fm.md)
- [static var didUpdate: NotificationCenter.BaseMessageIdentifier<NSWindow.DidUpdateMessage>](./messageidentifier/didupdate-vu3m.md)
- [static var didUpdateWindows: NotificationCenter.BaseMessageIdentifier<NSApplication.DidUpdateWindowsMessage>](./messageidentifier/didupdatewindows.md)
- [static var displayGenlockModeChanged: NotificationCenter.BaseMessageIdentifier<CMClock.DisplayGenlockModeChangedMessage>](./messageidentifier/displaygenlockmodechanged.md)
  Identifies `CMClock/DisplayGenlockModeChangedMessage`.
- [static var eventChanged: NotificationCenter.BaseMessageIdentifier<NSPersistentCloudKitContainer.EventChangedMessage>](./messageidentifier/eventchanged.md)
- [static var fontSetChanged: NotificationCenter.BaseMessageIdentifier<NSFont.FontSetChangedMessage>](./messageidentifier/fontsetchanged.md)
- [static var frameDidChange: NotificationCenter.BaseMessageIdentifier<NSView.FrameDidChangeMessage>](./messageidentifier/framedidchange.md)
- [static var indexDidUpdate: NotificationCenter.BaseMessageIdentifier<NSCoreDataCoreSpotlightDelegate.IndexDidUpdateMessage>](./messageidentifier/indexdidupdate.md)
- [static var itemDidCollapse: NotificationCenter.BaseMessageIdentifier<NSOutlineView.ItemDidCollapseMessage>](./messageidentifier/itemdidcollapse.md)
- [static var itemDidExpand: NotificationCenter.BaseMessageIdentifier<NSOutlineView.ItemDidExpandMessage>](./messageidentifier/itemdidexpand.md)
- [static var itemWillCollapse: NotificationCenter.BaseMessageIdentifier<NSOutlineView.ItemWillCollapseMessage>](./messageidentifier/itemwillcollapse.md)
- [static var itemWillExpand: NotificationCenter.BaseMessageIdentifier<NSOutlineView.ItemWillExpandMessage>](./messageidentifier/itemwillexpand.md)
- [static var keyboardSelectionDidChange: NotificationCenter.BaseMessageIdentifier<NSTextInputContext.KeyboardSelectionDidChangeMessage>](./messageidentifier/keyboardselectiondidchange.md)
- [static var objectsDidChange: NotificationCenter.BaseMessageIdentifier<NSManagedObjectContext.ObjectsDidChangeMessage>](./messageidentifier/objectsdidchange.md)
- [static var preferredScrollerStyleDidChange: NotificationCenter.BaseMessageIdentifier<NSScroller.PreferredScrollerStyleDidChangeMessage>](./messageidentifier/preferredscrollerstyledidchange.md)
- [static var protectedDataDidBecomeAvailable: NotificationCenter.BaseMessageIdentifier<NSApplication.ProtectedDataDidBecomeAvailableMessage>](./messageidentifier/protecteddatadidbecomeavailable-3di2c.md)
- [static var protectedDataDidBecomeAvailable: NotificationCenter.BaseMessageIdentifier<UIApplication.ProtectedDataDidBecomeAvailableMessage>](./messageidentifier/protecteddatadidbecomeavailable-6h44m.md)
- [static var protectedDataWillBecomeUnavailable: NotificationCenter.BaseMessageIdentifier<NSApplication.ProtectedDataWillBecomeUnavailableMessage>](./messageidentifier/protecteddatawillbecomeunavailable-1izcs.md)
- [static var protectedDataWillBecomeUnavailable: NotificationCenter.BaseMessageIdentifier<UIApplication.ProtectedDataWillBecomeUnavailableMessage>](./messageidentifier/protecteddatawillbecomeunavailable-3n08h.md)
- [static var radioAccessTechnologyDidChange: NotificationCenter.BaseMessageIdentifier<CTTelephonyNetworkInfo.RadioAccessTechnologyDidChangeMessage>](./messageidentifier/radioaccesstechnologydidchange.md)
- [static var registrationsChanged: NotificationCenter.BaseMessageIdentifier<AVAudioUnitComponentManager.RegistrationsChangedMessage>](./messageidentifier/registrationschanged.md)
- [static var registryDidChange: NotificationCenter.BaseMessageIdentifier<NSImageRep.RegistryDidChangeMessage>](./messageidentifier/registrydidchange.md)
- [static var remoteChange: NotificationCenter.BaseMessageIdentifier<NSPersistentStoreCoordinator.RemoteChangeMessage>](./messageidentifier/remotechange.md)
- [static var resumptionRecommendation: NotificationCenter.BaseMessageIdentifier<AVAudioSession.ResumptionRecommendationMessage>](./messageidentifier/resumptionrecommendation.md)
- [static var rowsDidChange: NotificationCenter.BaseMessageIdentifier<NSRuleEditor.RowsDidChangeMessage>](./messageidentifier/rowsdidchange.md)
- [static var selectedAlternativeString: NotificationCenter.BaseMessageIdentifier<NSTextAlternatives.SelectedAlternativeStringMessage>](./messageidentifier/selectedalternativestring.md)
- [static var selectionDidChange: NotificationCenter.BaseMessageIdentifier<UITableView.SelectionDidChangeMessage>](./messageidentifier/selectiondidchange-2akj4.md)
- [static var selectionDidChange: NotificationCenter.BaseMessageIdentifier<NSTableView.SelectionDidChangeMessage>](./messageidentifier/selectiondidchange-676mh.md)
- [static var selectionDidChange: NotificationCenter.BaseMessageIdentifier<NSComboBox.SelectionDidChangeMessage>](./messageidentifier/selectiondidchange-72x2p.md)
- [static var selectionDidChange: NotificationCenter.BaseMessageIdentifier<NSOutlineView.SelectionDidChangeMessage>](./messageidentifier/selectiondidchange-7qmnc.md)
- [static var selectionIsChanging: NotificationCenter.BaseMessageIdentifier<NSComboBox.SelectionIsChangingMessage>](./messageidentifier/selectionischanging-2i647.md)
- [static var selectionIsChanging: NotificationCenter.BaseMessageIdentifier<NSTableView.SelectionIsChangingMessage>](./messageidentifier/selectionischanging-5u4tc.md)
- [static var selectionIsChanging: NotificationCenter.BaseMessageIdentifier<NSOutlineView.SelectionIsChangingMessage>](./messageidentifier/selectionischanging-abh0.md)
- [static var storesDidChange: NotificationCenter.BaseMessageIdentifier<NSPersistentStoreCoordinator.StoresDidChangeMessage>](./messageidentifier/storesdidchange.md)
- [static var storesDidChangeAsync: NotificationCenter.BaseMessageIdentifier<NSPersistentStoreCoordinator.StoresDidChangeAsyncMessage>](./messageidentifier/storesdidchangeasync.md)
- [static var systemColorsDidChange: NotificationCenter.BaseMessageIdentifier<NSColor.SystemColorsDidChangeMessage>](./messageidentifier/systemcolorsdidchange.md)
- [static var systemPrefersReducedResourceUsageDidChange: NotificationCenter.BaseMessageIdentifier<UIApplication.SystemPrefersReducedResourceUsageDidChangeMessage>](./messageidentifier/systemprefersreducedresourceusagedidchange.md)
- [static var tagsDidChange: NotificationCenter.BaseMessageIdentifier<AVAudioUnitComponent.TagsDidChangeMessage>](./messageidentifier/tagsdidchange.md)
- [static var textDidBeginEditing: NotificationCenter.BaseMessageIdentifier<NSControl.TextDidBeginEditingMessage>](./messageidentifier/textdidbeginediting-45vc.md)
- [static var textDidChange: NotificationCenter.BaseMessageIdentifier<NSControl.TextDidChangeMessage>](./messageidentifier/textdidchange-5j4s4.md)
- [static var textDidEndEditing: NotificationCenter.BaseMessageIdentifier<NSControl.TextDidEndEditingMessage>](./messageidentifier/textdidendediting-5yxiy.md)
- [static var textMessageAvailabilityDidChange: NotificationCenter.BaseMessageIdentifier<MFMessageComposeViewController.TextMessageAvailabilityDidChangeMessage>](./messageidentifier/textmessageavailabilitydidchange.md)
  Notification posted when text message availability changes.
- [static var tokensDidExpire: NotificationCenter.BaseMessageIdentifier<ManagedSettingsStore.TokenExpiryMessage>](./messageidentifier/tokensdidexpire.md)
- [static var userPreferencesDidChange: NotificationCenter.BaseMessageIdentifier<HKHealthStore.HKUserPreferencesDidChangeMessage>](./messageidentifier/userpreferencesdidchange.md)
- [static var willAddItem: NotificationCenter.BaseMessageIdentifier<NSToolbar.WillAddItemMessage>](./messageidentifier/willadditem.md)
- [static var willBecomeActive: NotificationCenter.BaseMessageIdentifier<NSApplication.WillBecomeActiveMessage>](./messageidentifier/willbecomeactive.md)
- [static var willBeginSheet: NotificationCenter.BaseMessageIdentifier<NSWindow.WillBeginSheetMessage>](./messageidentifier/willbeginsheet.md)
- [static var willChangeNotifyingTextView: NotificationCenter.BaseMessageIdentifier<NSTextView.WillChangeNotifyingTextViewMessage>](./messageidentifier/willchangenotifyingtextview.md)
- [static var willClose: NotificationCenter.BaseMessageIdentifier<NSPopover.WillCloseMessage>](./messageidentifier/willclose-2wsvs.md)
- [static var willClose: NotificationCenter.BaseMessageIdentifier<NSWindow.WillCloseMessage>](./messageidentifier/willclose-4565q.md)
- [static var willDismiss: NotificationCenter.BaseMessageIdentifier<NSComboBox.WillDismissMessage>](./messageidentifier/willdismiss.md)
- [static var willEnterFullScreen: NotificationCenter.BaseMessageIdentifier<NSWindow.WillEnterFullScreenMessage>](./messageidentifier/willenterfullscreen.md)
- [static var willEnterVersionBrowser: NotificationCenter.BaseMessageIdentifier<NSWindow.WillEnterVersionBrowserMessage>](./messageidentifier/willenterversionbrowser.md)
- [static var willExitFullScreen: NotificationCenter.BaseMessageIdentifier<NSWindow.WillExitFullScreenMessage>](./messageidentifier/willexitfullscreen.md)
- [static var willExitVersionBrowser: NotificationCenter.BaseMessageIdentifier<NSWindow.WillExitVersionBrowserMessage>](./messageidentifier/willexitversionbrowser.md)
- [static var willFinishLaunching: NotificationCenter.BaseMessageIdentifier<NSApplication.WillFinishLaunchingMessage>](./messageidentifier/willfinishlaunching.md)
- [static var willHide: NotificationCenter.BaseMessageIdentifier<NSApplication.WillHideMessage>](./messageidentifier/willhide.md)
- [static var willMiniaturize: NotificationCenter.BaseMessageIdentifier<NSWindow.WillMiniaturizeMessage>](./messageidentifier/willminiaturize.md)
- [static var willMove: NotificationCenter.BaseMessageIdentifier<NSWindow.WillMoveMessage>](./messageidentifier/willmove.md)
- [static var willPopUp: NotificationCenter.BaseMessageIdentifier<NSComboBox.WillPopUpMessage>](./messageidentifier/willpopup-4czk2.md)
- [static var willPopUp: NotificationCenter.BaseMessageIdentifier<NSPopUpButton.WillPopUpMessage>](./messageidentifier/willpopup-81zuu.md)
- [static var willPopUp: NotificationCenter.BaseMessageIdentifier<NSPopUpButtonCell.WillPopUpMessage>](./messageidentifier/willpopup-8ycpp.md)
- [static var willResignActive: NotificationCenter.BaseMessageIdentifier<NSApplication.WillResignActiveMessage>](./messageidentifier/willresignactive-9aumz.md)
- [static var willResizeSubviews: NotificationCenter.BaseMessageIdentifier<NSSplitView.WillResizeSubviewsMessage>](./messageidentifier/willresizesubviews.md)
- [static var willSave: NotificationCenter.BaseMessageIdentifier<NSManagedObjectContext.WillSaveMessage>](./messageidentifier/willsave.md)
- [static var willSendAction: NotificationCenter.BaseMessageIdentifier<NSMenu.WillSendActionMessage>](./messageidentifier/willsendaction.md)
- [static var willShow: NotificationCenter.BaseMessageIdentifier<NSPopover.WillShowMessage>](./messageidentifier/willshow.md)
- [static var willStartLiveMagnify: NotificationCenter.BaseMessageIdentifier<NSScrollView.WillStartLiveMagnifyMessage>](./messageidentifier/willstartlivemagnify.md)
- [static var willStartLiveResize: NotificationCenter.BaseMessageIdentifier<NSWindow.WillStartLiveResizeMessage>](./messageidentifier/willstartliveresize.md)
- [static var willStartLiveScroll: NotificationCenter.BaseMessageIdentifier<NSScrollView.WillStartLiveScrollMessage>](./messageidentifier/willstartlivescroll.md)
- [static var willTerminate: NotificationCenter.BaseMessageIdentifier<UIApplication.WillTerminateMessage>](./messageidentifier/willterminate-1u238.md)
- [static var willTerminate: NotificationCenter.BaseMessageIdentifier<NSApplication.WillTerminateMessage>](./messageidentifier/willterminate-7lu3s.md)
- [static var willUnhide: NotificationCenter.BaseMessageIdentifier<NSApplication.WillUnhideMessage>](./messageidentifier/willunhide.md)
- [static var willUpdateWindows: NotificationCenter.BaseMessageIdentifier<NSApplication.WillUpdateWindowsMessage>](./messageidentifier/willupdatewindows.md)

## Relationships

### Conforming Types
- [NotificationCenter.BaseMessageIdentifier](./basemessageidentifier.md)

## See Also

### Using message identifiers
- [NotificationCenter.BaseMessageIdentifier](./basemessageidentifier.md)
  A type for use when defining optional Message identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier)*