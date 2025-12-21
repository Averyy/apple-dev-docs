# autoContentAccessingProxy

**Framework**: Objective-C Runtime  
**Kind**: property

A proxy for the receiving object

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var autoContentAccessingProxy: Any { get }
```

#### Discussion

This property returns a proxy for the receiving object if the receiver adopts the [`NSDiscardableContent`](https://developer.apple.com/documentation/Foundation/NSDiscardableContent) protocol and still has content that has not been discarded.

The proxy calls [`beginContentAccess()`](https://developer.apple.com/documentation/Foundation/NSDiscardableContent/beginContentAccess()) on the receiver to keep the content available as long as the proxy lives, and calls [`endContentAccess()`](https://developer.apple.com/documentation/Foundation/NSDiscardableContent/endContentAccess()) when the proxy is deallocated.

The wrapper object is otherwise a subclass of [`NSProxy`](https://developer.apple.com/documentation/Foundation/NSProxy) and forwards messages to the original receiver object as an [`NSProxy`](https://developer.apple.com/documentation/Foundation/NSProxy) does.

This method can be used to hide an [`NSDiscardableContent`](https://developer.apple.com/documentation/Foundation/NSDiscardableContent) object’s content volatility by creating an object that responds to the same messages but holds the contents of the original receiver available as long as the created proxy lives. Thus hidden, the [`NSDiscardableContent`](https://developer.apple.com/documentation/Foundation/NSDiscardableContent) object (by way of the proxy) can be given out to unsuspecting recipients of the object who would otherwise not know they might have to call [`beginContentAccess()`](https://developer.apple.com/documentation/Foundation/NSDiscardableContent/beginContentAccess()) and [`endContentAccess()`](https://developer.apple.com/documentation/Foundation/NSDiscardableContent/endContentAccess()) around particular usages (specific to each [`NSDiscardableContent`](https://developer.apple.com/documentation/Foundation/NSDiscardableContent) object) of the [`NSDiscardableContent`](https://developer.apple.com/documentation/Foundation/NSDiscardableContent) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/autocontentaccessingproxy)*