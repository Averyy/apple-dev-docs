# withUnsafePointer(_:)

**Framework**: Core Audio  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func withUnsafePointer<Result>(_ body: (UnsafePointer<AudioChannelLayout>) throws -> Result) rethrows -> Result
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/managedaudiochannellayout/withunsafepointer(_:))*