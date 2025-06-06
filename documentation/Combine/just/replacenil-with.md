# replaceNil(with:)

**Framework**: Combine  
**Kind**: method

Replaces nil elements in the stream with the provided element.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func replaceNil<T>(with output: T) -> Publishers.Map<Self, T> where Self.Output == T?
```

#### Return Value

A publisher that replaces `nil` elements from the upstream publisher with the provided element.

#### Discussion

The [`replaceNil(with:)`](publisher/replacenil(with:).md) operator enables replacement of `nil` values in a stream with a substitute value. In the example below, a collection publisher contains a nil value. The [`replaceNil(with:)`](publisher/replacenil(with:).md) operator replaces this with `0.0`.

```swift
let numbers: [Double?] = [1.0, 2.0, nil, 3.0]
numbers.publisher
    .replaceNil(with: 0.0)
    .sink { print("\($0)", terminator: " ") }

// Prints: "Optional(1.0) Optional(2.0) Optional(0.0) Optional(3.0)"
```

## Parameters

- `output`: The element to use when replacing  .

## See Also

- [func map<T>((Output) -> T) -> Just<T>](just/map(_:).md)
- [func tryMap<T>((Output) throws -> T) -> Result<T, any Error>.Publisher](just/trymap(_:).md)
- [func mapError<E>((Just<Output>.Failure) -> E) -> Result<Output, E>.Publisher](just/maperror(_:).md)
- [func scan<T>(T, (T, Output) -> T) -> Result<T, Just<Output>.Failure>.Publisher](just/scan(_:_:).md)
- [func tryScan<T>(T, (T, Output) throws -> T) -> Result<T, any Error>.Publisher](just/tryscan(_:_:).md)
- [func setFailureType<E>(to: E.Type) -> Result<Output, E>.Publisher](just/setfailuretype(to:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/replacenil(with:))*