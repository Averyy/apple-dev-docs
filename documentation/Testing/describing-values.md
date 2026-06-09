# Describing and reflecting values

**Framework**: Swift Testing

Add custom descriptions and mirrors to values you use in your tests.

#### Overview

The testing library provides two protocols, [`CustomTestStringConvertible`](customteststringconvertible.md) and [`CustomTestReflectable`](customtestreflectable.md), that you can use to customize the appearance of values in Swift. The testing library uses these protocols to describe parameterized test arguments and, if a call to [`expect(_:_:sourceLocation:)`](expect(_:_:sourcelocation:).md) or [`require(_:_:sourceLocation:)`](require(_:_:sourcelocation:)-5l63q.md) fails, to describe any values you pass to them.

#### Customize the Description of a Value

You use the [`CustomTestStringConvertible`](customteststringconvertible.md) protocol when you want to customize the description of a value *during testing only*. Values whose types conform to this protocol use it to describe themselves when the testing library presents them as part of the output of a test. For example, this protocol affects the display of values you pass as arguments to test functions or that are elements of an expectation failure.

By default, the testing library converts values to strings using [`String(describing:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/string/init(describing:)-67ncf). The resulting string may be inappropriate for some types and their values. If you make the type of the value conform to [`CustomTestStringConvertible`](customteststringconvertible.md), then the testing library will use the value of its [`testDescription`](customteststringconvertible/testdescription.md) property instead.

For example, consider the following type:

```swift
enum Food: CaseIterable {
  case paella, oden, ragu
}
```

If you pass an array of cases from this enumeration to a parameterized test function:

```swift
@Test(arguments: Food.allCases)
func isDelicious(_ food: Food) { ... }
```

Then the testing library needs to present all elements in the array in its output, but the default description of these values may not be adequately descriptive:

```None
◇ Test case passing 1 argument food → .paella to isDelicious(_:) started.
◇ Test case passing 1 argument food → .oden to isDelicious(_:) started.
◇ Test case passing 1 argument food → .ragu to isDelicious(_:) started.
```

When you adopt [`CustomTestStringConvertible`](customteststringconvertible.md), you can include customized descriptions in your test output instead.

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

The testing library then uses [`testDescription`](customteststringconvertible/testdescription.md) to present these values:

```None
◇ Test case passing 1 argument food → paella valenciana to isDelicious(_:) started.
◇ Test case passing 1 argument food → おでん to isDelicious(_:) started.
◇ Test case passing 1 argument food → ragù alla bolognese to isDelicious(_:) started.
```

#### Customize the Reflection of a Value

When a call to [`expect(_:_:sourceLocation:)`](expect(_:_:sourcelocation:).md) or to [`require(_:_:sourceLocation:)`](require(_:_:sourcelocation:)-5l63q.md) fails, the testing library presents the value or values you pass to these macros in its output.

The testing library uses [`Mirror.init(reflecting:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/mirror/init(reflecting:)) to break down these values if they contain properties that may be of interest to you. For instance, if the `isDelicious(_:)` test fails, you might see output such as:

```None
✘ Test isDelicious(_:) recorded an issue with 1 argument food → sandwich
↳ food.isDelicious → false
↳   food → sandwich
↳     sandwich → (toppings: [Food.pickles, Food.candyCorn])
↳       toppings → [Food.pickles, Food.candyCorn]
↳   isDelicious → false
```

This output is expressive, but also contains redundant information. You can refine it further by making `Food` conform to the [`CustomTestReflectable`](customtestreflectable.md) protocol.

```swift
extension Food: CustomTestReflectable {
  var customTestMirror: Mirror {
    switch self {
    case let .sandwich(toppings):
      let ingredientNames = toppings.map { String(describingForTest: $0) }
      return Mirror(
        self,
        children: [(label: "toppings", value: ingredientNames)]
      )
    default:
      Mirror(self, children: [])
    }
  }
}
```

With this conformance, the output of the failed test is instead:

```None
✘ Test isDelicious(_:) recorded an issue with 1 argument food → sandwich
↳ food.isDelicious → false
↳   food → sandwich
↳     toppings → ["pickles", "candy corn"]
↳   isDelicious → false
```

#### Implement Custom Descriptions Using Private Properties

If part or all of your type’s state is `private` or otherwise not visible to your test target, you may not be able to implement [`testDescription`](customteststringconvertible/testdescription.md) or [`customTestMirror`](customtestreflectable/customtestmirror.md) in your test target. You can implement these properties, without adding conformances to either protocol, in your production target, and then add empty protocol conformances in your test target. Make sure to use `internal` or `package` visibility for the properties so that your test target is able to use them.

```swift
// In your production target:

extension Food {
  package var testDescription: String { ... }
  package var customTestMirror: Mirror { ... }
}
  
// In your test target:

import FoodTruck

extension Food: CustomTestStringConvertible, CustomTestReflectable {}
```

> **Note**: If you use `internal` visibility for these properties, you must import your production target into your test target using the `@testable` attribute.

## See Also

- [protocol CustomTestReflectable](customtestreflectable.md)
  A protocol describing types with a custom reflection when presented as part of a test’s output.
- [protocol CustomTestStringConvertible](customteststringconvertible.md)
  A protocol describing types with a custom string representation when presented as part of a test’s output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/describing-values)*