# IntentParameterSummary.ParameterKeyPathsBuilder

**Framework**: App Intents  
**Kind**: enum

A result builder that declaratively builds the path to a parameter.

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
@resultBuilder
enum ParameterKeyPathsBuilder
```

## Topics

### Building the path
- [static func buildBlock(PartialKeyPath<Intent>...) -> [PartialKeyPath<Intent>]](intentparametersummary/parameterkeypathsbuilder/buildblock(_:).md)
- [static func buildExpression<ValueType>(KeyPath<Intent, IntentParameter<ValueType>>) -> PartialKeyPath<Intent>](intentparametersummary/parameterkeypathsbuilder/buildexpression(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparametersummary/parameterkeypathsbuilder)*