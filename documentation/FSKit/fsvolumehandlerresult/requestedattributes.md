# requestedAttributes

**Framework**: FSKit  
**Kind**: property

A set of attributes to populate.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class var requestedAttributes: FSItem.GetAttributesRequest { get }
```

#### Discussion

Your module populates these attributes in [`FSItem.Attributes`](fsitem/attributes.md) instances.

Different operations may require different attribute sets. Access this property through the relevant result subclass, such as ``FSLookupItemResult.requestedAttributes`.

> ❗ **Important**:  Be sure to populate all requested attributes. FSKit caches all populated attributes and may use them in subsequent operations, even if not explicitly requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolumehandlerresult/requestedattributes)*