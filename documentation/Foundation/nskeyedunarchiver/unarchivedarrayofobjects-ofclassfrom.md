# unarchivedArrayOfObjects(ofClass:from:)

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
static func unarchivedArrayOfObjects<DecodedObject>(ofClass cls: DecodedObject.Type, from data: Data) throws -> [DecodedObject]? where DecodedObject : NSObject, DecodedObject : NSSecureCoding
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchivedarrayofobjects(ofclass:from:))*