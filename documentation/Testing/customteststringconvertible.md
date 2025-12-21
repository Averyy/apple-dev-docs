# CustomTestStringConvertible

**Framework**: Swift Testing  
**Kind**: protocol

A protocol describing types with a custom string representation when presented as part of a test’s output.

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
protocol CustomTestStringConvertible
```

#### Overview

Values whose types conform to this protocol use it to describe themselves when they are present as part of the output of a test. For example, this protocol affects the display of values that are passed as arguments to test functions or that are elements of an expectation failure.

By default, the testing library converts values to strings using `String(describing:)`. The resulting string may be inappropriate for some types and their values. If the type of the value is made to conform to [`CustomTestStringConvertible`](customteststringconvertible.md), then the value of its [`testDescription`](customteststringconvertible/testdescription.md) property will be used instead.

For example, consider the following type:

```swift
enum Food: CaseIterable {
  case paella, oden, ragu
}
```

If an array of cases from this enumeration is passed to a parameterized test function:

```swift
@Test(arguments: Food.allCases)
func isDelicious(_ food: Food) { ... }
```

Then the values in the array need to be presented in the test output, but the default description of a value may not be adequately descriptive:

```None
◇ Test case passing 1 argument food → .paella to isDelicious(_:) started.
◇ Test case passing 1 argument food → .oden to isDelicious(_:) started.
◇ Test case passing 1 argument food → .ragu to isDelicious(_:) started.
```

By adopting [`CustomTestStringConvertible`](customteststringconvertible.md), customized descriptions can be included:

```swift
extension Food: CustomTestStringConvertible {
  var testDescription: String {
    switch self {
    case .paella:
      "paella valenciana"
    case .oden:
      "おでん"
    case .ragu:
      "ragù alla bolognese"
    }
  }
}
```

The presentation of these values will then reflect the value of the [`testDescription`](customteststringconvertible/testdescription.md) property:

```None
◇ Test case passing 1 argument food → paella valenciana to isDelicious(_:) started.
◇ Test case passing 1 argument food → おでん to isDelicious(_:) started.
◇ Test case passing 1 argument food → ragù alla bolognese to isDelicious(_:) started.
```

## Topics

### Instance Properties
- [var testDescription: String](customteststringconvertible/testdescription.md)
  A description of this instance to use when presenting it in a test’s output.

## See Also

- [struct Expectation](expectation.md)
  A type describing an expectation that has been evaluated.
- [struct ExpectationFailedError](expectationfailederror.md)
  A type describing an error thrown when an expectation fails during evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/customteststringconvertible)*