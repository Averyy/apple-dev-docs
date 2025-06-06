# init(_:identifier:_:_:otherwise:)

**Framework**: App Intents  
**Kind**: init

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init<IntentType, Parameter>(_ keyPath: KeyPath<IntentType, Parameter>, identifier comparisonOperator: ComparableComparisonOperator, _ value: Parameter.Value.ValueType.ID, @ParameterSummaryBuilder<Intent> _ when: () -> WhenCondition, @ParameterSummaryBuilder<Intent> otherwise: () -> Otherwise) where IntentType : AppIntent, Parameter : AnyIntentValue, Parameter.Value.ValueType : AppEntity, Parameter.Value.ValueType.ID == Int
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummarywhencondition/init(_:identifier:_:_:otherwise:)-4f45j)*