# isSearchableByDefault

**Framework**: Core Spotlight  
**Kind**: property

A Boolean value that indicates if the custom attribute should be searchable by default.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var isSearchableByDefault: Bool { get }
```

#### Discussion

The default value of this property is `false`.

## See Also

- [var keyName: String](cscustomattributekey/keyname.md)
  The name of the custom attribute key.
- [var isMultiValued: Bool](cscustomattributekey/ismultivalued.md)
  A Boolean value that indicates if the custom attribute is likely to have multiple values, such as arrays, associated with it.
- [var isSearchable: Bool](cscustomattributekey/issearchable.md)
  A Boolean value that indicates if the custom attribute can be specified as a search term.
- [var isUnique: Bool](cscustomattributekey/isunique.md)
  A Boolean value that indicates if duplicate custom attribute values should be treated as the same value to save storage space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cscustomattributekey/issearchablebydefault)*