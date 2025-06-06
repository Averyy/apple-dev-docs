# hasProperty(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether the described class has a property identified by the specified key.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func hasProperty(forKey key: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the described class has a property identified by the specified key; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `key`: The identifying key for a property of the receiver.

## See Also

- [func hasOrderedToManyRelationship(forKey: String) -> Bool](nsscriptclassdescription/hasorderedtomanyrelationship(forkey:).md)
  Returns a Boolean value indicating whether the described class has an ordered to-many relationship identified by the specified key.
- [func hasReadableProperty(forKey: String) -> Bool](nsscriptclassdescription/hasreadableproperty(forkey:).md)
  Returns a Boolean value indicating whether the described class has a readable property identified by the specified key.
- [func hasWritableProperty(forKey: String) -> Bool](nsscriptclassdescription/haswritableproperty(forkey:).md)
  Returns a Boolean value indicating whether the described class has a writable property identified by the specified key.
- [func key(withAppleEventCode: FourCharCode) -> String?](nsscriptclassdescription/key(withappleeventcode:).md)
  Given an Apple event code that identifies a property or element class, returns the key for the corresponding attribute, one-to-one relationship, or one-to-many relationship.
- [func type(forKey: String) -> String?](nsscriptclassdescription/type(forkey:).md)
  Returns the name of the declared type of the attribute or relationship identified by the passed key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/hasproperty(forkey:))*