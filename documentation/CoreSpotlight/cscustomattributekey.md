# CSCustomAttributeKey

**Framework**: Core Spotlight  
**Kind**: class

A key associated with a custom attribute for a searchable item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class CSCustomAttributeKey
```

#### Overview

The `CSCustomAttributeKey` class defines a key that you can associate with a custom attribute for a searchable item. Item attributes provide metadata about the item that can be indexed and displayed to users in search results.

Although the Core Spotlight framework provides several predefined attributes, such as title and description, you can create a `CSCustomAttributeKey` object to specify a custom attribute that makes sense in your domain.

## Topics

### Creating a custom attribute
- [convenience init?(keyName: String)](cscustomattributekey/init(keyname:).md)
  Returns a new custom attribute key with the specified name.
- [init?(keyName: String, searchable: Bool, searchableByDefault: Bool, unique: Bool, multiValued: Bool)](cscustomattributekey/init(keyname:searchable:searchablebydefault:unique:multivalued:).md)
  Returns a new custom attribute key with the specified name and properties.
### Getting the attribute details
- [var keyName: String](cscustomattributekey/keyname.md)
  The name of the custom attribute key.
- [var isMultiValued: Bool](cscustomattributekey/ismultivalued.md)
  A Boolean value that indicates if the custom attribute is likely to have multiple values, such as arrays, associated with it.
- [var isSearchable: Bool](cscustomattributekey/issearchable.md)
  A Boolean value that indicates if the custom attribute can be specified as a search term.
- [var isSearchableByDefault: Bool](cscustomattributekey/issearchablebydefault.md)
  A Boolean value that indicates if the custom attribute should be searchable by default.
- [var isUnique: Bool](cscustomattributekey/isunique.md)
  A Boolean value that indicates if duplicate custom attribute values should be treated as the same value to save storage space.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CSSearchableItem](cssearchableitem.md)
  The details of your app-specific content that someone might search for on their devices.
- [class CSSearchableItemAttributeSet](cssearchableitemattributeset.md)
  The detailed metadata for a searchable item.
- [class CSLocalizedString](cslocalizedstring.md)
  An object that displays localized text in search results related to your app.
- [class CSPerson](csperson.md)
  An object that represents a person in the context of search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cscustomattributekey)*