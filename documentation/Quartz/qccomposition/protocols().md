# protocols()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the list of protocols to which the composition conforms.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func protocols() -> [Any]!
```

```objc
- (NSArray *) protocols;
```

#### Return Value

A list of protocols. See [Standard Protocols](../standard-protocols.md).

## See Also

### Getting Information About a Composition
- [func attributes() -> [AnyHashable : Any]!](./attributes%28%29.md)
  Returns the attributes of the composition.
- [func identifier() -> String!](./identifier%28%29.md)
  Returns the unique and persistent identifier for the composition from the composition repository.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccomposition/protocols())*