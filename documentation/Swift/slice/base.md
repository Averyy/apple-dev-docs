# base

**Framework**: Swift  
**Kind**: property

The underlying collection of the slice.

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
var base: Base { get }
```

#### Discussion

You can use a slice’s `base` property to access its base collection. The following example declares `singleDigits`, a range of single digit integers, and then drops the first element to create a slice of that range, `singleNonZeroDigits`. The `base` property of the slice is equal to `singleDigits`.

```swift
let singleDigits = 0..<10
let singleNonZeroDigits = singleDigits.dropFirst()
// singleNonZeroDigits is a Slice<Range<Int>>

print(singleNonZeroDigits.count)
// Prints "9"
print(singleNonZeroDigits.base.count)
// Prints "10"
print(singleDigits == singleNonZeroDigits.base)
// Prints "true"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/base)*