# preferredName

**Framework**: Swift Testing  
**Kind**: property

A filename to use when writing this attachment to a test report or to a file on disk.

**Availability**:
- Swift 6.2+
- Xcode 17.0+

## Declaration

```swift
var preferredName: String { get }
```

#### Discussion

The value of this property is used as a hint to the testing library. The testing library may substitute a different filename as needed. If the value of this property has not been explicitly set, the testing library will attempt to generate its own value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachment/preferredname)*