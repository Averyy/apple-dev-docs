# allowsReverseTransformation()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (BOOL) allowsReverseTransformation;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver supports reverse value transformations, otherwise [`false`](../../Swift/false.md).

The default is [`true`](../../Swift/true.md).

## Discussion

Subclasses should override this method to return [`false`](../../Swift/false.md) if they do not support reverse value transformations.

## See Also

### Getting Information About a Transformer
- [class func transformedValueClass() -> AnyClass](./transformedvalueclass%28%29.md)
  Returns the class of the value returned by the receiver for a forward transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/valuetransformer/allowsreversetransformation())*