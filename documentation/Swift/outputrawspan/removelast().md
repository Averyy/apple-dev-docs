# removeLast()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Remove the last byte from this span.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
@discardableResult
mutating func removeLast() -> UInt8
```

#### Return Value

The removed byte.

#### Discussion

Returns the last byte. The `OutputRawSpan` must not be empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/outputrawspan/removelast())*