# load(_:isolation:)

**Framework**: AVFoundation  
**Kind**: method

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: macOS 16, iOS 19, tvOS 19, watchOS 12, visionOS 3)
func load<T>(_ property: AVAsyncProperty<Self, T>, isolation: isolated (any Actor)? = #isolation) async throws -> T
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/load(_:isolation:))*