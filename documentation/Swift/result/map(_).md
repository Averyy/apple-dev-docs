# map(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns a new result, mapping any success value using the given transformation.

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
func map<NewSuccess>(_ transform: (Success) -> NewSuccess) -> Result<NewSuccess, Failure> where NewSuccess : ~Copyable
```

Available when `Failure` conforms to `Error`.

#### Return Value

A `Result` instance with the result of evaluating `transform` as the new success value if this instance represents a success.

#### Discussion

Use this method when you need to transform the value of a `Result` instance when it represents a success. The following example transforms the integer success value of a result into a string:

```swift
func getNextInteger() -> Result<Int, Error> { /* ... */ }

let integerResult = getNextInteger()
// integerResult == .success(5)
let stringResult = integerResult.map { String($0) }
// stringResult == .success("5")
```

## Parameters

- `transform`: A closure that takes the success value of this instance.

## See Also

### Transforming a Result
- [func mapError<NewFailure>((Failure) -> NewFailure) -> Result<Success, NewFailure>](./maperror%28_%29.md)
  Returns a new result, mapping any failure value using the given transformation.
- [func flatMap<NewSuccess>((Success) -> Result<NewSuccess, Failure>) -> Result<NewSuccess, Failure>](./flatmap%28_%29.md)
  Returns a new result, mapping any success value using the given transformation and unwrapping the produced result.
- [func flatMapError<NewFailure>((Failure) -> Result<Success, NewFailure>) -> Result<Success, NewFailure>](./flatmaperror%28_%29.md)
  Returns a new result, mapping any failure value using the given transformation and unwrapping the produced result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/map(_:))*