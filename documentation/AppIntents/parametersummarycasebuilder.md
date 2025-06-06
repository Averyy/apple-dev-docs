# ParameterSummaryCaseBuilder

**Framework**: App Intents  
**Kind**: enum

A result builder that allows you to declaratively describe the cases of a switch statement in a parameter summary.

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
enum ParameterSummaryCaseBuilder<Intent, Value> where Intent : AppIntent, Value : _IntentValue
```

## Topics

### Building switch statement cases
- [static func buildBlock<C0, DefaultSummary>(C0, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>) -> ParameterSummaryTupleCaseCondition<Intent, Value, (C0, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>)>](parametersummarycasebuilder/buildblock(_:_:).md)
- [static func buildBlock<C0, C1, DefaultSummary>(C0, C1, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>) -> ParameterSummaryTupleCaseCondition<Intent, Value, (C0, C1, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>)>](parametersummarycasebuilder/buildblock(_:_:_:).md)
- [static func buildBlock<C0, C1, C2, DefaultSummary>(C0, C1, C2, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>) -> ParameterSummaryTupleCaseCondition<Intent, Value, (C0, C1, C2, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>)>](parametersummarycasebuilder/buildblock(_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, DefaultSummary>(C0, C1, C2, C3, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>) -> ParameterSummaryTupleCaseCondition<Intent, Value, (C0, C1, C2, C3, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>)>](parametersummarycasebuilder/buildblock(_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, DefaultSummary>(C0, C1, C2, C3, C4, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>) -> ParameterSummaryTupleCaseCondition<Intent, Value, (C0, C1, C2, C3, C4, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>)>](parametersummarycasebuilder/buildblock(_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, DefaultSummary>(C0, C1, C2, C3, C4, C5, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>) -> ParameterSummaryTupleCaseCondition<Intent, Value, (C0, C1, C2, C3, C4, C5, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>)>](parametersummarycasebuilder/buildblock(_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, DefaultSummary>(C0, C1, C2, C3, C4, C5, C6, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>) -> ParameterSummaryTupleCaseCondition<Intent, Value, (C0, C1, C2, C3, C4, C5, C6, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>)>](parametersummarycasebuilder/buildblock(_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, DefaultSummary>(C0, C1, C2, C3, C4, C5, C6, C7, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>) -> ParameterSummaryTupleCaseCondition<Intent, Value, (C0, C1, C2, C3, C4, C5, C6, C7, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>)>](parametersummarycasebuilder/buildblock(_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, DefaultSummary>(C0, C1, C2, C3, C4, C5, C6, C7, C8, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>) -> ParameterSummaryTupleCaseCondition<Intent, Value, (C0, C1, C2, C3, C4, C5, C6, C7, C8, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>)>](parametersummarycasebuilder/buildblock(_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, DefaultSummary>(C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>) -> ParameterSummaryTupleCaseCondition<Intent, Value, (C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>)>](parametersummarycasebuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, DefaultSummary>(C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>) -> ParameterSummaryTupleCaseCondition<Intent, Value, (C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>)>](parametersummarycasebuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, DefaultSummary>(C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>) -> ParameterSummaryTupleCaseCondition<Intent, Value, (C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>)>](parametersummarycasebuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, DefaultSummary>(C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>) -> ParameterSummaryTupleCaseCondition<Intent, Value, (C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>)>](parametersummarycasebuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, DefaultSummary>(C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>) -> ParameterSummaryTupleCaseCondition<Intent, Value, (C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>)>](parametersummarycasebuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, DefaultSummary>(C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>) -> ParameterSummaryTupleCaseCondition<Intent, Value, (C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, ParameterSummaryDefaultCaseCondition<Intent, Value, DefaultSummary>)>](parametersummarycasebuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [struct ParameterSummaryTupleCaseCondition](parametersummarytuplecasecondition.md)
  A type that represents a collection of case conditions for a specific switch statement.
### Type Methods
- [static func buildExpression<C0>(C0) -> C0](parametersummarycasebuilder/buildexpression(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummarycasebuilder)*