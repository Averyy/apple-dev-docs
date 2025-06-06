# mapError(_:)

**Framework**: Swift  
**Kind**: method

Returns a new result, mapping any failure value using the given transformation.

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
consuming func mapError<NewFailure>(_ transform: (Failure) -> NewFailure) -> Result<Success, NewFailure> where NewFailure : Error
```

#### Return Value

A `Result` instance with the result of evaluating `transform` as the new failure value if this instance represents a failure.

#### Discussion

Use this method when you need to transform the value of a `Result` instance when it represents a failure. The following example transforms the error value of a result by wrapping it in a custom `Error` type:

```swift
struct DatedError: Error {
    var error: Error
    var date: Date

    init(_ error: Error) {
        self.error = error
        self.date = Date()
    }
}

let result: Result<Int, Error> = // ...
// result == .failure(<error value>)
let resultWithDatedError = result.mapError { DatedError($0) }
// result == .failure(DatedError(error: <error value>, date: <date>))
```

## Parameters

- `transform`: A closure that takes the failure value of the   instance.

## See Also

- [func map<NewSuccess>((Success) -> NewSuccess) -> Result<NewSuccess, Failure>](result/map(_:).md)
  Returns a new result, mapping any success value using the given transformation.
- [func flatMap<NewSuccess>((Success) -> Result<NewSuccess, Failure>) -> Result<NewSuccess, Failure>](result/flatmap(_:).md)
  Returns a new result, mapping any success value using the given transformation and unwrapping the produced result.
- [func flatMapError<NewFailure>((Failure) -> Result<Success, NewFailure>) -> Result<Success, NewFailure>](result/flatmaperror(_:).md)
  Returns a new result, mapping any failure value using the given transformation and unwrapping the produced result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/maperror(_:))*