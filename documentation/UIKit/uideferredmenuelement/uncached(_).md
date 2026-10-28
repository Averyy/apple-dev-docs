# uncached(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns a placeholder menu element that the system replaces with the result of the provider’s completion handler.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class func uncached(_ elementProvider: @escaping (@escaping ([UIMenuElement]) -> Void) -> Void) -> Self
```

```objc
+ (instancetype) elementWithUncachedProvider:(void (^)(void (^completion)(NSArray<UIMenuElement *> *elements))) elementProvider;
```

## Discussion

When you use this initializer, the system calls each deferred element’s completion closure every time it encounters the element in a menu. The system doesn’t cache the element for reuse.

## Parameters

- `elementProvider`: The closure the system calls to request the deferred menu items.

## See Also

### Creating a deferred menu element
- [convenience init((([UIMenuElement]) -> Void) -> Void)](./init%28_%29.md)
  A convenience initializer that creates a placeholder menu element that the system replaces with the result of the provider’s completion handler.
- [class func usingFocus(identifier: UIDeferredMenuElement.Identifier, shouldCacheItems: Bool) -> Self](./usingfocus%28identifier,shouldcacheitems%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uideferredmenuelement/uncached(_:))*