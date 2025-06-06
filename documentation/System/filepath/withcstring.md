# withCString(_:)

**Framework**: System  
**Kind**: method

For backwards compatibility only. This function is equivalent to the preferred `withPlatformString`.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func withCString<Result>(_ body: (UnsafePointer<CChar>) throws -> Result) rethrows -> Result
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/withcstring(_:))*