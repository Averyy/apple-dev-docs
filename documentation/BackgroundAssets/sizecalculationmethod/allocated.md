# SizeCalculationMethod.allocated

**Framework**: Background Assets  
**Kind**: case

A calculation method that counts the number of bytes that the file system allocated for a file.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- tvOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)

## Declaration

```swift
case allocated
```

#### Discussion

The result of an “allocated” size calculation for a file roughly corresponds to the number of bytes that would newly be made available if the file were removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/sizecalculationmethod/allocated)*