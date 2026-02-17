# init(ianaName:)

**Framework**: Swift  
**Kind**: init

Creates an instance from the name of the IANA registry “charset”.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)
- watchOS 26.4+ (Beta)

## Declaration

```swift
init?(ianaName charsetName: String)
```

#### Discussion

> **Note**: The given name is compared to each IANA “charset” name with ASCII case-insensitive collation to determine which encoding is suitable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/encoding/init(iananame:))*