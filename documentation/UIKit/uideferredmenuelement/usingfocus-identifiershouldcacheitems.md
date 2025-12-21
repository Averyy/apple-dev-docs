# usingFocus(identifier:shouldCacheItems:)

**Framework**: UIKit  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
class func usingFocus(identifier: UIDeferredMenuElement.Identifier, shouldCacheItems: Bool) -> Self
```

#### Discussion

Returns a placeholder menu element that is replaced with elements provided from the responder chain. A loading UI takes the place of the element in the menu until it is fulfilled. The element may be stored and re-used across menus.

## Parameters

- `identifier`: An identifier for this deferred element that responders can check to determine which elements   to provide.
- `shouldCacheItems`: Whether or not the deferred element caches items. Passing in @c YES causes this deferred element to   ask the responder chain for elements only once, when the element is first encountered in a menu.   Passing in @c NO asks the responder chain for elements every time the element is displayed.

## See Also

- [convenience init((([UIMenuElement]) -> Void) -> Void)](uideferredmenuelement/init(_:).md)
  A convenience initializer that creates a placeholder menu element that the system replaces with the result of the provider’s completion handler.
- [class func uncached((([UIMenuElement]) -> Void) -> Void) -> Self](uideferredmenuelement/uncached(_:).md)
  Returns a placeholder menu element that the system replaces with the result of the provider’s completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uideferredmenuelement/usingfocus(identifier:shouldcacheitems:))*