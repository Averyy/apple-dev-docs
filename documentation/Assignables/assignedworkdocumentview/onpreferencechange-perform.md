# onPreferenceChange(_:perform:)

**Framework**: Assignables  
**Kind**: method

Adds an action to perform when the specified preference key’s value changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func onPreferenceChange<K>(_ key: K.Type = K.self, perform action: @escaping (K.Value) -> Void) -> some View where K : PreferenceKey, K.Value : Equatable
```

#### Return Value

A view that triggers `action` when the value for `key` changes.

## Parameters

- `key`: The key to monitor for value changes.
- `action`: The action to perform when the value for   changes. The    closure passes the new value as its parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/onpreferencechange(_:perform:))*