# withUnsafeMutablePointer(_:)

**Framework**: Core Audio  
**Kind**: method

Calls a closure with a mutable pointer to the backing `AudioChannelLayout`.

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
mutating func withUnsafeMutablePointer<Result>(_ body: (UnsafeMutablePointer<AudioChannelLayout>) throws -> Result) rethrows -> Result
```

#### Discussion

It is invalid to increase mNumberChannelDescriptions.

## Parameters

- `body`: A closure that is called with a mutable pointer to the   backing  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/managedaudiochannellayout/withunsafemutablepointer(_:))*