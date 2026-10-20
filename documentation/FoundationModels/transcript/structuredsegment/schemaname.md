# schemaName

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property

A name that can be used to understand which type the content represents.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS*

```swift
@backDeployed(before: iOS 27.0, macOS 27.0, visionOS 27.0)
var schemaName: String { get set }
```

*watchOS*

```swift
var schemaName: String
```

## See Also

### Inspecting a structured segment
- [var content: GeneratedContent](./content.md)
  The content of the segment.
- [var source: String](./source.md)
  A source that can be used to understand which type the content represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/structuredsegment/schemaname)*