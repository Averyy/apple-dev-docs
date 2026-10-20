# Confirmation

**Framework**: Swift Testing  
**Kind**: struct  
**Role**: Structure

A type that can be used to confirm that an event occurs zero or more times.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
struct Confirmation
```

## Mentions

- [Migrating a test from XCTest](./migratingfromxctest.md)
- [Testing asynchronous code](./testing-asynchronous-code.md)

## Topics

### Instance Methods
- [func callAsFunction(count: Int)](./confirmation/callasfunction%28count%29.md)
  Confirm this confirmation.
- [func confirm(count: Int)](./confirmation/confirm%28count%29.md)
  Confirm this confirmation.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Confirming that asynchronous events occur
- [Testing asynchronous code](./testing-asynchronous-code.md)
  Validate whether your code causes expected events to happen.
- [func confirmation<R>(Comment?, expectedCount: Int, isolation: isolated (any Actor)?, sourceLocation: SourceLocation, (Confirmation) async throws -> sending R) async rethrows -> R](./confirmation%28_,expectedcount,isolation,sourcelocation,_%29-5mqz2.md)
  Confirm that some event occurs during the invocation of a function.
- [func confirmation<R>(Comment?, expectedCount: some RangeExpression<Int> & Sendable & Sequence<Int>, isolation: isolated (any Actor)?, sourceLocation: SourceLocation, (Confirmation) async throws -> sending R) async rethrows -> R](./confirmation%28_,expectedcount,isolation,sourcelocation,_%29-l3il.md)
  Confirm that some event occurs during the invocation of a function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/confirmation)*