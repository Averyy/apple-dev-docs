# checkParameterRangeContains(value:context:)

**Framework**: App Intents  
**Kind**: method

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
func checkParameterRangeContains<Value>(value: Value, context: IntentParameterContext<Self.Output>) throws where Value : RangeComparableProperty, Value == Self.Output.ValueType, Self.Output : Sendable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/rangecheckingresolver/checkparameterrangecontains(value:context:))*