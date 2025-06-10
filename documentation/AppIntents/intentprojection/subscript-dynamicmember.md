# subscript(dynamicMember:)

**Framework**: App Intents  
**Kind**: subscript

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
final subscript<Value>(dynamicMember keyPath: KeyPath<Intent, Value>) -> Value.UnwrappedType where Value : _IntentValue { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentprojection/subscript(dynamicmember:))*