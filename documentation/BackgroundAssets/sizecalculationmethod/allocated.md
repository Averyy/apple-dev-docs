# SizeCalculationMethod.allocated

**Framework**: Background Assets  
**Kind**: case  
**Role**: Case

A calculation method that counts the number of bytes that the file system allocated for a file.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- tvOS 27.2+
- visionOS 27.2+

## Declaration

```swift
case allocated
```

```c
BASizeCalculationMethodAllocated
```

## Discussion

The result of an “allocated” size calculation for a file roughly corresponds to the number of bytes that would newly be made available if the file were removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/sizecalculationmethod/allocated)*