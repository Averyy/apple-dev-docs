# init(ianaName:)

**Framework**: Swift  
**Kind**: init

Creates an instance from the name of the IANA registry “charset”.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
init?(ianaName charsetName: String)
```

#### Discussion

> **Note**: The given name is compared to each IANA “charset” name with ASCII case-insensitive collation to determine which encoding is suitable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/encoding/init(iananame:))*