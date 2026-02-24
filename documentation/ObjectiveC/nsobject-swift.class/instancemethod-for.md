# instanceMethod(for:)

**Framework**: Objective-C Runtime  
**Kind**: method

Locates and returns the address of the implementation of the instance method identified by a given selector.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func instanceMethod(for aSelector: Selector!) -> IMP!
```

#### Return Value

The address of the implementation of the `aSelector` instance method.

#### Discussion

An error is generated if instances of the receiver can’t respond to `aSelector` messages.

Use this method to ask the class object for the implementation of instance methods only. To ask the class for the implementation of a class method, send the [`method(for:)`](nsobject-swift.class/method(for:).md) instance method to the class instead.

## Parameters

- `aSelector`: A [`Selector`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) that identifies the method for which to return the implementation address. The selector must be non-`NULL` and valid for the receiver. If in doubt, use the [`responds(to:)`](nsobjectprotocol/responds(to:).md) method to check before passing the selector to [`method(for:)`](nsobject-swift.class/method(for:).md).

## See Also

- [func method(for: Selector!) -> IMP!](nsobject-swift.class/method(for:).md)
  Locates and returns the address of the receiver’s implementation of a method so it can be called as a function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/instancemethod(for:))*