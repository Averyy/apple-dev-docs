# CustomTestArgumentEncodable

**Framework**: Swift Testing  
**Kind**: protocol

A protocol for customizing how arguments passed to parameterized tests are encoded, which is used to match against when running specific arguments.

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
protocol CustomTestArgumentEncodable : Sendable
```

## Mentions

- [Implementing parameterized tests](parameterizedtesting.md)

#### Overview

The testing library checks whether a test argument conforms to this protocol, or any of several other known protocols, when running selected test cases. When a test argument conforms to this protocol, that conformance takes highest priority, and the testing library will then call [`encodeTestArgument(to:)`](customtestargumentencodable/encodetestargument(to:).md) on the argument. A type that conforms to this protocol is not required to conform to either `Encodable` or `Decodable`.

See [`Implementing parameterized tests`](parameterizedtesting.md) for a list of the other supported ways to allow running selected test cases.

## Topics

### Instance Methods
- [func encodeTestArgument(to: some Encoder) throws](customtestargumentencodable/encodetestargument(to:).md)
  Encode this test argument.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)

## See Also

- [Implementing parameterized tests](parameterizedtesting.md)
  Specify different input parameters to generate multiple test cases from a test function.
- [Implementing parameterized tests](parameterizedtesting.md)
  Specify different input parameters to generate multiple test cases from a test function.
- [macro Test<C>(String?, any TestTrait..., arguments: C)](test(_:_:arguments:)-8kn7a.md)
  Declare a test parameterized over a collection of values.
- [macro Test<C1, C2>(String?, any TestTrait..., arguments: C1, C2)](test(_:_:arguments:_:).md)
  Declare a test parameterized over two collections of values.
- [macro Test<C1, C2>(String?, any TestTrait..., arguments: Zip2Sequence<C1, C2>)](test(_:_:arguments:)-3rzok.md)
  Declare a test parameterized over two zipped collections of values.
- [struct Case](test/case.md)
  A single test case from a parameterized [`Test`](test.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/customtestargumentencodable)*