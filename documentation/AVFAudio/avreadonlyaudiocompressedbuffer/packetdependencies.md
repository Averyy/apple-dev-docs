# packetDependencies

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

Read-only access to packet dependencies.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
var packetDependencies: Span<AudioStreamPacketDependencyDescription>? { get }
```

## Discussion

If the format doesn’t employ packet dependencies, this will be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avreadonlyaudiocompressedbuffer/packetdependencies)*