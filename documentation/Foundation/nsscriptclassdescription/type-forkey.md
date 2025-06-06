# type(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns the name of the declared type of the attribute or relationship identified by the passed key.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func type(forKey key: String) -> String?
```

#### Return Value

The name of the declared type of the attribute or relationship identified by `key`; for example, “NSString”. Searches in the receiver first, then in any superclass. Returns `nil` if no match is found.

## Parameters

- `key`: The identifying key for an attribute, one-to-one relationship, or one-to-many relationship of the receiver.

## See Also

- [func hasOrderedToManyRelationship(forKey: String) -> Bool](nsscriptclassdescription/hasorderedtomanyrelationship(forkey:).md)
  Returns a Boolean value indicating whether the described class has an ordered to-many relationship identified by the specified key.
- [func hasProperty(forKey: String) -> Bool](nsscriptclassdescription/hasproperty(forkey:).md)
  Returns a Boolean value indicating whether the described class has a property identified by the specified key.
- [func hasReadableProperty(forKey: String) -> Bool](nsscriptclassdescription/hasreadableproperty(forkey:).md)
  Returns a Boolean value indicating whether the described class has a readable property identified by the specified key.
- [func hasWritableProperty(forKey: String) -> Bool](nsscriptclassdescription/haswritableproperty(forkey:).md)
  Returns a Boolean value indicating whether the described class has a writable property identified by the specified key.
- [func key(withAppleEventCode: FourCharCode) -> String?](nsscriptclassdescription/key(withappleeventcode:).md)
  Given an Apple event code that identifies a property or element class, returns the key for the corresponding attribute, one-to-one relationship, or one-to-many relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/type(forkey:))*