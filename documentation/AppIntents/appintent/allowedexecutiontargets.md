# allowedExecutionTargets

**Framework**: App Intents  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

The list of targets this intent can be executed against.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static var allowedExecutionTargets: IntentExecutionTargets { get }
```

## Mentions

- [Configuring the runtime behavior of your app intents](../configuring-the-runtime-behavior-of-your-app-intents.md)

#### Discussion

By default, an intent can be executed against any target. Use this property to restrict execution to specific targets such as the main app, an App Intents extension, or a WidgetKit extension.

## Default Implementations

### AppIntent Implementations
- [static var allowedExecutionTargets: IntentExecutionTargets](./allowedexecutiontargets-91kol.md)
  The list of targets this intent can be executed against.

## See Also

### Specifying the intent’s allowed target
- [struct IntentExecutionTargets](../intentexecutiontargets.md)
  A set of options that describes which process performs an intent or entity query.
- [AppIntent.ExecutionTargets](./executiontargets.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/allowedexecutiontargets)*