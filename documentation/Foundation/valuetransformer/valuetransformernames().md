# valueTransformerNames()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an array of all the registered value transformers.

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
class func valueTransformerNames() -> [NSValueTransformerName]
```

```objc
+ (NSArray<NSString *> *) valueTransformerNames;
```

## Return Value

An array of all the registered value transformers.

## See Also

### Using the Name-Based Registry
- [class func setValueTransformer(ValueTransformer?, forName: NSValueTransformerName)](./setvaluetransformer%28_,forname%29.md)
  Registers the provided value transformer with a given identifier.
- [init?(forName: NSValueTransformerName)](./init%28forname%29.md)
  Returns the value transformer identified by a given identifier.
- [struct NSValueTransformerName](../nsvaluetransformername.md)
  Named value transformers defined by `NSValueTransformer`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/valuetransformer/valuetransformernames())*