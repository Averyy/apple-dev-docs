# init(keyName:)

**Framework**: Core Spotlight  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithKeyName:(NSString *) keyName;
```

## Return Value

A new custom attribute key.

## Discussion

To create custom attribute key names, use a reverse DNS format that includes your company name and does not include the period character (”.”). For example, a key name of the form `com_mycompany_myapp_mykeyname` works well.

## Parameters

- `keyName`: The name of the custom attribute for use as a key in a [`CSSearchableItemAttributeSet`](../cssearchableitemattributeset.md). The key name must be a string that contains only ASCII characters and no punctuation other than the underscore (that is “_”). The prefix `kMD` is reserved.

## See Also

### Creating a custom attribute
- [init?(keyName: String, searchable: Bool, searchableByDefault: Bool, unique: Bool, multiValued: Bool)](./init%28keyname,searchable,searchablebydefault,unique,multivalued%29.md)
  Returns a new custom attribute key with the specified name and properties.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cscustomattributekey/init(keyname:))*