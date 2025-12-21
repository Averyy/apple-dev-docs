# Test(_:_:arguments:_:)

**Framework**: Swift Testing  
**Kind**: macro

Declare a test parameterized over two collections of values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
@attached
(peer) macro Test<C1, C2>(_ displayName: String? = nil, _ traits: any TestTrait..., arguments collection1: C1, _ collection2: C2) where C1 : Collection, C1 : Sendable, C2 : Collection, C2 : Sendable, C1.Element : Sendable, C2.Element : Sendable
```

#### Overview

You can prefix the expressions you pass to `collection1` or `collection2` with `try` or `await`. The testing library evaluates the expressions lazily only if it determines that the associated test will run. During testing, the testing library calls the associated test function once for each pair of elements in `collection1` and `collection2`.

## Parameters

- `displayName`: The customized display name of this test. If the value of   this argument is  , the display name of the test is derived from the   associated function’s name.
- `traits`: Zero or more traits to apply to this test.
- `collection1`: A collection of values to pass to  .
- `collection2`: A second collection of values to pass to  .

## See Also

- [Defining test functions](definingtests.md)
  Define a test function to validate that code is working correctly.
- [Implementing parameterized tests](parameterizedtesting.md)
  Specify different input parameters to generate multiple test cases from a test function.
- [macro Test<C>(String?, any TestTrait..., arguments: C)](test(_:_:arguments:)-8kn7a.md)
  Declare a test parameterized over a collection of values.
- [macro Test<C1, C2>(String?, any TestTrait..., arguments: Zip2Sequence<C1, C2>)](test(_:_:arguments:)-3rzok.md)
  Declare a test parameterized over two zipped collections of values.
- [protocol CustomTestArgumentEncodable](customtestargumentencodable.md)
  A protocol for customizing how arguments passed to parameterized tests are encoded, which is used to match against when running specific arguments.
- [struct Case](test/case.md)
  A single test case from a parameterized [`Test`](test.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/test(_:_:arguments:_:))*