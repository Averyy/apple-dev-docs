# Result

**Framework**: Swift  
**Kind**: enum

A value that represents either a success or a failure, including an associated value in each case.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
enum Result<Success, Failure> where Failure : Error, Success : ~Copyable
```

## Mentions

- [Preserving the Results of a Throwing Expression](preserving-the-results-of-a-throwing-expression.md)
- [Writing Failable Asynchronous APIs](writing-failable-asynchronous-apis.md)

## Topics

### Representing a Result
- [case success(Success)](result/success(_:).md)
  A success, storing a `Success` value.
- [case failure(Failure)](result/failure(_:).md)
  A failure, storing a `Failure` value.
- [Writing Failable Asynchronous APIs](writing-failable-asynchronous-apis.md)
  Vend results as part of an API when you can’t return errors synchronously.
### Converting a Throwing Expression to a Result
- [Preserving the Results of a Throwing Expression](preserving-the-results-of-a-throwing-expression.md)
  Call the initializer that wraps a throwing expression when you need to serialize or memoize the result.
- [init(catching: () throws(Failure) -> Success)](result/init(catching:).md)
  Creates a new result by evaluating a throwing closure, capturing the returned value as a success, or any thrown error as a failure.
### Converting a Result to a Throwing Expression
- [func get() throws(Failure) -> Success](result/get.md)
  Returns the success value as a throwing expression.
### Transforming a Result
- [func map<NewSuccess>((Success) -> NewSuccess) -> Result<NewSuccess, Failure>](result/map(_:).md)
  Returns a new result, mapping any success value using the given transformation.
- [func mapError<NewFailure>((Failure) -> NewFailure) -> Result<Success, NewFailure>](result/maperror(_:).md)
  Returns a new result, mapping any failure value using the given transformation.
- [func flatMap<NewSuccess>((Success) -> Result<NewSuccess, Failure>) -> Result<NewSuccess, Failure>](result/flatmap(_:).md)
  Returns a new result, mapping any success value using the given transformation and unwrapping the produced result.
- [func flatMapError<NewFailure>((Failure) -> Result<Success, NewFailure>) -> Result<Success, NewFailure>](result/flatmaperror(_:).md)
  Returns a new result, mapping any failure value using the given transformation and unwrapping the produced result.
### Comparing Results
- [static func == (Result<Success, Failure>, Result<Success, Failure>) -> Bool](result/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](result/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Publishing a Result
- [var publisher: Result<Success, Failure>.Publisher](result/publisher-swift.property.md)
  A Combine publisher that publishes this instance’s result to each subscriber exactly once, or fails immediately if the result indicates failure.
- [Result.Publisher](result/publisher-swift.struct.md)
  The type of a Combine publisher that publishes this instance’s result to each subscriber exactly once, or fails immediately if the result indicates failure.
### Default Implementations
- [Equatable Implementations](result/equatable-implementations.md)
- [Hashable Implementations](result/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)

## See Also

- [protocol Error](error.md)
  A type representing an error value that can be thrown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result)*