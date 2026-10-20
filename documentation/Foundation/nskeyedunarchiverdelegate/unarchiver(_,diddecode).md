# unarchiver(_:didDecode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Informs the delegate that a given object has been decoded.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, didDecode object: consuming Any?) -> Any?
```

```objc
- (id) unarchiver:(NSKeyedUnarchiver *) unarchiver didDecodeObject:(id) object;
```

#### Return Value

The object to use in place of `object`. The delegate can either return `object` or return a different object to replace the decoded one. In apps using ARC, the delegate should only return `nil` if `object` itself is `nil`. In apps not using ARC, the delegate can return `nil` to indicate that the decoded value is unchanged—that is, `object` will be decoded.

#### Discussion

This method is called after `object` has been sent [`init(coder:)`](../nscoding/init%28coder%29.md) and [`awakeAfter(using:)`](../../ObjectiveC/nsobject-swift.class/awakeafter%28using%29.md).

The delegate may use this method to keep track of the decoded objects.

## Parameters

- `unarchiver`: An unarchiver for which the receiver is the delegate.
- `object`: The object that has been decoded. `object` may be `nil`.

## See Also

### Decoding Objects
- [func unarchiver(NSKeyedUnarchiver, cannotDecodeObjectOfClassName: String, originalClasses: [String]) -> AnyClass?](./unarchiver%28_,cannotdecodeobjectofclassname,originalclasses%29.md)
  Informs the delegate that the class with a given name is not available during decoding.
- [func unarchiver(NSKeyedUnarchiver, willReplace: Any, with: Any)](./unarchiver%28_,willreplace,with%29.md)
  Informs the delegate that one object is being substituted for another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/unarchiver(_:diddecode:))*