# setValueTransformer(_:forName:)

**Framework**: Foundation  
**Kind**: method

Registers the provided value transformer with a given identifier.

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
class func setValueTransformer(_ transformer: ValueTransformer?, forName name: NSValueTransformerName)
```

## Parameters

- `transformer`: The transformer to register.
- `name`: The name for  .

## See Also

- [Value Transformer Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ValueTransformers/ValueTransformers.html#//apple_ref/doc/uid/10000175i)
- [init?(forName: NSValueTransformerName)](valuetransformer/init(forname:).md)
  Returns the value transformer identified by a given identifier.
- [class func valueTransformerNames() -> [NSValueTransformerName]](valuetransformer/valuetransformernames.md)
  Returns an array of all the registered value transformers.
- [struct NSValueTransformerName](nsvaluetransformername.md)
  Named value transformers defined by `NSValueTransformer`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/valuetransformer/setvaluetransformer(_:forname:))*