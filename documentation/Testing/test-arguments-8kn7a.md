# Test(_:_:arguments:)

**Framework**: Swift Testing  
**Kind**: macro

Declare a test parameterized over a collection of values.

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
(peer) macro Test<C>(_ displayName: String? = nil, _ traits: any TestTrait..., arguments collection: C) where C : Collection, C : Sendable, C.Element : Sendable
```

#### Overview

During testing, the associated test function is called once for each element in `collection`.

## Parameters

- `displayName`: The customized display name of this test. If the value of   this argument is  , the display name of the test is derived from the   associated function’s name.
- `traits`: Zero or more traits to apply to this test.
- `collection`: A collection of values to pass to the associated test   function.

## See Also

- [Defining test functions](definingtests.md)
  Define a test function to validate that code is working correctly.
- [Implementing parameterized tests](parameterizedtesting.md)
  Specify different input parameters to generate multiple test cases from a test function.
- [macro Test<C1, C2>(String?, any TestTrait..., arguments: C1, C2)](test(_:_:arguments:_:).md)
  Declare a test parameterized over two collections of values.
- [macro Test<C1, C2>(String?, any TestTrait..., arguments: Zip2Sequence<C1, C2>)](test(_:_:arguments:)-3rzok.md)
  Declare a test parameterized over two zipped collections of values.
- [protocol CustomTestArgumentEncodable](customtestargumentencodable.md)
  A protocol for customizing how arguments passed to parameterized tests are encoded, which is used to match against when running specific arguments.
- [struct Case](test/case.md)
  A single test case from a parameterized [`Test`](test.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/test(_:_:arguments:)-8kn7a)*