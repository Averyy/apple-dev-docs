# bufferOffset

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The byte offset into [`buffer`](./buffer.md) where this plane’s data begins, or `0` if no buffer was provided at initialization.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var bufferOffset: Int { get }
```

```objc
@property (readonly) NSUInteger bufferOffset;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorauxiliaryplane/bufferoffset)*