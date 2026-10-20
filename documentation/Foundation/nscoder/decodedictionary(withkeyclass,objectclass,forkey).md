# decodeDictionary(withKeyClass:objectClass:forKey:)

**Framework**: Foundation  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@nonobjc
func decodeDictionary<DecodedKey, DecodedObject>(withKeyClass keyClass: DecodedKey.Type, objectClass: DecodedObject.Type, forKey key: String) -> [DecodedKey : DecodedObject]? where DecodedKey : NSObject, DecodedKey : NSCopying, DecodedKey : NSSecureCoding, DecodedObject : NSObject, DecodedObject : NSSecureCoding
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodedictionary(withkeyclass:objectclass:forkey:))*