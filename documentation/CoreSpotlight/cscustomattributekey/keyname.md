# keyName

**Framework**: Core Spotlight  
**Kind**: property

The name of the custom attribute key.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var keyName: String { get }
```

#### Discussion

The key name is a string that contains only ASCII characters and no punctuation other than the underscore (that is “_”). The prefix `kMD` is reserved. To create a custom attribute key name, it’s recommended that you use a reverse DNS format that includes your company name and does not include the period character (”.”). For example, a key name of the form `com_mycompany_myapp_mykeyname` works well.

## See Also

- [var isMultiValued: Bool](cscustomattributekey/ismultivalued.md)
  A Boolean value that indicates if the custom attribute is likely to have multiple values, such as arrays, associated with it.
- [var isSearchable: Bool](cscustomattributekey/issearchable.md)
  A Boolean value that indicates if the custom attribute can be specified as a search term.
- [var isSearchableByDefault: Bool](cscustomattributekey/issearchablebydefault.md)
  A Boolean value that indicates if the custom attribute should be searchable by default.
- [var isUnique: Bool](cscustomattributekey/isunique.md)
  A Boolean value that indicates if duplicate custom attribute values should be treated as the same value to save storage space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cscustomattributekey/keyname)*