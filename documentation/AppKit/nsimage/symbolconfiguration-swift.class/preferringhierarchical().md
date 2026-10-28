# preferringHierarchical()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates a configuration that specifies that the symbol should prefer its hierarchical variant, if one exists.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class func preferringHierarchical() -> Self
```

```objc
+ (instancetype) configurationPreferringHierarchical;
```

## Discussion

If the symbol doesn’t support hierarchical, the result will be a monochrome (templated) symbol.

## See Also

### Type Methods
- [class func preferringMonochrome() -> Self](./preferringmonochrome%28%29.md)
  Creates a configuration that specifies that the symbol should prefer its monochrome variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/symbolconfiguration-swift.class/preferringhierarchical())*