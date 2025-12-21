# init(keyName:)

**Framework**: Core Spotlight  
**Kind**: init

Returns a new custom attribute key with the specified name.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
convenience init?(keyName: String)
```

#### Return Value

A new custom attribute key.

#### Discussion

To create custom attribute key names, use a reverse DNS format that includes your company name and does not include the period character (”.”). For example, a key name of the form `com_mycompany_myapp_mykeyname` works well.

## Parameters

- `keyName`: The name of the custom attribute for use as a key in a  . The key name must be a string that contains only ASCII characters and no punctuation other than the underscore (that is “_”). The prefix   is reserved.

## See Also

- [init?(keyName: String, searchable: Bool, searchableByDefault: Bool, unique: Bool, multiValued: Bool)](cscustomattributekey/init(keyname:searchable:searchablebydefault:unique:multivalued:).md)
  Returns a new custom attribute key with the specified name and properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cscustomattributekey/init(keyname:))*