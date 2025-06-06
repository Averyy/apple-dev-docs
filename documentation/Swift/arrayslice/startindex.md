# startIndex

**Framework**: Swift  
**Kind**: property

The position of the first element in a nonempty array.

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
var startIndex: Int { get }
```

#### Discussion

`ArraySlice` instances are not always indexed from zero. Use `startIndex` and `endIndex` as the bounds for any element access, instead of `0` and `count`.

If the array is empty, `startIndex` is equal to `endIndex`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/arrayslice/startindex)*