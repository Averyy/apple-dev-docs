# id

**Framework**: TipKit  
**Kind**: property  
**Required**: Yes

The tip’s unique identifier.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var id: String { get }
```

#### Discussion

If you don’t provide a value, the system assigns the name of the type that conforms to the `Tip` protocol during initialization.

## See Also

- [var title: Text](tip/title.md)
  A title that names the tip.
- [var message: Text?](tip/message.md)
  A short description of how to use the tip’s feature.
- [var image: Image?](tip/image.md)
  The image associated with the tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tip/id)*