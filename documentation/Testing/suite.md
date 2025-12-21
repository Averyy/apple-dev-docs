# Suite(_:_:)

**Framework**: Swift Testing  
**Kind**: macro

Declare a test suite.

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
(member) @attached(peer) macro Suite(_ displayName: String? = nil, _ traits: any SuiteTrait...)
```

#### Overview

A test suite is a type that contains one or more test functions. Any escapable type (that is, any type that is not marked `~Escapable`) may be a test suite.

The use of the `@Suite` attribute is optional; types are recognized as test suites even if they do not have the `@Suite` attribute applied to them.

When adding test functions to a type extension, do not use the `@Suite` attribute. Only a type’s primary declaration may have the `@Suite` attribute applied to it.

## Parameters

- `displayName`: The customized display name of this test suite. If the   value of this argument is  , the display name of the test is derived   from the associated type’s name.
- `traits`: Zero or more traits to apply to this test suite.

## See Also

- [Organizing test functions with suite types](organizingtests.md)
  Organize tests into test suites.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/suite(_:_:))*