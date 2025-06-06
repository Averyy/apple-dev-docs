# decodeArrayOfObjects(ofClass:forKey:)

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
func decodeArrayOfObjects<DecodedObject>(ofClass cls: DecodedObject.Type, forKey key: String) -> [DecodedObject]? where DecodedObject : NSObject, DecodedObject : NSSecureCoding
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodearrayofobjects(ofclass:forkey:))*