# init(_:_:)

**Framework**: App Intents  
**Kind**: init

Initializes a parameter summary Switch statement over widget family.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(_ widgetFamily: ParameterSummarySwitchCondition<Intent, Value, CaseCondition>.WidgetFamily, @ParameterSummaryCaseBuilder<Intent, IntentWidgetFamily> _ builder: () -> CaseCondition) where Value == IntentWidgetFamily
```

#### Discussion

For example:

```swift
static var parameterSummary: some ParameterSummary {
    Switch(.widgetFamily) {
        Case(.systemLarge) {
            Summary("Parameter summary for large widgets")
        }
        Case([.systemSmall, .systemMedium]) {
            Summary("Parameter summary for small and medium widgets")
        }
        DefaultCase {
            Summary("Default parameter summary")
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummaryswitchcondition/init(_:_:)-4vxvs)*