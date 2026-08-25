# EvaluationTrait

**Framework**: Evaluations  
**Kind**: struct

A test trait that runs an evaluation and records the result as attachments.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
struct EvaluationTrait
```

## Mentions

- [Evaluating language model responses](evaluating-language-model-responses.md)
- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)

#### Overview

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
- [func provideScope(for: Test, testCase: Test.Case?, performing: () async throws -> Void) async throws](evaluationtrait/providescope(for:testcase:performing:).md)
  Runs the evaluation and makes its result available to the test body through an evaluation context.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [TestScoping](../testing/testscoping.md)
- [TestTrait](../testing/testtrait.md)
- [Trait](../testing/trait.md)

## See Also

- [struct EvaluationContext](evaluationcontext.md)
  A context that provides the evaluation result within a test scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationtrait)*