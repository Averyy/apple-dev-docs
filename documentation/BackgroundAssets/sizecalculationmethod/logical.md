# SizeCalculationMethod.logical

**Framework**: Background Assets  
**Kind**: case

A calculation method that counts the number of bytes in a file.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- tvOS 27.2+
- visionOS 27.2+

## Declaration

```swift
case logical
```

#### Discussion

The result of a “logical” size calculation for a file may be greater or less than the actual number of bytes that a file takes up on disk due to file-system features like alignment or compression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/sizecalculationmethod/logical)*