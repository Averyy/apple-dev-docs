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
### Identifying undo manager messages
- [static var willUndoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.WillUndoChangeMessage>](notificationcenter/messageidentifier/willundochange.md)
  An identifier for the undo manager will undo change message.
- [static var didUndoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.DidUndoChangeMessage>](notificationcenter/messageidentifier/didundochange.md)
  An identifier for the undo manager did undo change message.
- [static var willRedoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.WillRedoChangeMessage>](notificationcenter/messageidentifier/willredochange.md)
  An identifier for the undo manager will redo change message.
- [static var didRedoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.DidRedoChangeMessage>](notificationcenter/messageidentifier/didredochange.md)
  An identifier for the undo manager did redo change message.
- [static var checkpoint: NotificationCenter.BaseMessageIdentifier<UndoManager.CheckpointMessage>](notificationcenter/messageidentifier/checkpoint.md)
  An identifier for the undo manager checkpoint message.
- [static var didOpenUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.DidOpenUndoGroupMessage>](notificationcenter/messageidentifier/didopenundogroup.md)
  An identifier for the undo manager did open undo group message.
- [static var willCloseUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.WillCloseUndoGroupMessage>](notificationcenter/messageidentifier/willcloseundogroup.md)
  An identifier for the undo manager will close undo group message.
- [static var didCloseUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.DidCloseUndoGroupMessage>](notificationcenter/messageidentifier/didcloseundogroup.md)
  An identifier for the undo manager did close undo group message.
### Identifying defaults messages
- [static var didChange: NotificationCenter.BaseMessageIdentifier<UserDefaults.DidChangeMessage>](notificationcenter/messageidentifier/didchange-187tw.md)
- [static var sizeLimitExceeded: NotificationCenter.BaseMessageIdentifier<UserDefaults.SizeLimitExceededMessage>](notificationcenter/messageidentifier/sizelimitexceeded.md)
### Identifying metadata query messages
- [static var didStartGathering: NotificationCenter.BaseMessageIdentifier<NSMetadataQuery.DidStartGatheringMessage>](notificationcenter/messageidentifier/didstartgathering.md)
- [static var didFinishGathering: NotificationCenter.BaseMessageIdentifier<NSMetadataQuery.DidFinishGatheringMessage>](notificationcenter/messageidentifier/didfinishgathering.md)
### Identifying calendar, date, and time zone messages
- [static var calendarDayChanged: NotificationCenter.BaseMessageIdentifier<Calendar.CalendarDayChangedMessage>](notificationcenter/messageidentifier/calendardaychanged.md)
- [static var systemClockDidChange: NotificationCenter.BaseMessageIdentifier<Date.SystemClockDidChangeMessage>](notificationcenter/messageidentifier/systemclockdidchange.md)
- [static var systemTimeZoneDidChange: NotificationCenter.BaseMessageIdentifier<TimeZone.SystemTimeZoneDidChangeMessage>](notificationcenter/messageidentifier/systemtimezonedidchange.md)
### Identifying locale messages
- [static var currentLocaleDidChange: NotificationCenter.BaseMessageIdentifier<Locale.CurrentLocaleDidChangeMessage>](notificationcenter/messageidentifier/currentlocaledidchange.md)
### Identifying bundle messages
- [static var didLoad: NotificationCenter.BaseMessageIdentifier<Bundle.DidLoadMessage>](notificationcenter/messageidentifier/didload.md)
### Identifying process info messages
- [static var powerStateDidChange: NotificationCenter.BaseMessageIdentifier<ProcessInfo.PowerStateDidChangeMessage>](notificationcenter/messageidentifier/powerstatedidchange.md)
- [static var thermalStateDidChange: NotificationCenter.BaseMessageIdentifier<ProcessInfo.ThermalStateDidChangeMessage>](notificationcenter/messageidentifier/thermalstatedidchange.md)
- [static var didTerminate: NotificationCenter.BaseMessageIdentifier<Process.DidTerminateMessage>](notificationcenter/messageidentifier/didterminate.md)
### Identifying file handle messages
- [static var connectionAccepted: NotificationCenter.BaseMessageIdentifier<FileHandle.ConnectionAcceptedMessage>](notificationcenter/messageidentifier/connectionaccepted.md)
- [static var dataAvailable: NotificationCenter.BaseMessageIdentifier<FileHandle.DataAvailableMessage>](notificationcenter/messageidentifier/dataavailable.md)
- [static var readToEndOfFileCompletion: NotificationCenter.BaseMessageIdentifier<FileHandle.ReadToEndOfFileCompletionMessage>](notificationcenter/messageidentifier/readtoendoffilecompletion.md)
- [static var readCompletion: NotificationCenter.BaseMessageIdentifier<FileHandle.ReadCompletionMessage>](notificationcenter/messageidentifier/readcompletion.md)
### Identifying port messages
- [static var didBecomeInvalid: NotificationCenter.BaseMessageIdentifier<Port.DidBecomeInvalidMessage>](notificationcenter/messageidentifier/didbecomeinvalid.md)
### Identifying file manager messages
- [static var ubiquityIdentityDidChange: NotificationCenter.BaseMessageIdentifier<FileManager.UbiquityIdentityDidChangeMessage>](notificationcenter/messageidentifier/ubiquityidentitydidchange.md)
### Identifying bundle resource request messages
- [static var lowDiskSpace: NotificationCenter.BaseMessageIdentifier<NSBundleResourceRequest.LowDiskSpaceMessage>](notificationcenter/messageidentifier/lowdiskspace.md)
### Identifying extension messages
- [static var didBecomeActive: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.DidBecomeActiveMessage>](notificationcenter/messageidentifier/didbecomeactive-79dvm.md)
- [static var didEnterBackground: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.DidEnterBackgroundMessage>](notificationcenter/messageidentifier/didenterbackground-5gdtk.md)
- [static var willEnterForeground: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.WillEnterForegroundMessage>](notificationcenter/messageidentifier/willenterforeground-p1og.md)
- [static var willResignActive: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.WillResignActiveMessage>](notificationcenter/messageidentifier/willresignactive-9z4xc.md)
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
- [static var willTerminate: NotificationCenter.BaseMessageIdentifier<UIApplication.WillTerminateMessage>](notificationcenter/messageidentifier/willterminate.md)
- [static var didReceiveMemoryWarning: NotificationCenter.BaseMessageIdentifier<UIApplication.DidReceiveMemoryWarningMessage>](notificationcenter/messageidentifier/didreceivememorywarning.md)
- [static var significantTimeChange: NotificationCenter.BaseMessageIdentifier<UIApplication.SignificantTimeChangeMessage>](notificationcenter/messageidentifier/significanttimechange.md)
- [static var backgroundRefreshStatusDidChange: NotificationCenter.BaseMessageIdentifier<UIApplication.BackgroundRefreshStatusDidChangeMessage>](notificationcenter/messageidentifier/backgroundrefreshstatusdidchange.md)
- [static var userDidTakeScreenshot: NotificationCenter.BaseMessageIdentifier<UIApplication.UserDidTakeScreenshotMessage>](notificationcenter/messageidentifier/userdidtakescreenshot.md)
- [static var protectedDataDidBecomeAvailable: NotificationCenter.BaseMessageIdentifier<UIApplication.ProtectedDataDidBecomeAvailableMessage>](notificationcenter/messageidentifier/protecteddatadidbecomeavailable.md)
- [static var protectedDataWillBecomeUnavailable: NotificationCenter.BaseMessageIdentifier<UIApplication.ProtectedDataWillBecomeUnavailableMessage>](notificationcenter/messageidentifier/protecteddatawillbecomeunavailable.md)
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
### Identifying UIKit table messages
- [static var selectionDidChange: NotificationCenter.BaseMessageIdentifier<UITableView.SelectionDidChangeMessage>](notificationcenter/messageidentifier/selectiondidchange.md)
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
- [static var didBecomeKey: NotificationCenter.BaseMessageIdentifier<UIWindow.DidBecomeKeyMessage>](notificationcenter/messageidentifier/didbecomekey.md)
- [static var didResignKey: NotificationCenter.BaseMessageIdentifier<UIWindow.DidResignKeyMessage>](notificationcenter/messageidentifier/didresignkey.md)
- [static var showDetailTargetDidChange: NotificationCenter.BaseMessageIdentifier<UIViewController.ShowDetailTargetDidChangeMessage>](notificationcenter/messageidentifier/showdetailtargetdidchange.md)
### Identifying UIKit focus messages
- [static var didUpdate: NotificationCenter.BaseMessageIdentifier<UIFocusSystem.DidUpdateMessage>](notificationcenter/messageidentifier/didupdate.md)
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
- [static var conversationHistoryDidUpdateMessage: NotificationCenter.BaseMessageIdentifier<ConversationHistoryManager.ConversationHistoryDidUpdate>](notificationcenter/messageidentifier/conversationhistorydidupdatemessage.md)
- [static var didBecomeCurrent: NotificationCenter.BaseMessageIdentifier<GCController.DidBecomeCurrentMessage>](notificationcenter/messageidentifier/didbecomecurrent-9p0n4.md)
  The identifier of the message that posts after a game controller becomes the most recently used controller.
- [static var didBecomeCurrent: NotificationCenter.BaseMessageIdentifier<GCMouse.DidBecomeCurrentMessage>](notificationcenter/messageidentifier/didbecomecurrent-9zfc.md)
  The identifier of the message that posts after a mouse becomes the most recently used mouse.
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCMouse.DidConnectMessage>](notificationcenter/messageidentifier/didconnect-2pidr.md)
  The identifier of the message that posts after a mouse accessory connects to the device.
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCRacingWheel.DidConnectMessage>](notificationcenter/messageidentifier/didconnect-39qlx.md)
  The identifier of the message that posts after a racing wheel accessory connects to the device.
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCController.DidConnectMessage>](notificationcenter/messageidentifier/didconnect-3d7x9.md)
  The identifier of the message that posts after a game controller accessory connects to the device.
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCKeyboard.DidConnectMessage>](notificationcenter/messageidentifier/didconnect-6zuxs.md)
  The identifier of the message that posts after a keyboard accessory connects to the device.
- [static var didConnect: NotificationCenter.BaseMessageIdentifier<GCStylus.DidConnectMessage>](notificationcenter/messageidentifier/didconnect-wf9.md)
  The identifier of the message that posts after a stylus accessory connects to the device.
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCRacingWheel.DidDisconnectMessage>](notificationcenter/messageidentifier/diddisconnect-127wj.md)
  The identifier of the message that posts after a racing wheel accessory disconnects from the device.
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCStylus.DidDisconnectMessage>](notificationcenter/messageidentifier/diddisconnect-3p6qi.md)
  The identifier of the message that posts after a stylus accessory disconnects from the device.
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCMouse.DidDisconnectMessage>](notificationcenter/messageidentifier/diddisconnect-5s9vw.md)
  The identifier of the message that posts after a mouse accessory disconnects from the device.
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCKeyboard.DidDisconnectMessage>](notificationcenter/messageidentifier/diddisconnect-97jtl.md)
  The identifier of the message that posts after a keyboard accessory disconnects from the device.
- [static var didDisconnect: NotificationCenter.BaseMessageIdentifier<GCController.DidDisconnectMessage>](notificationcenter/messageidentifier/diddisconnect-9ymbl.md)
  The identifier of the message that posts after a game controller accessory disconnects from the device.
- [static var didMoveToWritableLocation: NotificationCenter.BaseMessageIdentifier<UIDocument.DidMoveToWritableLocationMessage>](notificationcenter/messageidentifier/didmovetowritablelocation.md)
- [static var didStopBeingCurrent: NotificationCenter.BaseMessageIdentifier<GCMouse.DidStopBeingCurrentMessage>](notificationcenter/messageidentifier/didstopbeingcurrent-2sc31.md)
  The identifier of the message that posts after a mouse stops being longer the most recently used mouse.
- [static var didStopBeingCurrent: NotificationCenter.BaseMessageIdentifier<GCController.DidStopBeingCurrentMessage>](notificationcenter/messageidentifier/didstopbeingcurrent-9pdq9.md)
  The identifier of the message that posts after a game controller stops being longer the most recently used controller.

## Relationships

### Conforming Types
- [NotificationCenter.BaseMessageIdentifier](notificationcenter/basemessageidentifier.md)

## See Also

- [NotificationCenter.BaseMessageIdentifier](notificationcenter/basemessageidentifier.md)
  A type for use when defining optional Message identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier)*