# attributedTitle

**Framework**: Accessibility  
**Kind**: property  
**Required**: Yes

An attributed version of the axis title.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@NSCopying
var attributedTitle: NSAttributedString { get set }
```

#### Discussion

If you set the value of this property, the system uses this value instead of [`title`](axdataaxisdescriptor/title.md).

## See Also

- [var title: String](axdataaxisdescriptor/title.md)
  The title of the axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axdataaxisdescriptor/attributedtitle)*