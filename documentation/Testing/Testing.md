# Swift Testing

**Framework**: Swift Testing  
**Kind**: module

Create and run tests for your Swift packages and Xcode projects.

**Availability**:
- Swift 6.0+
- Xcode 16.0+

#### Overview

![The Swift logo on a blue gradient background that contains function, number, tag, and checkmark diamond symbols.](https://docs-assets.developer.apple.com/published/bb0ec39fe3198b15d431887aac09a527/swift-testing-hero%402x.png)

With Swift Testing you leverage powerful and expressive capabilities of the Swift programming language to develop tests with more confidence and less code. The library integrates seamlessly with Swift Package Manager testing workflow, supports flexible test organization, customizable metadata, and scalable test execution.

- Define test functions almost anywhere with a single attribute.
- Group related tests into hierarchies using Swift’s type system.
- Integrate seamlessly with Swift concurrency.
- Parameterize test functions across wide ranges of inputs.
- Enable tests dynamically depending on runtime conditions.
- Parallelize tests in-process.
- Categorize tests using tags.
- Associate bugs directly with the tests that verify their fixes or reproduce their problems.

###### Related Videos

- [`Meet Swift Testing`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2024/10179)
- [`Go further with Swift Testing`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2024/10195)

## Topics

### Essentials
- [Defining test functions](definingtests.md)
  Define a test function to validate that code is working correctly.
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
### Test parameterization
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
- [struct Case](test/case.md)
  A single test case from a parameterized [`Test`](test.md).
### Behavior validation
- [Expectations and confirmations](expectations.md)
  Check for expected values, outcomes, and asynchronous events in tests.
- [Known issues](known-issues.md)
  Mark issues as known when running tests.
### Test customization
- [Traits](traits.md)
  Annotate test functions and suites, and customize their behavior.
### Value description and reflection
- [Describing and reflecting values](describing-values.md)
  Add custom descriptions and mirrors to values you use in your tests.
- [protocol CustomTestReflectable](customtestreflectable.md)
  A protocol describing types with a custom reflection when presented as part of a test’s output.
- [protocol CustomTestStringConvertible](customteststringconvertible.md)
  A protocol describing types with a custom string representation when presented as part of a test’s output.
### Data collection
- [Attachments](attachments.md)
  Attach values to tests to help diagnose issues and gather feedback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Testing)*