# checkParameterRangeContains(value:context:)

**Framework**: App Intents  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func checkParameterRangeContains<Value>(value: Value, context: IntentParameterContext<Self.Output>) throws where Value : RangeComparableProperty, Value == Self.Output.ValueType, Self.Output : Sendable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/doublefromintresolver/checkparameterrangecontains(value:context:))*