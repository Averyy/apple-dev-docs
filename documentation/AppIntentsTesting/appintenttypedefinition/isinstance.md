# isInstance(_:)

**Framework**: App Intents Testing  
**Kind**: method  
**Required**: Yes

Validates that the provided value matches this definition’s type.

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
func isInstance(_ value: Self.Instance) throws
```

#### Discussion

If validation fails, this method throws an error.

## Parameters

- `value`: The value to validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appintenttypedefinition/isinstance(_:))*