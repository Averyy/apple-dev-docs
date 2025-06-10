# init(_:_:)

**Framework**: App Intents  
**Kind**: init

Initializes a parameter summary Switch statement over widget family.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+
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

## See Also

- [init(KeyPath<Intent, IntentParameter<Value>>, () -> CaseCondition)](parametersummaryswitchcondition/init(_:_:)-6cdw3.md)
- [enum ParameterSummaryCaseBuilder](parametersummarycasebuilder.md)
  A result builder that allows you to declaratively describe the cases of a switch statement in a parameter summary.
- [ParameterSummarySwitchCondition.WidgetFamily](parametersummaryswitchcondition/widgetfamily.md)
  An enum that represents a parameter summary Switch statement over widget family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummaryswitchcondition/init(_:_:)-4vxvs)*