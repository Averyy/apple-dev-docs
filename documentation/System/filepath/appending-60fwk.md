# appending(_:)

**Framework**: System  
**Kind**: method

Non-mutating version of `append(_:C)`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func appending<C>(_ components: C) -> FilePath where C : Collection, C.Element == FilePath.Component
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/appending(_:)-60fwk)*