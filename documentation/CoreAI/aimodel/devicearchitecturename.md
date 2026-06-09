# deviceArchitectureName

**Framework**: Core AI  
**Kind**: property

The Core AI architecture name of the current device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var deviceArchitectureName: String { get }
```

## Mentions

- [Compiling Core AI models ahead of time](compiling-core-ai-models-ahead-of-time.md)

#### Discussion

When compiling model assets ahead of time with `xcrun coreai-build compile`, the toolchain produces artifacts for specific device architectures. Use this property to discover which compiled asset matches the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodel/devicearchitecturename)*