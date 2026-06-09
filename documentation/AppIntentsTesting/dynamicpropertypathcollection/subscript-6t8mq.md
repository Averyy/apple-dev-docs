# subscript(_:)

**Framework**: App Intents Testing  
**Kind**: subscript

Accesses typed properties from the intent value at the given index.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
subscript<T>(position: Int) -> T where T : IntentValueConvertible { get throws }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/dynamicpropertypathcollection/subscript(_:)-6t8mq)*