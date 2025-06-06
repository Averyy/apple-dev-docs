# age

**Framework**: Swift  
**Kind**: property

The earliest version of the Unicode Standard in which the scalar was assigned.

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
var age: Unicode.Version? { get }
```

#### Discussion

This value is `nil` for code points that have not yet been assigned.

This property corresponds to the “Age” property in the [`Unicode Standard`](https://developer.apple.comhttp://www.unicode.org/versions/latest/).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/age)*