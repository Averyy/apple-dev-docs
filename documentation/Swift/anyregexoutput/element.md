# AnyRegexOutput.Element

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

An individual match output value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct Element
```

## Topics

### Instance Properties
- [var name: String?](./element/name.md)
  The name of this capture, if the capture is named.
- [var range: Range<String.Index>?](./element/range.md)
  The range over which a value was captured, if there was a capture.
- [var substring: Substring?](./element/substring.md)
  The slice of the input which was captured, if there was a capture.
- [var type: any Any.Type](./element/type.md)
  The type of this capture.
- [var value: Any?](./element/value.md)
  The captured value, if there was a capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyregexoutput/element)*