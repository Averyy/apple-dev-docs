# allowedExecutionTargets

**Framework**: App Intents  
**Kind**: property  
**Role**: Type Property

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

## Discussion

By default, an intent can be executed against any target. Use this property to restrict execution to specific targets such as the main app, an App Intents extension, or a WidgetKit extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/allowedexecutiontargets-91kol)*