# min(_:_:_:_:)

**Framework**: Swift  
**Kind**: func

Returns the least argument passed.

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
func min<T>(_ x: T, _ y: T, _ z: T, _ rest: T...) -> T where T : Comparable
```

#### Return Value

The least of all the arguments. If there are multiple equal least arguments, the result is the first one.

## Parameters

- `x`: A value to compare.
- `y`: Another value to compare.
- `z`: A third value to compare.
- `rest`: Zero or more additional values.

## See Also

- [func min<T>(T, T) -> T](min(_:_:).md)
  Returns the lesser of two comparable values.
- [func max<T>(T, T) -> T](max(_:_:).md)
  Returns the greater of two comparable values.
- [func max<T>(T, T, T, T...) -> T](max(_:_:_:_:).md)
  Returns the greatest argument passed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/min(_:_:_:_:))*