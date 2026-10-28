# identifier()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the unique and persistent identifier for the composition from the composition repository.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func identifier() -> String!
```

```objc
- (NSString *) identifier;
```

## Return Value

The unique identifier for the composition if it comes from the composition repository; `nil` otherwise.

## See Also

### Getting Information About a Composition
- [func attributes() -> [AnyHashable : Any]!](./attributes%28%29.md)
  Returns the attributes of the composition.
- [func protocols() -> [Any]!](./protocols%28%29.md)
  Returns the list of protocols to which the composition conforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccomposition/identifier())*