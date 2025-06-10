# Test

**Framework**: Swift Testing  
**Kind**: struct

A type representing a test or suite.

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
struct Test
```

#### Overview

An instance of this type may represent:

- A type containing zero or more tests (i.e. a );
- An individual test function (possibly contained within a type); or
- A test function parameterized over one or more sequences of inputs.

Two instances of this type are considered to be equal if the values of their [`id`](test/id-swift.property.md) properties are equal.

## Topics

### Structures
- [struct Case](test/case.md)
  A single test case from a parameterized [`Test`](test.md).
### Instance Properties
- [var associatedBugs: [Bug]](test/associatedbugs.md)
  The set of bugs associated with this test.
- [var comments: [Comment]](test/comments.md)
  The complete set of comments about this test from all of its traits.
- [var displayName: String?](test/displayname.md)
  The customized display name of this instance, if specified.
- [var isParameterized: Bool](test/isparameterized.md)
  Whether or not this test is parameterized.
- [var isSuite: Bool](test/issuite.md)
  Whether or not this instance is a test suite containing other tests.
- [var name: String](test/name.md)
  The name of this instance.
- [var sourceLocation: SourceLocation](test/sourcelocation.md)
  The source location of this test.
- [var tags: Set<Tag>](test/tags.md)
  The complete, unique set of tags associated with this test.
- [var timeLimit: Duration?](test/timelimit.md)
  The maximum amount of time this test’s cases may run for.
- [var traits: [any Trait]](test/traits.md)
  The set of traits added to this instance when it was initialized.
### Type Properties
- [static var current: Test?](test/current.md)
  The test that is running on the current task, if any.
### Default Implementations
- [Equatable Implementations](test/equatable-implementations.md)
- [Hashable Implementations](test/hashable-implementations.md)
- [Identifiable Implementations](test/identifiable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Defining test functions](definingtests.md)
  Define a test function to validate that code is working correctly.
- [Organizing test functions with suite types](organizingtests.md)
  Organize tests into test suites.
- [Migrating a test from XCTest](migratingfromxctest.md)
  Migrate an existing test method or test class written using XCTest.
- [macro Test(String?, any TestTrait...)](test(_:_:).md)
  Declare a test.
- [macro Suite(String?, any SuiteTrait...)](suite(_:_:).md)
  Declare a test suite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/test)*