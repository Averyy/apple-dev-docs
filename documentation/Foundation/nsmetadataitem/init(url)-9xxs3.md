# init(url:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a metadata item with a given URL.

**Availability**:
- macOS 10.9+

## Declaration

```swift
init?(url: URL)
```

```objc
- (instancetype) initWithURL:(NSURL *) url;
```

#### Return Value

A metadata item for the file identified by `url`.

## Parameters

- `url`: The URL for the metadata item.

## See Also

### Related Documentation
- [File Metadata Search Programming Guide](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/Introduction.html#//apple_ref/doc/uid/TP40001841)
- [File Metadata Attributes Reference](https://developer.apple.com/library/archive/documentation/CoreServices/Reference/MetadataAttributesRef/MetadataAttrRef.html#//apple_ref/doc/uid/TP40001689)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataitem/init(url:)-9xxs3)*