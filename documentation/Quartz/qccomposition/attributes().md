# attributes()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the attributes of the composition.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func attributes() -> [AnyHashable : Any]!
```

```objc
- (NSDictionary *) attributes;
```

#### Return Value

A dictionary of composition attributes. See [Attribute Keys](../attribute-keys.md) for the attributes that can be returned.

## See Also

### Getting Information About a Composition
- [func protocols() -> [Any]!](./protocols%28%29.md)
  Returns the list of protocols to which the composition conforms.
- [func identifier() -> String!](./identifier%28%29.md)
  Returns the unique and persistent identifier for the composition from the composition repository.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccomposition/attributes())*