# image

**Framework**: TipKit  
**Kind**: property  
**Required**: Yes

The image associated with the tip.

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
var image: Image? { get }
```

#### Discussion

Use this property to display an icon to the left of the `title` and `message` of your tip. This property is `Optional` and defaults to a value of `nil`.

## See Also

- [var title: Text](tip/title.md)
  A title that names the tip.
- [var message: Text?](tip/message.md)
  A short description of how to use the tip’s feature.
- [var id: String](tip/id.md)
  The tip’s unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tip/image)*