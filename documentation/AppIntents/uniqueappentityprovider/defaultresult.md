# defaultResult()

**Framework**: App Intents  
**Kind**: method

The default value for parameters using this provider when no value is provided by the user.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func defaultResult() async -> Self.DefaultValue?
```

#### Discussion

Either a single value or an array of values may be provided. If an array is provided and the parameter requires a single value, only the first element of the array is used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/uniqueappentityprovider/defaultresult())*