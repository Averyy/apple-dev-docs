# isInstance(_:)

**Framework**: App Intents Testing  
**Kind**: method  
**Required**: Yes

Validates that the provided value matches this definition’s type.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func isInstance(_ value: Self.Instance) throws
```

#### Discussion

If validation fails, this method throws an error.

## Parameters

- `value`: The value to validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appintenttypedefinition/isinstance(_:))*