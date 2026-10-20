# setValueTransformer(_:forName:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (void) setValueTransformer:(NSValueTransformer *) transformer forName:(NSValueTransformerName) name;
```

## Parameters

- `transformer`: The transformer to register.
- `name`: The name for `transformer`.

## See Also

### Related Documentation
- [Value Transformer Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ValueTransformers/ValueTransformers.html#//apple_ref/doc/uid/10000175i)
### Using the Name-Based Registry
- [init?(forName: NSValueTransformerName)](./init%28forname%29.md)
  Returns the value transformer identified by a given identifier.
- [class func valueTransformerNames() -> [NSValueTransformerName]](./valuetransformernames%28%29.md)
  Returns an array of all the registered value transformers.
- [struct NSValueTransformerName](../nsvaluetransformername.md)
  Named value transformers defined by `NSValueTransformer`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/valuetransformer/setvaluetransformer(_:forname:))*