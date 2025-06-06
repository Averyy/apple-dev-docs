# version(forClassName:)

**Framework**: Foundation  
**Kind**: method

This method is present for historical reasons and is not used with keyed archivers.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func version(forClassName className: String) -> Int
```

#### Return Value

The version in effect for the class named `className` or `NSNotFound` if no class named `className` exists.

#### Discussion

The version number does apply not to `NSKeyedArchiver`/`NSKeyedUnarchiver`.  A keyed archiver does not encode class version numbers.

## See Also

- [var systemVersion: UInt32](nscoder/systemversion.md)
  The system version in effect for the archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/version(forclassname:))*