# subscript(_:)

**Framework**: Core Audio  
**Kind**: subscript

Access an indexed `AudioBuffer` (`mBuffers[i]`).

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
subscript(index: UnsafeMutableAudioBufferListPointer.Index) -> UnsafeMutableAudioBufferListPointer.Element { get nonmutating set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/unsafemutableaudiobufferlistpointer/subscript(_:))*