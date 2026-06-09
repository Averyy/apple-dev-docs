# NotificationCenter.MessageIdentifier

**Framework**: Foundation  
**Kind**: protocol

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

#### Overview

Implement a `MessageIdentifier` to provide a typed, ergonomic experience at the call point, as described in [`SE-0299`](https://developer.apple.comhttps://github.com/swiftlang/swift-evolution/blob/main/proposals/0299-extend-generic-static-member-lookup.md).

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
- [associatedtype MessageType](notificationcenter/messageidentifier/messagetype.md)
### Identifying cookie storage messages
- [static var cookiesChanged: NotificationCenter.BaseMessageIdentifier<HTTPCookieStorage.CookiesChangedMessage>](notificationcenter/messageidentifier/cookieschanged.md)
  An identifier for a message about a cookie storage instance’s cookies changing.
### Identifying undo manager messages
- [static var willUndoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.WillUndoChangeMessage>](notificationcenter/messageidentifier/willundochange.md)
  An identifier for a message about an undo manager preparing to perform an undo.
- [static var didUndoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.DidUndoChangeMessage>](notificationcenter/messageidentifier/didundochange.md)
  An identifier for a message about an undo manager having performed an undo.
- [static var willRedoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.WillRedoChangeMessage>](notificationcenter/messageidentifier/willredochange.md)
  An identifier for a message about an undo manager preparing to perform a redo.
- [static var didRedoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.DidRedoChangeMessage>](notificationcenter/messageidentifier/didredochange.md)
  An identifier for a message about an undo manager having performed a redo.
- [static var checkpoint: NotificationCenter.BaseMessageIdentifier<UndoManager.CheckpointMessage>](notificationcenter/messageidentifier/checkpoint.md)
  An identifier for a message about an undo manager reaching a checkpoint.
- [static var didOpenUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.DidOpenUndoGroupMessage>](notificationcenter/messageidentifier/didopenundogroup.md)
  An identifier for a message about an undo manager having opened an undo group.
- [static var willCloseUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.WillCloseUndoGroupMessage>](notificationcenter/messageidentifier/willcloseundogroup.md)
  An identifier for a message about an undo manager preparing to close an undo group.
- [static var didCloseUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.DidCloseUndoGroupMessage>](notificationcenter/messageidentifier/didcloseundogroup.md)
  An identifier for a message about an undo manager having closed an undo group.
### Identifying defaults messages
- [static var didChange: NotificationCenter.BaseMessageIdentifier<UserDefaults.DidChangeMessage>](notificationcenter/messageidentifier/didchange-187tw.md)
  An identifier for a message about a change in a user defaults setting.
- [static var sizeLimitExceeded: NotificationCenter.BaseMessageIdentifier<UserDefaults.SizeLimitExceededMessage>](notificationcenter/messageidentifier/sizelimitexceeded.md)
  An identifier for a message about a user defaults database exceeding its maximum size.
### Identifying metadata query messages
- [static var didStartGathering: NotificationCenter.BaseMessageIdentifier<NSMetadataQuery.DidStartGatheringMessage>](notificationcenter/messageidentifier/didstartgathering.md)
  An identifier for a message about a metadata query that is starting its initial result gathering.
- [static var didFinishGathering: NotificationCenter.BaseMessageIdentifier<NSMetadataQuery.DidFinishGatheringMessage>](notificationcenter/messageidentifier/didfinishgathering.md)
  An identifier for a message about a metadata query that finished its initial result gathering.
### Identifying calendar, date, and time zone messages
- [static var calendarDayChanged: NotificationCenter.BaseMessageIdentifier<Calendar.CalendarDayChangedMessage>](notificationcenter/messageidentifier/calendardaychanged.md)
  An identifier for a message about a change in calendar day.
- [static var systemClockDidChange: NotificationCenter.BaseMessageIdentifier<Date.SystemClockDidChangeMessage>](notificationcenter/messageidentifier/systemclockdidchange.md)
  An identifier for a message about a change in the system clock.
- [static var systemTimeZoneDidChange: NotificationCenter.BaseMessageIdentifier<TimeZone.SystemTimeZoneDidChangeMessage>](notificationcenter/messageidentifier/systemtimezonedidchange.md)
  An identifier for a message about a change in the system time zone.
### Identifying locale messages
- [static var currentLocaleDidChange: NotificationCenter.BaseMessageIdentifier<Locale.CurrentLocaleDidChangeMessage>](notificationcenter/messageidentifier/currentlocaledidchange.md)
  An identifier for a message about a change in current locale.
### Identifying bundle messages
- [static var didLoad: NotificationCenter.BaseMessageIdentifier<Bundle.DidLoadMessage>](notificationcenter/messageidentifier/didload.md)
  An identifier for a message about a bundle dynamically loading a class.
### Identifying process info messages
- [static var powerStateDidChange: NotificationCenter.BaseMessageIdentifier<ProcessInfo.PowerStateDidChangeMessage>](notificationcenter/messageidentifier/powerstatedidchange.md)
  An identifier for a message about a power state change.
- [static var thermalStateDidChange: NotificationCenter.BaseMessageIdentifier<ProcessInfo.ThermalStateDidChangeMessage>](notificationcenter/messageidentifier/thermalstatedidchange.md)
  An identifier for a message about a thermal state change.
- [static var didTerminate: NotificationCenter.BaseMessageIdentifier<Process.DidTerminateMessage>](notificationcenter/messageidentifier/didterminate.md)
  An identifier for a message about a stopped task.
### Identifying file handle messages
- [static var connectionAccepted: NotificationCenter.BaseMessageIdentifier<FileHandle.ConnectionAcceptedMessage>](notificationcenter/messageidentifier/connectionaccepted.md)
  An identifier for a message about a file handle accepting a connection.
- [static var dataAvailable: NotificationCenter.BaseMessageIdentifier<FileHandle.DataAvailableMessage>](notificationcenter/messageidentifier/dataavailable.md)
  An identifier for a message about a file handle having data available for reading.
- [static var readToEndOfFileCompletion: NotificationCenter.BaseMessageIdentifier<FileHandle.ReadToEndOfFileCompletionMessage>](notificationcenter/messageidentifier/readtoendoffilecompletion.md)
  An identifier for a message about a file handle having reached the end of a file or communication channel.
- [static var readCompletion: NotificationCenter.BaseMessageIdentifier<FileHandle.ReadCompletionMessage>](notificationcenter/messageidentifier/readcompletion.md)
  An identifier for a message about a file handle having read the currently available data from a file or communication channel.
### Identifying port messages
- [static var didBecomeInvalid: NotificationCenter.BaseMessageIdentifier<Port.DidBecomeInvalidMessage>](notificationcenter/messageidentifier/didbecomeinvalid.md)
  An identifier for a message about a port becoming invalid.
### Identifying file manager messages
- [static var ubiquityIdentityDidChange: NotificationCenter.BaseMessageIdentifier<FileManager.UbiquityIdentityDidChangeMessage>](notificationcenter/messageidentifier/ubiquityidentitydidchange.md)
  An identifier for a message about a file manager’s ubiquity identity changing.
### Identifying bundle resource request messages
- [static var lowDiskSpace: NotificationCenter.BaseMessageIdentifier<NSBundleResourceRequest.LowDiskSpaceMessage>](notificationcenter/messageidentifier/lowdiskspace.md)
  An identifier for a message about the available disk space getting low.
### Identifying extension messages
- [static var didBecomeActive: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.DidBecomeActiveMessage>](notificationcenter/messageidentifier/didbecomeactive-79dvm.md)
  An identifier for a message about a host app moving from the inactive to the active state.
- [static var willResignActive: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.WillResignActiveMessage>](notificationcenter/messageidentifier/willresignactive-9z4xc.md)
  An identifier for a message about a host app moving from the active to the inactive state.
- [static var didEnterBackground: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.DidEnterBackgroundMessage>](notificationcenter/messageidentifier/didenterbackground-5gdtk.md)
  An identifier for a message about a host app beginning to run in the background.
- [static var willEnterForeground: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.WillEnterForegroundMessage>](notificationcenter/messageidentifier/willenterforeground-p1og.md)
  An identifier for a message about a host app preparing to run in the foreground.
### Identifying UIKit accessibility messages
- [static var switchControlStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.SwitchControlStatusDidChangeMessage>](notificationcenter/messageidentifier/switchcontrolstatusdidchange.md)
- [static var elementFocused: NotificationCenter.BaseMessageIdentifier<UIAccessibility.ElementFocusedMessage>](notificationcenter/messageidentifier/elementfocused.md)
- [static var reduceTransparencyStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.ReduceTransparencyStatusDidChangeMessage>](notificationcenter/messageidentifier/reducetransparencystatusdidchange.md)
- [static var announcementDidFinish: NotificationCenter.BaseMessageIdentifier<UIAccessibility.AnnouncementDidFinishMessage>](notificationcenter/messageidentifier/announcementdidfinish.md)
- [static var boldTextStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.BoldTextStatusDidChangeMessage>](notificationcenter/messageidentifier/boldtextstatusdidchange.md)
- [static var closedCaptioningStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.ClosedCaptioningStatusDidChangeMessage>](notificationcenter/messageidentifier/closedcaptioningstatusdidchange.md)
- [static var darkerSystemColorsStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.DarkerSystemColorsStatusDidChangeMessage>](notificationcenter/messageidentifier/darkersystemcolorsstatusdidchange.md)
- [static var grayscaleStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.GrayscaleStatusDidChangeMessage>](notificationcenter/messageidentifier/grayscalestatusdidchange.md)
- [static var invertColorsStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.InvertColorsStatusDidChangeMessage>](notificationcenter/messageidentifier/invertcolorsstatusdidchange.md)
- [static var assistiveTouchStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.AssistiveTouchStatusDidChangeMessage>](notificationcenter/messageidentifier/assistivetouchstatusdidchange.md)
- [static var guidedAccessStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.GuidedAccessStatusDidChangeMessage>](notificationcenter/messageidentifier/guidedaccessstatusdidchange.md)
- [static var monoAudioStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.MonoAudioStatusDidChangeMessage>](notificationcenter/messageidentifier/monoaudiostatusdidchange.md)
- [static var speakScreenStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.SpeakScreenStatusDidChangeMessage>](notificationcenter/messageidentifier/speakscreenstatusdidchange.md)
- [static var speakSelectionStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.SpeakSelectionStatusDidChangeMessage>](notificationcenter/messageidentifier/speakselectionstatusdidchange.md)
- [static var hearingDevicePairedEarDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.HearingDevicePairedEarDidChangeMessage>](notificationcenter/messageidentifier/hearingdevicepairedeardidchange.md)
- [static var reduceMotionStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.ReduceMotionStatusDidChangeMessage>](notificationcenter/messageidentifier/reducemotionstatusdidchange.md)
- [static var shakeToUndoDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.ShakeToUndoDidChangeMessage>](notificationcenter/messageidentifier/shaketoundodidchange.md)
- [static var voiceOverStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.VoiceOverStatusDidChangeMessage>](notificationcenter/messageidentifier/voiceoverstatusdidchange.md)
- [static var buttonShapesEnabledStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIAccessibility.ButtonShapesEnabledStatusDidChangeMessage>](notificationcenter/messageidentifier/buttonshapesenabledstatusdidchange.md)
### Identifying UIKit app life cycle messages
- [static var didFinishLaunching: NotificationCenter.BaseMessageIdentifier<UIApplication.DidFinishLaunchingMessage>](notificationcenter/messageidentifier/didfinishlaunching.md)
- [static var didBecomeActive: NotificationCenter.BaseMessageIdentifier<UIApplication.DidBecomeActiveMessage>](notificationcenter/messageidentifier/didbecomeactive-2hcfs.md)
- [static var didEnterBackground: NotificationCenter.BaseMessageIdentifier<UIApplication.DidEnterBackgroundMessage>](notificationcenter/messageidentifier/didenterbackground-1u5sm.md)
- [static var willEnterForeground: NotificationCenter.BaseMessageIdentifier<UIApplication.WillEnterForegroundMessage>](notificationcenter/messageidentifier/willenterforeground-95zi8.md)
- [static var willResignActive: NotificationCenter.BaseMessageIdentifier<UIApplication.WillResignActiveMessage>](notificationcenter/messageidentifier/willresignactive-4rf2p.md)
- [static var didReceiveMemoryWarning: NotificationCenter.BaseMessageIdentifier<UIApplication.DidReceiveMemoryWarningMessage>](notificationcenter/messageidentifier/didreceivememorywarning.md)
- [static var significantTimeChange: NotificationCenter.BaseMessageIdentifier<UIApplication.SignificantTimeChangeMessage>](notificationcenter/messageidentifier/significanttimechange.md)
- [static var backgroundRefreshStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIApplication.BackgroundRefreshStatusDidChangeMessage>](notificationcenter/messageidentifier/backgroundrefreshstatusdidchange.md)
- [static var userDidTakeScreenshot: NotificationCenter.BaseMessageIdentifier<UIApplication.UserDidTakeScreenshotMessage>](notificationcenter/messageidentifier/userdidtakescreenshot.md)
### Identifying UIKit content size messages
- [static var contentSizeCategoryDidChange: NotificationCenter.BaseMessageIdentifier<UIContentSizeCategory.DidChangeMessage>](notificationcenter/messageidentifier/contentsizecategorydidchange.md)
### Identifying UIKIt device messages
- [static var batteryLevelDidChange: NotificationCenter.BaseMessageIdentifier<UIDevice.BatteryLevelDidChangeMessage>](notificationcenter/messageidentifier/batteryleveldidchange.md)
- [static var batteryStateDidChange: NotificationCenter.BaseMessageIdentifier<UIDevice.BatteryStateDidChangeMessage>](notificationcenter/messageidentifier/batterystatedidchange.md)
- [static var orientationDidChange: NotificationCenter.BaseMessageIdentifier<UIDevice.OrientationDidChangeMessage>](notificationcenter/messageidentifier/orientationdidchange.md)
- [static var proximityStateDidChange: NotificationCenter.BaseMessageIdentifier<UIDevice.ProximityStateDidChangeMessage>](notificationcenter/messageidentifier/proximitystatedidchange.md)
### Identifying UIKit document messages
- [static var stateChanged: NotificationCenter.BaseMessageIdentifier<UIDocument.StateChangedMessage>](notificationcenter/messageidentifier/statechanged.md)
### Identifying UIKit pasteboard messages
- [static var changed: NotificationCenter.BaseMessageIdentifier<UIPasteboard.ChangedMessage>](notificationcenter/messageidentifier/changed-28zxj.md)
- [static var removed: NotificationCenter.BaseMessageIdentifier<UIPasteboard.RemovedMessage>](notificationcenter/messageidentifier/removed.md)
### Identifying UIKit responder messages
- [static var keyboardWillChangeFrame: NotificationCenter.BaseMessageIdentifier<UIResponder.KeyboardWillChangeFrameMessage>](notificationcenter/messageidentifier/keyboardwillchangeframe.md)
- [static var keyboardDidChangeFrame: NotificationCenter.BaseMessageIdentifier<UIResponder.KeyboardDidChangeFrameMessage>](notificationcenter/messageidentifier/keyboarddidchangeframe.md)
- [static var keyboardWillHide: NotificationCenter.BaseMessageIdentifier<UIResponder.KeyboardWillHideMessage>](notificationcenter/messageidentifier/keyboardwillhide.md)
- [static var keyboardDidHide: NotificationCenter.BaseMessageIdentifier<UIResponder.KeyboardDidHideMessage>](notificationcenter/messageidentifier/keyboarddidhide.md)
- [static var keyboardWillShow: NotificationCenter.BaseMessageIdentifier<UIResponder.KeyboardWillShowMessage>](notificationcenter/messageidentifier/keyboardwillshow.md)
- [static var keyboardDidShow: NotificationCenter.BaseMessageIdentifier<UIResponder.KeyboardDidShowMessage>](notificationcenter/messageidentifier/keyboarddidshow.md)
### Identifying UIKit screen messages
- [static var brightnessDidChange: NotificationCenter.BaseMessageIdentifier<UIScreen.BrightnessDidChangeMessage>](notificationcenter/messageidentifier/brightnessdidchange.md)
- [static var modeDidChange: NotificationCenter.BaseMessageIdentifier<UIScreen.ModeDidChangeMessage>](notificationcenter/messageidentifier/modedidchange.md)
- [static var capturedDidChange: NotificationCenter.BaseMessageIdentifier<UIScreen.CapturedDidChangeMessage>](notificationcenter/messageidentifier/captureddidchange.md)
- [static var referenceDisplayModeStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIScreen.ReferenceDisplayModeStatusDidChangeMessage>](notificationcenter/messageidentifier/referencedisplaymodestatusdidchange.md)
### Identifying UIKit text field messages
- [static var textDidBeginEditing: NotificationCenter.BaseMessageIdentifier<UITextField.TextDidBeginEditingMessage>](notificationcenter/messageidentifier/textdidbeginediting-7lt1k.md)
- [static var textDidChange: NotificationCenter.BaseMessageIdentifier<UITextField.TextDidChangeMessage>](notificationcenter/messageidentifier/textdidchange-9363k.md)
- [static var textDidEndEditing: NotificationCenter.BaseMessageIdentifier<UITextField.TextDidEndEditingMessage>](notificationcenter/messageidentifier/textdidendediting-4r8fw.md)
### Identifying UIKit text input mode messages
- [static var currentInputModeDidChange: NotificationCenter.BaseMessageIdentifier<UITextInputMode.CurrentInputModeDidChangeMessage>](notificationcenter/messageidentifier/currentinputmodedidchange.md)
### Identifying UIKit text view messages
- [static var textDidBeginEditing: NotificationCenter.BaseMessageIdentifier<UITextView.TextDidBeginEditingMessage>](notificationcenter/messageidentifier/textdidbeginediting-9y8tn.md)
- [static var textDidChange: NotificationCenter.BaseMessageIdentifier<UITextView.TextDidChangeMessage>](notificationcenter/messageidentifier/textdidchange-8ns63.md)
- [static var textDidEndEditing: NotificationCenter.BaseMessageIdentifier<UITextView.TextDidEndEditingMessage>](notificationcenter/messageidentifier/textdidendediting-6cmke.md)
### Identifying UIKit view controller messages
- [static var didBecomeVisible: NotificationCenter.BaseMessageIdentifier<UIWindow.DidBecomeVisibleMessage>](notificationcenter/messageidentifier/didbecomevisible.md)
- [static var didBecomeHidden: NotificationCenter.BaseMessageIdentifier<UIWindow.DidBecomeHiddenMessage>](notificationcenter/messageidentifier/didbecomehidden.md)
- [static var showDetailTargetDidChange: NotificationCenter.BaseMessageIdentifier<UIViewController.ShowDetailTargetDidChangeMessage>](notificationcenter/messageidentifier/showdetailtargetdidchange.md)
### Identifying UIKit focus messages
- [static var movementDidFail: NotificationCenter.BaseMessageIdentifier<UIFocusSystem.MovementDidFailMessage>](notificationcenter/messageidentifier/movementdidfail.md)
### Identifying UIKit pointer lock state messages
- [static var didChange: NotificationCenter.BaseMessageIdentifier<UIPointerLockState.DidChangeMessage>](notificationcenter/messageidentifier/didchange-7wty5.md)
### Identifying UIKit scene messages
- [static var systemProtectionDidChange: NotificationCenter.BaseMessageIdentifier<UIScene.SystemProtectionDidChangeMessage>](notificationcenter/messageidentifier/systemprotectiondidchange.md)
- [static var willConnect: NotificationCenter.BaseMessageIdentifier<UIScene.WillConnectMessage>](notificationcenter/messageidentifier/willconnect.md)
- [static var willEnterForeground: NotificationCenter.BaseMessageIdentifier<UIScene.WillEnterForegroundMessage>](notificationcenter/messageidentifier/willenterforeground-992xq.md)
- [static var didActivate: NotificationCenter.BaseMessageIdentifier<UIScene.DidActivateMessage>](notificationcenter/messageidentifier/didactivate.md)
- [static var willDeactivate: NotificationCenter.BaseMessageIdentifier<UIScene.WillDeactivateMessage>](notificationcenter/messageidentifier/willdeactivate.md)
- [static var didEnterBackground: NotificationCenter.BaseMessageIdentifier<UIScene.DidEnterBackgroundMessage>](notificationcenter/messageidentifier/didenterbackground-5fqw0.md)
### Identifying AppKit workspace messages
- [static var didHideApplication: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidHideApplicationMessage>](notificationcenter/messageidentifier/didhideapplication.md)
- [static var didUnhideApplication: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidUnhideApplicationMessage>](notificationcenter/messageidentifier/didunhideapplication.md)
- [static var willLaunchApplication: NotificationCenter.BaseMessageIdentifier<NSWorkspace.WillLaunchApplicationMessage>](notificationcenter/messageidentifier/willlaunchapplication.md)
- [static var didLaunchApplication: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidLaunchApplicationMessage>](notificationcenter/messageidentifier/didlaunchapplication.md)
- [static var willSleep: NotificationCenter.BaseMessageIdentifier<NSWorkspace.WillSleepMessage>](notificationcenter/messageidentifier/willsleep.md)
- [static var didWake: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidWakeMessage>](notificationcenter/messageidentifier/didwake.md)
- [static var didTerminateApplication: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidTerminateApplicationMessage>](notificationcenter/messageidentifier/didterminateapplication.md)
- [static var didMountVolume: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidMountVolumeMessage>](notificationcenter/messageidentifier/didmountvolume.md)
- [static var willUnmountVolume: NotificationCenter.BaseMessageIdentifier<NSWorkspace.WillUnmountVolumeMessage>](notificationcenter/messageidentifier/willunmountvolume.md)
- [static var didUnmountVolume: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidUnmountVolumeMessage>](notificationcenter/messageidentifier/didunmountvolume.md)
- [static var didActivateApplication: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidActivateApplicationMessage>](notificationcenter/messageidentifier/didactivateapplication.md)
- [static var didDeactivateApplication: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidDeactivateApplicationMessage>](notificationcenter/messageidentifier/diddeactivateapplication.md)
- [static var didRenameVolume: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidRenameVolumeMessage>](notificationcenter/messageidentifier/didrenamevolume.md)
- [static var sessionDidBecomeActive: NotificationCenter.BaseMessageIdentifier<NSWorkspace.SessionDidBecomeActiveMessage>](notificationcenter/messageidentifier/sessiondidbecomeactive.md)
- [static var sessionDidResignActive: NotificationCenter.BaseMessageIdentifier<NSWorkspace.SessionDidResignActiveMessage>](notificationcenter/messageidentifier/sessiondidresignactive.md)
- [static var didChangeFileLabels: NotificationCenter.BaseMessageIdentifier<NSWorkspace.DidChangeFileLabelsMessage>](notificationcenter/messageidentifier/didchangefilelabels.md)
- [static var screensDidSleep: NotificationCenter.BaseMessageIdentifier<NSWorkspace.ScreensDidSleepMessage>](notificationcenter/messageidentifier/screensdidsleep.md)
- [static var screensDidWake: NotificationCenter.BaseMessageIdentifier<NSWorkspace.ScreensDidWakeMessage>](notificationcenter/messageidentifier/screensdidwake.md)
- [static var activeSpaceDidChange: NotificationCenter.BaseMessageIdentifier<NSWorkspace.ActiveSpaceDidChangeMessage>](notificationcenter/messageidentifier/activespacedidchange.md)
- [static var accessibilityDisplayOptionsDidChange: NotificationCenter.BaseMessageIdentifier<NSWorkspace.AccessibilityDisplayOptionsDidChangeMessage>](notificationcenter/messageidentifier/accessibilitydisplayoptionsdidchange.md)
- [static var shouldBeginSuppressingHighDynamicRangeContent: NotificationCenter.BaseMessageIdentifier<NSApplication.ShouldBeginSuppressingHighDynamicRangeContent>](notificationcenter/messageidentifier/shouldbeginsuppressinghighdynamicrangecontent.md)
- [static var shouldEndSuppressingHighDynamicRangeContent: NotificationCenter.BaseMessageIdentifier<NSApplication.ShouldEndSuppressingHighDynamicRangeContent>](notificationcenter/messageidentifier/shouldendsuppressinghighdynamicrangecontent.md)
### Identifying EventKit messages
- [static var changed: NotificationCenter.BaseMessageIdentifier<EKEventStore.EventStoreChanged>](notificationcenter/messageidentifier/changed-50yz5.md)
  A notification posted when changes are made to the Calendar or Reminders database.
### Identifying iTunes library messages
- [static var didChange: NotificationCenter.BaseMessageIdentifier<DidChangeLibraryMessage>](notificationcenter/messageidentifier/didchange-1coqh.md)
### Type Properties
- [static var accessoryDidConnect: NotificationCenter.BaseMessageIdentifier<EAAccessoryManager.AccessoryDidConnectMessage>](notificationcenter/messageidentifier/accessorydidconnect.md)
- [static var accessoryDidDisconnect: NotificationCenter.BaseMessageIdentifier<EAAccessoryManager.AccessoryDidDisconnectMessage>](notificationcenter/messageidentifier/accessorydiddisconnect.md)
- [static var boundsDidChange: NotificationCenter.BaseMessageIdentifier<NSView.BoundsDidChangeMessage>](notificationcenter/messageidentifier/boundsdidchange.md)
- [static var colorDidChange: NotificationCenter.BaseMessageIdentifier<NSColorPanel.ColorDidChangeMessage>](notificationcenter/messageidentifier/colordidchange.md)
- [static var colorSpaceDidChange: NotificationCenter.BaseMessageIdentifier<NSScreen.ColorSpaceDidChangeMessage>](notificationcenter/messageidentifier/colorspacedidchange.md)
- [static var columnConfigurationDidChange: NotificationCenter.BaseMessageIdentifier<NSBrowser.ColumnConfigurationDidChangeMessage>](notificationcenter/messageidentifier/columnconfigurationdidchange.md)
- [static var columnDidMove: NotificationCenter.BaseMessageIdentifier<NSOutlineView.ColumnDidMoveMessage>](notificationcenter/messageidentifier/columndidmove-78e2d.md)
- [static var columnDidMove: NotificationCenter.BaseMessageIdentifier<NSTableView.ColumnDidMoveMessage>](notificationcenter/messageidentifier/columndidmove-9tkq6.md)
- [static var columnDidResize: NotificationCenter.BaseMessageIdentifier<NSOutlineView.ColumnDidResizeMessage>](notificationcenter/messageidentifier/columndidresize-5pxs4.md)
- [static var columnDidResize: NotificationCenter.BaseMessageIdentifier<NSTableView.ColumnDidResizeMessage>](notificationcenter/messageidentifier/columndidresize-7ktag.md)
- [static var contextHelpModeDidActivate: NotificationCenter.BaseMessageIdentifier<NSHelpManager.ContextHelpModeDidActivateMessage>](notificationcenter/messageidentifier/contexthelpmodedidactivate.md)
- [static var contextHelpModeDidDeactivate: NotificationCenter.BaseMessageIdentifier<NSHelpManager.ContextHelpModeDidDeactivateMessage>](notificationcenter/messageidentifier/contexthelpmodediddeactivate.md)
- [static var conversationHistoryDidUpdateMessage: NotificationCenter.BaseMessageIdentifier<ConversationHistoryManager.ConversationHistoryDidUpdate>](notificationcenter/messageidentifier/conversationhistorydidupdatemessage.md)
- [static var didAddItem: NotificationCenter.BaseMessageIdentifier<NSMenu.DidAddItemMessage>](notificationcenter/messageidentifier/didadditem.md)
- [static var didBecomeActive: NotificationCenter.BaseMessageIdentifier<NSApplication.DidBecomeActiveMessage>](notificationcenter/messageidentifier/didbecomeactive-2y311.md)
- [static var didBecomeActive: NotificationCenter.BaseMessageIdentifier<AVAudioSession.DidBecomeActiveMessage>](notificationcenter/messageidentifier/didbecomeactive-546kc.md)
- [static var didBecomeCurrent: NotificationCenter.BaseMessageIdentifier<GCController.DidBecomeCurrentMessage>](notificationcenter/messageidentifier/didbecomecurrent-9p0n4.md)
  The identifier of the message that posts after a game controller becomes the most recently used controller.
- [static var didBecomeCurrent: NotificationCenter.BaseMessageIdentifier<GCMouse.DidBecomeCurrentMessage>](notificationcenter/messageidentifier/didbecomecurrent-9zfc.md)
  The identifier of the message that posts after a mouse becomes the most recently used mouse.
- [static var didBecomeInactive: NotificationCenter.BaseMessageIdentifier<AVAudioSession.DidBecomeInactiveMessage>](notificationcenter/messageidentifier/didbecomeinactive.md)
- [static var didBecomeKey: NotificationCenter.BaseMessageIdentifier<NSWindow.DidBecomeKeyMessage>](notificationcenter/messageidentifier/didbecomekey-3qijm.md)
- [static var didBecomeKey: NotificationCenter.BaseMessageIdentifier<UIWindow.DidBecomeKeyMessage>](notificationcenter/messageidentifier/didbecomekey-6kgub.md)
- [static var didBecomeMain: NotificationCenter.BaseMessageIdentifier<NSWindow.DidBecomeMainMessage>](notificationcenter/messageidentifier/didbecomemain.md)
- [static var didBeginEditing: NotificationCenter.BaseMessageIdentifier<NSTextView.DidBeginEditingMessage>](notificationcenter/messageidentifier/didbeginediting.md)
- [static var didBeginTracking: NotificationCenter.BaseMessageIdentifier<NSMenu.DidBeginTrackingMessage>](notificationcenter/messageidentifier/didbegintracking.md)
- [static var didChange: NotificationCenter.BaseMessageIdentifier<NSFontCollection.DidChangeMessage>](notificationcenter/messageidentifier/didchange-1ebzb.md)
- [static var didChange: NotificationCenter.BaseMessageIdentifier<NSColorList.DidChangeMessage>](notificationcenter/messageidentifier/didchange-96f1i.md)
- [static var didChange: NotificationCenter.BaseMessageIdentifier<NSTextView.DidChangeMessage>](notificationcenter/messageidentifier/didchange-ywl6.md)
- [static var didChangeAutomaticCapitalization: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticCapitalizationMessage>](notificationcenter/messageidentifier/didchangeautomaticcapitalization.md)
- [static var didChangeAutomaticDashSubstitution: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticDashSubstitutionMessage>](notificationcenter/messageidentifier/didchangeautomaticdashsubstitution.md)
- [static var didChangeAutomaticInlinePrediction: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticInlinePredictionMessage>](notificationcenter/messageidentifier/didchangeautomaticinlineprediction.md)
- [static var didChangeAutomaticPeriodSubstitution: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticPeriodSubstitutionMessage>](notificationcenter/messageidentifier/didchangeautomaticperiodsubstitution.md)
- [static var didChangeAutomaticQuoteSubstitution: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticQuoteSubstitutionMessage>](notificationcenter/messageidentifier/didchangeautomaticquotesubstitution.md)
- [static var didChangeAutomaticSpellingCorrection: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticSpellingCorrectionMessage>](notificationcenter/messageidentifier/didchangeautomaticspellingcorrection.md)
- [static var didChangeAutomaticTextCompletion: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticTextCompletionMessage>](notificationcenter/messageidentifier/didchangeautomatictextcompletion.md)
- [static var didChangeAutomaticTextReplacement: NotificationCenter.BaseMessageIdentifier<NSSpellChecker.DidChangeAutomaticTextReplacementMessage>](notificationcenter/messageidentifier/didchangeautomatictextreplacement.md)
- [static var didChangeBackingProperties: NotificationCenter.BaseMessageIdentifier<NSWindow.DidChangeBackingPropertiesMessage>](notificationcenter/messageidentifier/didchangebackingproperties.md)
- [static var didChangeItem: NotificationCenter.BaseMessageIdentifier<NSMenu.DidChangeItemMessage>](notificationcenter/messageidentifier/didchangeitem.md)
- [static var didChangeOcclusionState: NotificationCenter.BaseMessageIdentifier<NSWindow.DidChangeOcclusionStateMessage>](notificationcenter/messageidentifier/didchangeocclusionstate-5853a.md)
- [static var didChangeOcclusionState: NotificationCenter.BaseMessageIdentifier<NSApplication.DidChangeOcclusionStateMessage>](notificationcenter/messageidentifier/didchangeocclusionstate-99vn6.md)
- [static var didChangeScreen: NotificationCenter.BaseMessageIdentifier<NSWindow.DidChangeScreenMessage>](notificationcenter/messageidentifier/didchangescreen.md)
- [static var didChangeScreenParameters: NotificationCenter.BaseMessageIdentifier<NSApplication.DidChangeScreenParametersMessage>](notificationcenter/messageidentifier/didchangescreenparameters.md)
- [static var didChangeScreenProfile: NotificationCenter.BaseMessageIdentifier<NSWindow.DidChangeScreenProfileMessage>](notificationcenter/messageidentifier/didchangescreenprofile.md)
- [static var didChangeSelection: NotificationCenter.BaseMessageIdentifier<NSTextView.DidChangeSelectionMessage>](notificationcenter/messageidentifier/didchangeselection.md)
- [static var didChangeTypingAttributes: NotificationCenter.BaseMessageIdentifier<NSTextView.DidChangeTypingAttributesMessage>](notificationcenter/messageidentifier/didchangetypingattributes.md)
- [static var didClose: NotificationCenter.BaseMessageIdentifier<NSPopover.DidCloseMessage>](notificationcenter/messageidentifier/didclose.md)
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCMouse.DidConnectMessage>](notificationcenter/messageidentifier/didconnect-2pidr.md)
  The identifier of the message that posts after a mouse accessory connects to the device.
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCRacingWheel.DidConnectMessage>](notificationcenter/messageidentifier/didconnect-39qlx.md)
  The identifier of the message that posts after a racing wheel accessory connects to the device.
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCController.DidConnectMessage>](notificationcenter/messageidentifier/didconnect-3d7x9.md)
  The identifier of the message that posts after a game controller accessory connects to the device.
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCKeyboard.DidConnectMessage>](notificationcenter/messageidentifier/didconnect-6zuxs.md)
  The identifier of the message that posts after a keyboard accessory connects to the device.
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCSpatialAccessory.DidConnectMessage>](notificationcenter/messageidentifier/didconnect-oq29.md)
  The identifier of the message that posts after a spatial accessory connects to the device.
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCStylus.DidConnectMessage>](notificationcenter/messageidentifier/didconnect-wf9.md)
  The identifier of the message that posts after a stylus accessory connects to the device.
- [static var didDeminiaturize: NotificationCenter.BaseMessageIdentifier<NSWindow.DidDeminiaturizeMessage>](notificationcenter/messageidentifier/diddeminiaturize.md)
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCRacingWheel.DidDisconnectMessage>](notificationcenter/messageidentifier/diddisconnect-127wj.md)
  The identifier of the message that posts after a racing wheel accessory disconnects from the device.
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCStylus.DidDisconnectMessage>](notificationcenter/messageidentifier/diddisconnect-3p6qi.md)
  The identifier of the message that posts after a stylus accessory disconnects from the device.
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCMouse.DidDisconnectMessage>](notificationcenter/messageidentifier/diddisconnect-5s9vw.md)
  The identifier of the message that posts after a mouse accessory disconnects from the device.
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCKeyboard.DidDisconnectMessage>](notificationcenter/messageidentifier/diddisconnect-97jtl.md)
  The identifier of the message that posts after a keyboard accessory disconnects from the device.
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCSpatialAccessory.DidDisconnectMessage>](notificationcenter/messageidentifier/diddisconnect-9qi2f.md)
  The identifier of the message that posts after a spatial accessory disconnects from the device.
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCController.DidDisconnectMessage>](notificationcenter/messageidentifier/diddisconnect-9ymbl.md)
  The identifier of the message that posts after a game controller accessory disconnects from the device.
- [static var didEndEditing: NotificationCenter.BaseMessageIdentifier<NSTextView.DidEndEditingMessage>](notificationcenter/messageidentifier/didendediting.md)
- [static var didEndLiveMagnify: NotificationCenter.BaseMessageIdentifier<NSScrollView.DidEndLiveMagnifyMessage>](notificationcenter/messageidentifier/didendlivemagnify.md)
- [static var didEndLiveResize: NotificationCenter.BaseMessageIdentifier<NSWindow.DidEndLiveResizeMessage>](notificationcenter/messageidentifier/didendliveresize.md)
- [static var didEndLiveScroll: NotificationCenter.BaseMessageIdentifier<NSScrollView.DidEndLiveScrollMessage>](notificationcenter/messageidentifier/didendlivescroll.md)
- [static var didEndSheet: NotificationCenter.BaseMessageIdentifier<NSWindow.DidEndSheetMessage>](notificationcenter/messageidentifier/didendsheet.md)
- [static var didEndTracking: NotificationCenter.BaseMessageIdentifier<NSMenu.DidEndTrackingMessage>](notificationcenter/messageidentifier/didendtracking.md)
- [static var didEnterFullScreen: NotificationCenter.BaseMessageIdentifier<NSWindow.DidEnterFullScreenMessage>](notificationcenter/messageidentifier/didenterfullscreen.md)
- [static var didEnterVersionBrowser: NotificationCenter.BaseMessageIdentifier<NSWindow.DidEnterVersionBrowserMessage>](notificationcenter/messageidentifier/didenterversionbrowser.md)
- [static var didExitFullScreen: NotificationCenter.BaseMessageIdentifier<NSWindow.DidExitFullScreenMessage>](notificationcenter/messageidentifier/didexitfullscreen.md)
- [static var didExitVersionBrowser: NotificationCenter.BaseMessageIdentifier<NSWindow.DidExitVersionBrowserMessage>](notificationcenter/messageidentifier/didexitversionbrowser.md)
- [static var didExpose: NotificationCenter.BaseMessageIdentifier<NSWindow.DidExposeMessage>](notificationcenter/messageidentifier/didexpose.md)
- [static var didFinishRestoringWindows: NotificationCenter.BaseMessageIdentifier<NSApplication.DidFinishRestoringWindowsMessage>](notificationcenter/messageidentifier/didfinishrestoringwindows.md)
- [static var didHide: NotificationCenter.BaseMessageIdentifier<NSApplication.DidHideMessage>](notificationcenter/messageidentifier/didhide.md)
- [static var didLiveScroll: NotificationCenter.BaseMessageIdentifier<NSScrollView.DidLiveScrollMessage>](notificationcenter/messageidentifier/didlivescroll.md)
- [static var didMergeChanges: NotificationCenter.BaseMessageIdentifier<NSManagedObjectContext.DidMergeChangesMessage>](notificationcenter/messageidentifier/didmergechanges.md)
- [static var didMergeChangesAsync: NotificationCenter.BaseMessageIdentifier<NSManagedObjectContext.DidMergeChangesAsyncMessage>](notificationcenter/messageidentifier/didmergechangesasync.md)
- [static var didMiniaturize: NotificationCenter.BaseMessageIdentifier<NSWindow.DidMiniaturizeMessage>](notificationcenter/messageidentifier/didminiaturize.md)
- [static var didMove: NotificationCenter.BaseMessageIdentifier<NSWindow.DidMoveMessage>](notificationcenter/messageidentifier/didmove.md)
- [static var didMoveToWritableLocation: NotificationCenter.BaseMessageIdentifier<UIDocument.DidMoveToWritableLocationMessage>](notificationcenter/messageidentifier/didmovetowritablelocation.md)
- [static var didRemoveItem: NotificationCenter.BaseMessageIdentifier<NSToolbar.DidRemoveItemMessage>](notificationcenter/messageidentifier/didremoveitem-4hapv.md)
- [static var didRemoveItem: NotificationCenter.BaseMessageIdentifier<NSMenu.DidRemoveItemMessage>](notificationcenter/messageidentifier/didremoveitem-bimz.md)
- [static var didResignActive: NotificationCenter.BaseMessageIdentifier<NSApplication.DidResignActiveMessage>](notificationcenter/messageidentifier/didresignactive.md)
- [static var didResignKey: NotificationCenter.BaseMessageIdentifier<UIWindow.DidResignKeyMessage>](notificationcenter/messageidentifier/didresignkey-11hzh.md)
- [static var didResignKey: NotificationCenter.BaseMessageIdentifier<NSWindow.DidResignKeyMessage>](notificationcenter/messageidentifier/didresignkey-2dgp0.md)
- [static var didResignMain: NotificationCenter.BaseMessageIdentifier<NSWindow.DidResignMainMessage>](notificationcenter/messageidentifier/didresignmain.md)
- [static var didResize: NotificationCenter.BaseMessageIdentifier<NSWindow.DidResizeMessage>](notificationcenter/messageidentifier/didresize.md)
- [static var didResizeSubviews: NotificationCenter.BaseMessageIdentifier<NSSplitView.DidResizeSubviewsMessage>](notificationcenter/messageidentifier/didresizesubviews.md)
- [static var didSave: NotificationCenter.BaseMessageIdentifier<NSManagedObjectContext.DidSaveMessage>](notificationcenter/messageidentifier/didsave.md)
- [static var didSaveObjectIDs: NotificationCenter.BaseMessageIdentifier<NSManagedObjectContext.DidSaveObjectIDsMessage>](notificationcenter/messageidentifier/didsaveobjectids.md)
- [static var didSaveObjectIDsAsync: NotificationCenter.BaseMessageIdentifier<NSManagedObjectContext.DidSaveObjectIDsAsyncMessage>](notificationcenter/messageidentifier/didsaveobjectidsasync.md)
- [static var didSendAction: NotificationCenter.BaseMessageIdentifier<NSMenu.DidSendActionMessage>](notificationcenter/messageidentifier/didsendaction.md)
- [static var didShow: NotificationCenter.BaseMessageIdentifier<NSPopover.DidShowMessage>](notificationcenter/messageidentifier/didshow.md)
- [static var didStopBeingCurrent: NotificationCenter.BaseMessageIdentifier<GCMouse.DidStopBeingCurrentMessage>](notificationcenter/messageidentifier/didstopbeingcurrent-2sc31.md)
  The identifier of the message that posts after a mouse stops being longer the most recently used mouse.
- [static var didStopBeingCurrent: NotificationCenter.BaseMessageIdentifier<GCController.DidStopBeingCurrentMessage>](notificationcenter/messageidentifier/didstopbeingcurrent-9pdq9.md)
  The identifier of the message that posts after a game controller stops being longer the most recently used controller.
- [static var didUnhide: NotificationCenter.BaseMessageIdentifier<NSApplication.DidUnhideMessage>](notificationcenter/messageidentifier/didunhide.md)
- [static var didUpdate: NotificationCenter.BaseMessageIdentifier<UIFocusSystem.DidUpdateMessage>](notificationcenter/messageidentifier/didupdate-p3fm.md)
- [static var didUpdate: NotificationCenter.BaseMessageIdentifier<NSWindow.DidUpdateMessage>](notificationcenter/messageidentifier/didupdate-vu3m.md)
- [static var didUpdateWindows: NotificationCenter.BaseMessageIdentifier<NSApplication.DidUpdateWindowsMessage>](notificationcenter/messageidentifier/didupdatewindows.md)
- [static var eventChanged: NotificationCenter.BaseMessageIdentifier<NSPersistentCloudKitContainer.EventChangedMessage>](notificationcenter/messageidentifier/eventchanged.md)
- [static var fontSetChanged: NotificationCenter.BaseMessageIdentifier<NSFont.FontSetChangedMessage>](notificationcenter/messageidentifier/fontsetchanged.md)
- [static var frameDidChange: NotificationCenter.BaseMessageIdentifier<NSView.FrameDidChangeMessage>](notificationcenter/messageidentifier/framedidchange.md)
- [static var indexDidUpdate: NotificationCenter.BaseMessageIdentifier<NSCoreDataCoreSpotlightDelegate.IndexDidUpdateMessage>](notificationcenter/messageidentifier/indexdidupdate.md)
- [static var itemDidCollapse: NotificationCenter.BaseMessageIdentifier<NSOutlineView.ItemDidCollapseMessage>](notificationcenter/messageidentifier/itemdidcollapse.md)
- [static var itemDidExpand: NotificationCenter.BaseMessageIdentifier<NSOutlineView.ItemDidExpandMessage>](notificationcenter/messageidentifier/itemdidexpand.md)
- [static var itemWillCollapse: NotificationCenter.BaseMessageIdentifier<NSOutlineView.ItemWillCollapseMessage>](notificationcenter/messageidentifier/itemwillcollapse.md)
- [static var itemWillExpand: NotificationCenter.BaseMessageIdentifier<NSOutlineView.ItemWillExpandMessage>](notificationcenter/messageidentifier/itemwillexpand.md)
- [static var keyboardSelectionDidChange: NotificationCenter.BaseMessageIdentifier<NSTextInputContext.KeyboardSelectionDidChangeMessage>](notificationcenter/messageidentifier/keyboardselectiondidchange.md)
- [static var objectsDidChange: NotificationCenter.BaseMessageIdentifier<NSManagedObjectContext.ObjectsDidChangeMessage>](notificationcenter/messageidentifier/objectsdidchange.md)
- [static var preferredScrollerStyleDidChange: NotificationCenter.BaseMessageIdentifier<NSScroller.PreferredScrollerStyleDidChangeMessage>](notificationcenter/messageidentifier/preferredscrollerstyledidchange.md)
- [static var protectedDataDidBecomeAvailable: NotificationCenter.BaseMessageIdentifier<NSApplication.ProtectedDataDidBecomeAvailableMessage>](notificationcenter/messageidentifier/protecteddatadidbecomeavailable-3di2c.md)
- [static var protectedDataDidBecomeAvailable: NotificationCenter.BaseMessageIdentifier<UIApplication.ProtectedDataDidBecomeAvailableMessage>](notificationcenter/messageidentifier/protecteddatadidbecomeavailable-6h44m.md)
- [static var protectedDataWillBecomeUnavailable: NotificationCenter.BaseMessageIdentifier<NSApplication.ProtectedDataWillBecomeUnavailableMessage>](notificationcenter/messageidentifier/protecteddatawillbecomeunavailable-1izcs.md)
- [static var protectedDataWillBecomeUnavailable: NotificationCenter.BaseMessageIdentifier<UIApplication.ProtectedDataWillBecomeUnavailableMessage>](notificationcenter/messageidentifier/protecteddatawillbecomeunavailable-3n08h.md)
- [static var radioAccessTechnologyDidChange: NotificationCenter.BaseMessageIdentifier<CTTelephonyNetworkInfo.RadioAccessTechnologyDidChangeMessage>](notificationcenter/messageidentifier/radioaccesstechnologydidchange.md)
- [static var registrationsChanged: NotificationCenter.BaseMessageIdentifier<AVAudioUnitComponentManager.RegistrationsChangedMessage>](notificationcenter/messageidentifier/registrationschanged.md)
- [static var registryDidChange: NotificationCenter.BaseMessageIdentifier<NSImageRep.RegistryDidChangeMessage>](notificationcenter/messageidentifier/registrydidchange.md)
- [static var remoteChange: NotificationCenter.BaseMessageIdentifier<NSPersistentStoreCoordinator.RemoteChangeMessage>](notificationcenter/messageidentifier/remotechange.md)
- [static var resumptionRecommendation: NotificationCenter.BaseMessageIdentifier<AVAudioSession.ResumptionRecommendationMessage>](notificationcenter/messageidentifier/resumptionrecommendation.md)
- [static var rowsDidChange: NotificationCenter.BaseMessageIdentifier<NSRuleEditor.RowsDidChangeMessage>](notificationcenter/messageidentifier/rowsdidchange.md)
- [static var selectedAlternativeString: NotificationCenter.BaseMessageIdentifier<NSTextAlternatives.SelectedAlternativeStringMessage>](notificationcenter/messageidentifier/selectedalternativestring.md)
- [static var selectionDidChange: NotificationCenter.BaseMessageIdentifier<UITableView.SelectionDidChangeMessage>](notificationcenter/messageidentifier/selectiondidchange-2akj4.md)
- [static var selectionDidChange: NotificationCenter.BaseMessageIdentifier<NSTableView.SelectionDidChangeMessage>](notificationcenter/messageidentifier/selectiondidchange-676mh.md)
- [static var selectionDidChange: NotificationCenter.BaseMessageIdentifier<NSComboBox.SelectionDidChangeMessage>](notificationcenter/messageidentifier/selectiondidchange-72x2p.md)
- [static var selectionDidChange: NotificationCenter.BaseMessageIdentifier<NSOutlineView.SelectionDidChangeMessage>](notificationcenter/messageidentifier/selectiondidchange-7qmnc.md)
- [static var selectionIsChanging: NotificationCenter.BaseMessageIdentifier<NSComboBox.SelectionIsChangingMessage>](notificationcenter/messageidentifier/selectionischanging-2i647.md)
- [static var selectionIsChanging: NotificationCenter.BaseMessageIdentifier<NSTableView.SelectionIsChangingMessage>](notificationcenter/messageidentifier/selectionischanging-5u4tc.md)
- [static var selectionIsChanging: NotificationCenter.BaseMessageIdentifier<NSOutlineView.SelectionIsChangingMessage>](notificationcenter/messageidentifier/selectionischanging-abh0.md)
- [static var storesDidChange: NotificationCenter.BaseMessageIdentifier<NSPersistentStoreCoordinator.StoresDidChangeMessage>](notificationcenter/messageidentifier/storesdidchange.md)
- [static var storesDidChangeAsync: NotificationCenter.BaseMessageIdentifier<NSPersistentStoreCoordinator.StoresDidChangeAsyncMessage>](notificationcenter/messageidentifier/storesdidchangeasync.md)
- [static var systemColorsDidChange: NotificationCenter.BaseMessageIdentifier<NSColor.SystemColorsDidChangeMessage>](notificationcenter/messageidentifier/systemcolorsdidchange.md)
- [static var tagsDidChange: NotificationCenter.BaseMessageIdentifier<AVAudioUnitComponent.TagsDidChangeMessage>](notificationcenter/messageidentifier/tagsdidchange.md)
- [static var textDidBeginEditing: NotificationCenter.BaseMessageIdentifier<NSControl.TextDidBeginEditingMessage>](notificationcenter/messageidentifier/textdidbeginediting-45vc.md)
- [static var textDidChange: NotificationCenter.BaseMessageIdentifier<NSControl.TextDidChangeMessage>](notificationcenter/messageidentifier/textdidchange-5j4s4.md)
- [static var textDidEndEditing: NotificationCenter.BaseMessageIdentifier<NSControl.TextDidEndEditingMessage>](notificationcenter/messageidentifier/textdidendediting-5yxiy.md)
- [static var textMessageAvailabilityDidChange: NotificationCenter.BaseMessageIdentifier<MFMessageComposeViewController.TextMessageAvailabilityDidChangeMessage>](notificationcenter/messageidentifier/textmessageavailabilitydidchange.md)
  Notification posted when text message availability changes.
- [static var tokensDidExpire: NotificationCenter.BaseMessageIdentifier<ManagedSettingsStore.TokenExpiryMessage>](notificationcenter/messageidentifier/tokensdidexpire.md)
- [static var userPreferencesDidChange: NotificationCenter.BaseMessageIdentifier<HKHealthStore.HKUserPreferencesDidChangeMessage>](notificationcenter/messageidentifier/userpreferencesdidchange.md)
- [static var willAddItem: NotificationCenter.BaseMessageIdentifier<NSToolbar.WillAddItemMessage>](notificationcenter/messageidentifier/willadditem.md)
- [static var willBecomeActive: NotificationCenter.BaseMessageIdentifier<NSApplication.WillBecomeActiveMessage>](notificationcenter/messageidentifier/willbecomeactive.md)
- [static var willBeginSheet: NotificationCenter.BaseMessageIdentifier<NSWindow.WillBeginSheetMessage>](notificationcenter/messageidentifier/willbeginsheet.md)
- [static var willChangeNotifyingTextView: NotificationCenter.BaseMessageIdentifier<NSTextView.WillChangeNotifyingTextViewMessage>](notificationcenter/messageidentifier/willchangenotifyingtextview.md)
- [static var willClose: NotificationCenter.BaseMessageIdentifier<NSPopover.WillCloseMessage>](notificationcenter/messageidentifier/willclose-2wsvs.md)
- [static var willClose: NotificationCenter.BaseMessageIdentifier<NSWindow.WillCloseMessage>](notificationcenter/messageidentifier/willclose-4565q.md)
- [static var willDismiss: NotificationCenter.BaseMessageIdentifier<NSComboBox.WillDismissMessage>](notificationcenter/messageidentifier/willdismiss.md)
- [static var willEnterFullScreen: NotificationCenter.BaseMessageIdentifier<NSWindow.WillEnterFullScreenMessage>](notificationcenter/messageidentifier/willenterfullscreen.md)
- [static var willEnterVersionBrowser: NotificationCenter.BaseMessageIdentifier<NSWindow.WillEnterVersionBrowserMessage>](notificationcenter/messageidentifier/willenterversionbrowser.md)
- [static var willExitFullScreen: NotificationCenter.BaseMessageIdentifier<NSWindow.WillExitFullScreenMessage>](notificationcenter/messageidentifier/willexitfullscreen.md)
- [static var willExitVersionBrowser: NotificationCenter.BaseMessageIdentifier<NSWindow.WillExitVersionBrowserMessage>](notificationcenter/messageidentifier/willexitversionbrowser.md)
- [static var willFinishLaunching: NotificationCenter.BaseMessageIdentifier<NSApplication.WillFinishLaunchingMessage>](notificationcenter/messageidentifier/willfinishlaunching.md)
- [static var willHide: NotificationCenter.BaseMessageIdentifier<NSApplication.WillHideMessage>](notificationcenter/messageidentifier/willhide.md)
- [static var willMiniaturize: NotificationCenter.BaseMessageIdentifier<NSWindow.WillMiniaturizeMessage>](notificationcenter/messageidentifier/willminiaturize.md)
- [static var willMove: NotificationCenter.BaseMessageIdentifier<NSWindow.WillMoveMessage>](notificationcenter/messageidentifier/willmove.md)
- [static var willPopUp: NotificationCenter.BaseMessageIdentifier<NSComboBox.WillPopUpMessage>](notificationcenter/messageidentifier/willpopup-4czk2.md)
- [static var willPopUp: NotificationCenter.BaseMessageIdentifier<NSPopUpButton.WillPopUpMessage>](notificationcenter/messageidentifier/willpopup-81zuu.md)
- [static var willPopUp: NotificationCenter.BaseMessageIdentifier<NSPopUpButtonCell.WillPopUpMessage>](notificationcenter/messageidentifier/willpopup-8ycpp.md)
- [static var willResignActive: NotificationCenter.BaseMessageIdentifier<NSApplication.WillResignActiveMessage>](notificationcenter/messageidentifier/willresignactive-9aumz.md)
- [static var willResizeSubviews: NotificationCenter.BaseMessageIdentifier<NSSplitView.WillResizeSubviewsMessage>](notificationcenter/messageidentifier/willresizesubviews.md)
- [static var willSave: NotificationCenter.BaseMessageIdentifier<NSManagedObjectContext.WillSaveMessage>](notificationcenter/messageidentifier/willsave.md)
- [static var willSendAction: NotificationCenter.BaseMessageIdentifier<NSMenu.WillSendActionMessage>](notificationcenter/messageidentifier/willsendaction.md)
- [static var willShow: NotificationCenter.BaseMessageIdentifier<NSPopover.WillShowMessage>](notificationcenter/messageidentifier/willshow.md)
- [static var willStartLiveMagnify: NotificationCenter.BaseMessageIdentifier<NSScrollView.WillStartLiveMagnifyMessage>](notificationcenter/messageidentifier/willstartlivemagnify.md)
- [static var willStartLiveResize: NotificationCenter.BaseMessageIdentifier<NSWindow.WillStartLiveResizeMessage>](notificationcenter/messageidentifier/willstartliveresize.md)
- [static var willStartLiveScroll: NotificationCenter.BaseMessageIdentifier<NSScrollView.WillStartLiveScrollMessage>](notificationcenter/messageidentifier/willstartlivescroll.md)
- [static var willTerminate: NotificationCenter.BaseMessageIdentifier<UIApplication.WillTerminateMessage>](notificationcenter/messageidentifier/willterminate-1u238.md)
- [static var willTerminate: NotificationCenter.BaseMessageIdentifier<NSApplication.WillTerminateMessage>](notificationcenter/messageidentifier/willterminate-7lu3s.md)
- [static var willUnhide: NotificationCenter.BaseMessageIdentifier<NSApplication.WillUnhideMessage>](notificationcenter/messageidentifier/willunhide.md)
- [static var willUpdateWindows: NotificationCenter.BaseMessageIdentifier<NSApplication.WillUpdateWindowsMessage>](notificationcenter/messageidentifier/willupdatewindows.md)

## Relationships

### Conforming Types
- [NotificationCenter.BaseMessageIdentifier](notificationcenter/basemessageidentifier.md)

## See Also

- [NotificationCenter.BaseMessageIdentifier](notificationcenter/basemessageidentifier.md)
  A type for use when defining optional Message identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier)*