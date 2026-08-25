# provideScope(for:testCase:performing:)

**Framework**: Evaluations  
**Kind**: method

Runs the evaluation and makes its result available to the test body through an evaluation context.

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
nonisolated
(nonsending) func provideScope(for test: Test, testCase: Test.Case?, performing function: @Sendable () async throws -> Void) async throws
```

#### Discussion

The Swift Testing framework calls this method automatically when you attach the trait to a test. The evaluation runs first, the framework stores its result in [`EvaluationContext`](evaluationcontext.md), and then the test body executes inside that context.

## Parameters

- `test`: The test to which this trait is attached.
- `testCase`: The specific test case being run, or `nil` when running the whole test.
- `function`: The test body closure to invoke after the evaluation completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationtrait/providescope(for:testcase:performing:))*