# init(_:id:content:)

**Framework**: Foundation Models  
**Kind**: init

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(_ data: Data, id: KeyPath<Data.Element, ID>, @DynamicInstructionsBuilder content: @escaping (Data.Element) -> Content)
```

## See Also

- [init(Data, content: (Data.Element) -> Content)](dynamicinstructionsforeach/init(_:content:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicinstructionsforeach/init(_:id:content:))*