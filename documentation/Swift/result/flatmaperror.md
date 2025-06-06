# flatMapError(_:)

**Framework**: Swift  
**Kind**: method

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

#### Return Value

A `Result` instance, either from the closure or the previous `.success`.

## Parameters

- `transform`: A closure that takes the failure value of the   instance.

## See Also

- [func map<NewSuccess>((Success) -> NewSuccess) -> Result<NewSuccess, Failure>](result/map(_:).md)
  Returns a new result, mapping any success value using the given transformation.
- [func mapError<NewFailure>((Failure) -> NewFailure) -> Result<Success, NewFailure>](result/maperror(_:).md)
  Returns a new result, mapping any failure value using the given transformation.
- [func flatMap<NewSuccess>((Success) -> Result<NewSuccess, Failure>) -> Result<NewSuccess, Failure>](result/flatmap(_:).md)
  Returns a new result, mapping any success value using the given transformation and unwrapping the produced result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/flatmaperror(_:))*