# Test.Case

**Framework**: Swift Testing  
**Kind**: struct

A single test case from a parameterized [`Test`](test.md).

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
struct Case
```

#### Overview

A test case represents a test run with a particular combination of inputs. Tests that are  parameterized map to a single instance of [`Test.Case`](test/case.md).

## Topics

### Instance Properties
- [var isParameterized: Bool](test/case/isparameterized.md)
  Whether or not this test case is from a parameterized test.
### Type Properties
- [static var current: Test.Case?](test/case/current.md)
  The test case that is running on the current task, if any.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Implementing parameterized tests](parameterizedtesting.md)
  Specify different input parameters to generate multiple test cases from a test function.
- [macro Test<C>(String?, any TestTrait..., arguments: C)](test(_:_:arguments:)-8kn7a.md)
  Declare a test parameterized over a collection of values.
- [macro Test<C1, C2>(String?, any TestTrait..., arguments: C1, C2)](test(_:_:arguments:_:).md)
  Declare a test parameterized over two collections of values.
- [macro Test<C1, C2>(String?, any TestTrait..., arguments: Zip2Sequence<C1, C2>)](test(_:_:arguments:)-3rzok.md)
  Declare a test parameterized over two zipped collections of values.
- [protocol CustomTestArgumentEncodable](customtestargumentencodable.md)
  A protocol for customizing how arguments passed to parameterized tests are encoded, which is used to match against when running specific arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/test/case)*