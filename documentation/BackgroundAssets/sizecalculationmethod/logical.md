# SizeCalculationMethod.logical

**Framework**: Background Assets  
**Kind**: case

A calculation method that counts the number of bytes in a file.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- tvOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)

## Declaration

```swift
case logical
```

#### Discussion

The result of a “logical” size calculation for a file may be greater or less than the actual number of bytes that a file takes up on disk due to file-system features like alignment or compression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/sizecalculationmethod/logical)*