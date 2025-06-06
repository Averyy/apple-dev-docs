# Defining test functions

**Framework**: Swift Testing

Define a test function to validate that code is working correctly.

#### Overview

Defining a test function for a Swift package or project is straightforward.

##### Import the Testing Library

To import the testing library, add the following to the Swift source file that contains the test:

```swift
import Testing
```

> **Note**: Only import the testing library into a test target. Importing the testing library into an application, library, or binary target isn’t supported or recommended. Test functions aren’t stripped from binaries when building for release, so logic and fixtures of a test may be visible to anyone who inspects a build product that contains a test function.

Only import the testing library into a test target. Importing the testing library into an application, library, or binary target isn’t supported or recommended. Test functions aren’t stripped from binaries when building for release, so logic and fixtures of a test may be visible to anyone who inspects a build product that contains a test function.

##### Declare a Test Function

To declare a test function, write a Swift function declaration that doesn’t take any arguments, then prefix its name with the `@Test` attribute:

```swift
@Test func foodTruckExists() {
  // Test logic goes here.
}
```

This test function can be present at file scope or within a type. A type containing test functions is automatically a  and can be optionally annotated with the `@Suite` attribute. For more information about suites, see [`Organizing test functions with suite types`](organizingtests.md).

Note that, while this function is a valid test function, it doesn’t actually perform any action or test any code. To check for expected values and outcomes in test functions, add [`Expectations and confirmations`](expectations.md) to the test function.

##### Customize a Tests Name

To customize a test function’s name as presented in an IDE or at the command line, supply a string literal as an argument to the `@Test` attribute:

```swift
@Test("Food truck exists") func foodTruckExists() { ... }
```

To further customize the appearance and behavior of a test function, use [`Traits`](traits.md) such as [`tags(_:)`](trait/tags(_:).md).

##### Write Concurrent or Throwing Tests

As with other Swift functions, test functions can be marked `async` and `throws` to annotate them as concurrent or throwing, respectively. If a test is only safe to run in the main actor’s execution context (that is, from the main thread of the process), it can be annotated `@MainActor`:

```swift
@Test @MainActor func foodTruckExists() async throws { ... }
```

##### Limit the Availability of a Test

If a test function can only run on newer versions of an operating system or of the Swift language, use the `@available` attribute when declaring it. Use the `message` argument of the `@available` attribute to specify a message to log if a test is unable to run due to limited availability:

```swift
@available(macOS 11.0, *)
@available(swift, introduced: 8.0, message: "Requires Swift 8.0 features to run")
@Test func foodTruckExists() { ... }
```

## See Also

- [Organizing test functions with suite types](organizingtests.md)
  Organize tests into test suites.
- [Migrating a test from XCTest](migratingfromxctest.md)
  Migrate an existing test method or test class written using XCTest.
- [macro Test(String?, any TestTrait...)](test(_:_:).md)
  Declare a test.
- [struct Test](test.md)
  A type representing a test or suite.
- [macro Suite(String?, any SuiteTrait...)](suite(_:_:).md)
  Declare a test suite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/definingtests)*