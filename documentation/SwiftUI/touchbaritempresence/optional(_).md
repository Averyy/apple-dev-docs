# TouchBarItemPresence.optional(_:)

**Framework**: SwiftUI  
**Kind**: case  
**Role**: Case

The Touch Bar view isn’t visible by default, but appears in the customization palette.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case optional(String)
```

## Parameters

- `id`: A globally unique identifier for this item.

## See Also

### Getting presence options
- [TouchBarItemPresence.default(_:)](./default%28_%29.md)
  The Touch Bar view is visible by default, but can be removed during customization.
- [TouchBarItemPresence.required(_:)](./required%28_%29.md)
  The Touch Bar view is visible by default and cannot be removed during customization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/touchbaritempresence/optional(_:))*