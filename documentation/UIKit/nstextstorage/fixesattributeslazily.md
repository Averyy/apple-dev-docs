# fixesAttributesLazily

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the text storage object fixes attributes lazily.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var fixesAttributesLazily: Bool { get }
```

#### Discussion

When subclassing, the default value of this property is [`false`](https://developer.apple.com/documentation/swift/false), meaning that your subclass fixes attributes immediately when they change. The system’s concrete subclass overrides this property and sets it to [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func invalidateAttributes(in: NSRange)](nstextstorage/invalidateattributes(in:).md)
  Invalidates attributes in the specified range.
- [func ensureAttributesAreFixed(in: NSRange)](nstextstorage/ensureattributesarefixed(in:).md)
  Ensures that attribute fixing occurs in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstorage/fixesattributeslazily)*