# uncached(_:)

**Framework**: UIKit  
**Kind**: method

Returns a placeholder menu element that the system replaces with the result of the provider’s completion handler.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func uncached(_ elementProvider: @escaping (@escaping ([UIMenuElement]) -> Void) -> Void) -> Self
```

#### Discussion

When you use this initializer, the system calls each deferred element’s completion closure every time it encounters the element in a menu. The system doesn’t cache the element for reuse.

## Parameters

- `elementProvider`: The closure the system calls to request the deferred menu items.

## See Also

- [convenience init((([UIMenuElement]) -> Void) -> Void)](uideferredmenuelement/init(_:).md)
  A convenience initializer that creates a placeholder menu element that the system replaces with the result of the provider’s completion handler.
- [class func usingFocus(identifier: UIDeferredMenuElement.Identifier, shouldCacheItems: Bool) -> Self](uideferredmenuelement/usingfocus(identifier:shouldcacheitems:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uideferredmenuelement/uncached(_:))*