# max(_:_:)

**Framework**: Swift  
**Kind**: func  
**Role**: Function

Returns the greater of two comparable values.

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
func max<T>(_ x: T, _ y: T) -> T where T : Comparable
```

#### Return Value

The greater of `x` and `y`. If `x` is equal to `y`, returns `y`.

## Parameters

- `x`: A value to compare.
- `y`: Another value to compare.

## See Also

### Choosing the Smallest and Largest Value
- [func min<T>(T, T) -> T](./min%28_,_%29.md)
  Returns the lesser of two comparable values.
- [func min<T>(T, T, T, T...) -> T](./min%28_,_,_,_%29.md)
  Returns the least argument passed.
- [func max<T>(T, T, T, T...) -> T](./max%28_,_,_,_%29.md)
  Returns the greatest argument passed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/max(_:_:))*