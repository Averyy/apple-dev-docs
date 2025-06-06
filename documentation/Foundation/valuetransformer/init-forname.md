# init(forName:)

**Framework**: Foundation  
**Kind**: init

Returns the value transformer identified by a given identifier.

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
init?(forName name: NSValueTransformerName)
```

#### Return Value

The value transformer identified by `name` in the shared registry, or `nil` if not found.

#### Discussion

If `valueTransformerForName:` does not find a registered transformer instance for `name`, it will attempt to find a class with the specified name. If a corresponding class is found an instance will be created and initialized using its `init:` method and then automatically registered with `name`.

## Parameters

- `name`: The transformer identifier.

## See Also

- [class func setValueTransformer(ValueTransformer?, forName: NSValueTransformerName)](valuetransformer/setvaluetransformer(_:forname:).md)
  Registers the provided value transformer with a given identifier.
- [class func valueTransformerNames() -> [NSValueTransformerName]](valuetransformer/valuetransformernames.md)
  Returns an array of all the registered value transformers.
- [struct NSValueTransformerName](nsvaluetransformername.md)
  Named value transformers defined by `NSValueTransformer`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/valuetransformer/init(forname:))*