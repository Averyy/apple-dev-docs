# CMBufferCompareHandler

**Framework**: Core Media  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias CMBufferCompareHandler = (CMBuffer, CMBuffer) -> CFComparisonResult
```

```c
typedef enum CFComparisonResult (^)(const void *, const void *) CMBufferCompareHandler;
```

## See Also

### Type Aliases
- [typealias CMBufferGetBooleanHandler](./cmbuffergetbooleanhandler.md)
- [typealias CMBufferGetSizeHandler](./cmbuffergetsizehandler.md)
- [typealias CMBufferGetTimeHandler](./cmbuffergettimehandler.md)
- [typealias CMTaggedBufferGroupFormatDescription](./cmtaggedbuffergroupformatdescription.md)
  A type for tagged buffer format descriptions.
- [typealias CMTaggedBufferGroupFormatType](./cmtaggedbuffergroupformattype.md)
  A type for tagged buffer format information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbuffercomparehandler)*