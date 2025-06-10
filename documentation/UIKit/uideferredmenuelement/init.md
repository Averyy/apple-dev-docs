# init(_:)

**Framework**: UIKit  
**Kind**: init

A convenience initializer that creates a placeholder menu element that the system replaces with the result of the provider’s completion handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(_ elementProvider: @escaping (@escaping ([UIMenuElement]) -> Void) -> Void)
```

#### Discussion

The system calls each element’s closure once, when it first encounters the element in a menu. Once provided, the system caches the element and may reuse it across menus.

You can use [`uncached(_:)`](uideferredmenuelement/uncached(_:).md) to initialize a deferred menu element without caching. With caching disabled, the system calls the provider closure each time it displays the element.

## Parameters

- `elementProvider`: The closure the system calls to request the deferred menu items.

## See Also

- [class func uncached((([UIMenuElement]) -> Void) -> Void) -> Self](uideferredmenuelement/uncached(_:).md)
  Returns a placeholder menu element that the system replaces with the result of the provider’s completion handler.
- [class func usingFocus(identifier: UIDeferredMenuElement.Identifier, shouldCacheItems: Bool) -> Self](uideferredmenuelement/usingfocus(identifier:shouldcacheitems:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uideferredmenuelement/init(_:))*