# UnionValue

**Framework**: App Intents  
**Kind**: associatedtype  
**Required**: Yes

The union value type that this cases enum represents.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
associatedtype UnionValue : AppUnionValue where Self == Self.UnionValue.Cases
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appunionvaluecasesproviding/unionvalue)*