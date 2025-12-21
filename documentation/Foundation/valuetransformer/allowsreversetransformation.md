# allowsReverseTransformation()

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether the receiver can reverse a transformation.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func allowsReverseTransformation() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver supports reverse value transformations, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

The default is [`true`](https://developer.apple.com/documentation/Swift/true).

#### Discussion

Subclasses should override this method to return [`false`](https://developer.apple.com/documentation/Swift/false) if they do not support reverse value transformations.

## See Also

- [class func transformedValueClass() -> AnyClass](valuetransformer/transformedvalueclass.md)
  Returns the class of the value returned by the receiver for a forward transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/valuetransformer/allowsreversetransformation())*