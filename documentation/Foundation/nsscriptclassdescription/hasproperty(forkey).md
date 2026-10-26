# hasProperty(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the described class has a property identified by the specified key.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func hasProperty(forKey key: String) -> Bool
```

```objc
- (BOOL) hasPropertyForKey:(NSString *) key;
```

#### Return Value

[`true`](../../Swift/true.md) if the described class has a property identified by the specified key; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `key`: The identifying key for a property of the receiver.

## See Also

### Getting attribute and relationship information
- [func hasOrderedToManyRelationship(forKey: String) -> Bool](./hasorderedtomanyrelationship%28forkey%29.md)
  Returns a Boolean value indicating whether the described class has an ordered to-many relationship identified by the specified key.
- [func hasReadableProperty(forKey: String) -> Bool](./hasreadableproperty%28forkey%29.md)
  Returns a Boolean value indicating whether the described class has a readable property identified by the specified key.
- [func hasWritableProperty(forKey: String) -> Bool](./haswritableproperty%28forkey%29.md)
  Returns a Boolean value indicating whether the described class has a writable property identified by the specified key.
- [func key(withAppleEventCode: FourCharCode) -> String?](./key%28withappleeventcode%29.md)
  Given an Apple event code that identifies a property or element class, returns the key for the corresponding attribute, one-to-one relationship, or one-to-many relationship.
- [func type(forKey: String) -> String?](./type%28forkey%29.md)
  Returns the name of the declared type of the attribute or relationship identified by the passed key.
- [- isReadOnlyKey:](./isreadonlykey_.md)
  Returns a Boolean value indicating whether a specified property in the receiver is read-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/hasproperty(forkey:))*