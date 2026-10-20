# isMultiValued

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the custom attribute is likely to have multiple values, such as arrays, associated with it.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var isMultiValued: Bool { get }
```

```objc
@property (readonly, getter=isMultiValued) BOOL multiValued;
```

#### Discussion

The default value of this property is `false`.

## See Also

### Getting the attribute details
- [var keyName: String](./keyname.md)
  The name of the custom attribute key.
- [var isSearchable: Bool](./issearchable.md)
  A Boolean value that indicates if the custom attribute can be specified as a search term.
- [var isSearchableByDefault: Bool](./issearchablebydefault.md)
  A Boolean value that indicates if the custom attribute should be searchable by default.
- [var isUnique: Bool](./isunique.md)
  A Boolean value that indicates if duplicate custom attribute values should be treated as the same value to save storage space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cscustomattributekey/ismultivalued)*