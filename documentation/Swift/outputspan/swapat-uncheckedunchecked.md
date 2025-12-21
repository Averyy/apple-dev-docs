# swapAt(unchecked:unchecked:)

**Framework**: Swift  
**Kind**: method

Exchange the elements at the two given offsets

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
mutating func swapAt(unchecked i: OutputSpan<Element>.Index, unchecked j: OutputSpan<Element>.Index)
```

#### Discussion

This subscript does not validate `i` or `j`; this is an unsafe operation.

## Parameters

- `i`: A valid index into this span.
- `j`: A valid index into this span.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/outputspan/swapat(unchecked:unchecked:))*