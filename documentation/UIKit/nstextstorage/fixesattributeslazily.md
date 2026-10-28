# fixesAttributesLazily

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the text storage object fixes attributes lazily.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var fixesAttributesLazily: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL fixesAttributesLazily;
```

## Discussion

When subclassing, the default value of this property is [`false`](../../Swift/false.md), meaning that your subclass fixes attributes immediately when they change. The system’s concrete subclass overrides this property and sets it to [`true`](../../Swift/true.md).

## See Also

### Fixing the string attributes
- [func invalidateAttributes(in: NSRange)](./invalidateattributes%28in%29.md)
  Invalidates attributes in the specified range.
- [func ensureAttributesAreFixed(in: NSRange)](./ensureattributesarefixed%28in%29.md)
  Ensures that attribute fixing occurs in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstorage/fixesattributeslazily)*