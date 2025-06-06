# max(_:_:_:_:)

**Framework**: Swift  
**Kind**: func

Returns the greatest argument passed.

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
func max<T>(_ x: T, _ y: T, _ z: T, _ rest: T...) -> T where T : Comparable
```

#### Return Value

The greatest of all the arguments. If there are multiple equal greatest arguments, the result is the last one.

## Parameters

- `x`: A value to compare.
- `y`: Another value to compare.
- `z`: A third value to compare.
- `rest`: Zero or more additional values.

## See Also

- [func min<T>(T, T) -> T](min(_:_:).md)
  Returns the lesser of two comparable values.
- [func min<T>(T, T, T, T...) -> T](min(_:_:_:_:).md)
  Returns the least argument passed.
- [func max<T>(T, T) -> T](max(_:_:).md)
  Returns the greater of two comparable values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/max(_:_:_:_:))*