# IntentExecutionTargets

**Framework**: App Intents  
**Kind**: struct

A set of options that describes which process performs an intent or entity query.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct IntentExecutionTargets
```

#### Overview

If you reuse intents and entities between your app, widget extension, or App Intents extension by using a Swift package or framework, the system may perform your [`AppIntent`](appintent.md) or [`EntityQuery`](entityquery.md) from the app or App Intents extension. By default, the system performs an intent or entity query using any available target. Use `IntentExecutionTargets` to tell the system which targets can perform your [`AppIntent`](appintent.md) or [`EntityQuery`](entityquery.md). For example, a browser app might represent browser tabs and bookmarks as app entities and offer app intents to add a bookmark or open a browser tab. Adding a bookmark might be an action that can happen while the app isn’t visible, so performing the action in the App Intents extension makes sense. However, opening a new tab makes sense only when the app is visible, requiring the system to perform the intent in the app’s process.

The following example shows an app intent that the system performs in either the main app or the app intents extension:

```swift
struct MyIntent: AppIntent {
    static var allowedExecutionTargets: IntentExecutionTargets { [.main, .appIntentsExtension] }
}
```

## Topics

### Specifying the target
- [static var appIntentsExtension: IntentExecutionTargets](intentexecutiontargets/appintentsextension.md)
  The system performs the intent or query in your app intents extension.
- [static var `default`: IntentExecutionTargets](intentexecutiontargets/default.md)
  The system performs the intent or query in any available target.
- [static var main: IntentExecutionTargets](intentexecutiontargets/main.md)
  The system performs the intent or query in the main app process.
- [static var widgetKitExtension: IntentExecutionTargets](intentexecutiontargets/widgetkitextension.md)
  The system performs the intent or query in a widget extension.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [Hashable](../swift/hashable.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [static var allowedExecutionTargets: IntentExecutionTargets](appintent/allowedexecutiontargets.md)
  The list of targets this intent can be executed against.
- [AppIntent.ExecutionTargets](appintent/executiontargets.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentexecutiontargets)*