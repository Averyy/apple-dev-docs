# EvaluationTrait

**Framework**: Evaluations  
**Kind**: struct  
**Role**: Structure

A test trait that runs an evaluation and records the result as attachments.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
struct EvaluationTrait
```

## Mentions

- [Evaluating language model responses](./evaluating-language-model-responses.md)
- [Evaluating tool-calling behavior](./evaluating-tool-calling-behavior.md)

## Overview

```swift
let accuracyMetric = Metric("Accuracy")

@Test(.evaluates(myEvaluation))
func testAccuracy() async throws {
    let result = EvaluationContext.current.result
    #expect(result.aggregateValue(.mean(of: accuracyMetric)) >= 0.8)
}
```

The result is accessible from an evaluation context.

## Topics

### Instance Methods
- [func provideScope(for: Test, testCase: Test.Case?, performing: () async throws -> Void) async throws](./evaluationtrait/providescope%28for,testcase,performing%29.md)
  Runs the evaluation and makes its result available to the test body through an evaluation context.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TestScoping](../Testing/testscoping.md)
- [TestTrait](../Testing/testtrait.md)
- [Trait](../Testing/trait.md)

## See Also

### Swift Testing integration
- [struct EvaluationContext](./evaluationcontext.md)
  A context that provides the evaluation result within a test scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationtrait)*