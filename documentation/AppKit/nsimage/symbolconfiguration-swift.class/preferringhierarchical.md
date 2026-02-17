# preferringHierarchical()

**Framework**: AppKit  
**Kind**: method

Creates a configuration that specifies that the symbol should prefer its hierarchical variant, if one exists.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class func preferringHierarchical() -> Self
```

#### Discussion

If the symbol doesn’t support hierarchical, the result will be a monochrome (templated) symbol.

## See Also

- [class func preferringMonochrome() -> Self](nsimage/symbolconfiguration-swift.class/preferringmonochrome.md)
  Creates a configuration that specifies that the symbol should prefer its monochrome variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/symbolconfiguration-swift.class/preferringhierarchical())*