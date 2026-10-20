# autoContentAccessingProxy

**Framework**: Objective-C Runtime  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (retain, readonly) id autoContentAccessingProxy;
```

#### Discussion

This property returns a proxy for the receiving object if the receiver adopts the [`NSDiscardableContent`](../../Foundation/nsdiscardablecontent.md) protocol and still has content that has not been discarded.

The proxy calls [`beginContentAccess()`](../../Foundation/nsdiscardablecontent/begincontentaccess%28%29.md) on the receiver to keep the content available as long as the proxy lives, and calls [`endContentAccess()`](../../Foundation/nsdiscardablecontent/endcontentaccess%28%29.md) when the proxy is deallocated.

The wrapper object is otherwise a subclass of [`NSProxy`](../../Foundation/nsproxy.md) and forwards messages to the original receiver object as an [`NSProxy`](../../Foundation/nsproxy.md) does.

This method can be used to hide an [`NSDiscardableContent`](../../Foundation/nsdiscardablecontent.md) object’s content volatility by creating an object that responds to the same messages but holds the contents of the original receiver available as long as the created proxy lives. Thus hidden, the [`NSDiscardableContent`](../../Foundation/nsdiscardablecontent.md) object (by way of the proxy) can be given out to unsuspecting recipients of the object who would otherwise not know they might have to call [`beginContentAccess()`](../../Foundation/nsdiscardablecontent/begincontentaccess%28%29.md) and [`endContentAccess()`](../../Foundation/nsdiscardablecontent/endcontentaccess%28%29.md) around particular usages (specific to each [`NSDiscardableContent`](../../Foundation/nsdiscardablecontent.md) object) of the [`NSDiscardableContent`](../../Foundation/nsdiscardablecontent.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/autocontentaccessingproxy)*