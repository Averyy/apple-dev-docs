# allowedExecutionTargets

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

The list of targets this intent can be executed against.

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
static var allowedExecutionTargets: IntentExecutionTargets { get }
```

#### Discussion

By default, an intent can be executed against any target. Use this property to restrict execution to specific targets such as the main app, an App Intents extension, or a WidgetKit extension.

## See Also

- [struct IntentExecutionTargets](intentexecutiontargets.md)
  A set of options that describes which process performs an intent or entity query.
- [AppIntent.ExecutionTargets](appintent/executiontargets.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/allowedexecutiontargets)*