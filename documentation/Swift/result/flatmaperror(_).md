# flatMapError(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns a new result, mapping any failure value using the given transformation and unwrapping the produced result.

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
consuming func flatMapError<NewFailure>(_ transform: (Failure) -> Result<Success, NewFailure>) -> Result<Success, NewFailure> where NewFailure : Error
```

Available when `Failure` conforms to `Error`.

## Return Value

A `Result` instance, either from the closure or the previous `.success`.

## Parameters

- `transform`: A closure that takes the failure value of the instance.

## See Also

### Transforming a Result
- [func map<NewSuccess>((Success) -> NewSuccess) -> Result<NewSuccess, Failure>](./map%28_%29.md)
  Returns a new result, mapping any success value using the given transformation.
- [func mapError<NewFailure>((Failure) -> NewFailure) -> Result<Success, NewFailure>](./maperror%28_%29.md)
  Returns a new result, mapping any failure value using the given transformation.
- [func flatMap<NewSuccess>((Success) -> Result<NewSuccess, Failure>) -> Result<NewSuccess, Failure>](./flatmap%28_%29.md)
  Returns a new result, mapping any success value using the given transformation and unwrapping the produced result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/flatmaperror(_:))*