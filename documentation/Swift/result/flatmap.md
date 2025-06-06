# flatMap(_:)

**Framework**: Swift  
**Kind**: method

Returns a new result, mapping any success value using the given transformation and unwrapping the produced result.

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
func flatMap<NewSuccess>(_ transform: (Success) -> Result<NewSuccess, Failure>) -> Result<NewSuccess, Failure> where NewSuccess : ~Copyable
```

#### Return Value

A `Result` instance, either from the closure or the previous `.failure`.

#### Discussion

Use this method to avoid a nested result when your transformation produces another `Result` type.

In this example, note the difference in the result of using `map` and `flatMap` with a transformation that returns a result type.

```swift
func getNextInteger() -> Result<Int, Error> {
    .success(4)
}
func getNextAfterInteger(_ n: Int) -> Result<Int, Error> {
    .success(n + 1)
}

let result = getNextInteger().map { getNextAfterInteger($0) }
// result == .success(.success(5))

let result = getNextInteger().flatMap { getNextAfterInteger($0) }
// result == .success(5)
```

## Parameters

- `transform`: A closure that takes the success value of the   instance.

## See Also

- [func map<NewSuccess>((Success) -> NewSuccess) -> Result<NewSuccess, Failure>](result/map(_:).md)
  Returns a new result, mapping any success value using the given transformation.
- [func mapError<NewFailure>((Failure) -> NewFailure) -> Result<Success, NewFailure>](result/maperror(_:).md)
  Returns a new result, mapping any failure value using the given transformation.
- [func flatMapError<NewFailure>((Failure) -> Result<Success, NewFailure>) -> Result<Success, NewFailure>](result/flatmaperror(_:).md)
  Returns a new result, mapping any failure value using the given transformation and unwrapping the produced result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/flatmap(_:))*