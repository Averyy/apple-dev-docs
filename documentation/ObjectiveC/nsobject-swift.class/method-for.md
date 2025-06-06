# method(for:)

**Framework**: Objective-C Runtime  
**Kind**: method

Locates and returns the address of the receiver’s implementation of a method so it can be called as a function.

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
func method(for aSelector: Selector!) -> IMP!
```

#### Return Value

The address of the receiver’s implementation of the `aSelector`.

#### Discussion

If the receiver is an instance, `aSelector` should refer to an instance method; if the receiver is a class, it should refer to a class method.

## Parameters

- `aSelector`: A   that identifies the method for which to return the implementation address. The selector must be a valid and non- . If in doubt, use the   method to check before passing the selector to  .

## See Also

- [class func instanceMethod(for: Selector!) -> IMP!](nsobject-swift.class/instancemethod(for:).md)
  Locates and returns the address of the implementation of the instance method identified by a given selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/method(for:))*