# getValue(forKey:)

**Framework**: SwiftData  
**Kind**: method  
**Required**: Yes

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
func getValue<Value>(forKey: KeyPath<Self.Model, Value>) -> Value where Value : Decodable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/backingdata/getvalue(forkey:)-5fis7)*