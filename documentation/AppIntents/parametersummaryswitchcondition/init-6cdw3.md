# init(_:_:)

**Framework**: App Intents  
**Kind**: init

Creates a `Switch` statement that branches based on union value parameter cases.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init(_ keyPath: KeyPath<Intent, IntentParameter<Value>>, @ParameterSummaryCaseBuilder<Intent, Value> _ builder: () -> CaseCondition)
```

## Parameters

- `keyPath`: Key path to the union value parameter
- `builder`: A result builder that constructs the case conditions

## See Also

- [init(ParameterSummarySwitchCondition<Intent, Value, CaseCondition>.WidgetFamily, () -> CaseCondition)](parametersummaryswitchcondition/init(_:_:)-4vxvs.md)
  Initializes a parameter summary Switch statement over widget family.
- [enum ParameterSummaryCaseBuilder](parametersummarycasebuilder.md)
  A result builder that allows you to declaratively describe the cases of a switch statement in a parameter summary.
- [ParameterSummarySwitchCondition.WidgetFamily](parametersummaryswitchcondition/widgetfamily.md)
  An enum that represents a parameter summary Switch statement over widget family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummaryswitchcondition/init(_:_:)-6cdw3)*