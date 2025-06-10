# buildExpression(_:)

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
static func buildExpression<ValueType>(_ expression: KeyPath<Intent, IntentParameter<ValueType>>) -> PartialKeyPath<Intent> where ValueType : _IntentValue, ValueType : Sendable
```

## See Also

- [static func buildBlock(PartialKeyPath<Intent>...) -> [PartialKeyPath<Intent>]](intentparametersummary/parameterkeypathsbuilder/buildblock(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparametersummary/parameterkeypathsbuilder/buildexpression(_:))*