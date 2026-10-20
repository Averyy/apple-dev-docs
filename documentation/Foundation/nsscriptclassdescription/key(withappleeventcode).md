# key(withAppleEventCode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Given an Apple event code that identifies a property or element class, returns the key for the corresponding attribute, one-to-one relationship, or one-to-many relationship.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func key(withAppleEventCode appleEventCode: FourCharCode) -> String?
```

```objc
- (NSString *) keyWithAppleEventCode:(FourCharCode) appleEventCode;
```

#### Return Value

The key that corresponds to the property or element class identified by `appleEventCode` in the receiver or, if none exists, in a class description in the receiver’s superclasses. The four-character Apple event code associated with the attribute or relationship identified by `key` Returns `0` if no such attribute or relationship is found. Returns `nil` if it cannot find any such attribute or relationship.

## Parameters

- `appleEventCode`: An Apple event code that identifies a property or element class.

## See Also

### Getting attribute and relationship information
- [func hasOrderedToManyRelationship(forKey: String) -> Bool](./hasorderedtomanyrelationship%28forkey%29.md)
  Returns a Boolean value indicating whether the described class has an ordered to-many relationship identified by the specified key.
- [func hasProperty(forKey: String) -> Bool](./hasproperty%28forkey%29.md)
  Returns a Boolean value indicating whether the described class has a property identified by the specified key.
- [func hasReadableProperty(forKey: String) -> Bool](./hasreadableproperty%28forkey%29.md)
  Returns a Boolean value indicating whether the described class has a readable property identified by the specified key.
- [func hasWritableProperty(forKey: String) -> Bool](./haswritableproperty%28forkey%29.md)
  Returns a Boolean value indicating whether the described class has a writable property identified by the specified key.
- [func type(forKey: String) -> String?](./type%28forkey%29.md)
  Returns the name of the declared type of the attribute or relationship identified by the passed key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/key(withappleeventcode:))*