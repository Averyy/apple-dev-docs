# defaultResult()

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

The default value for parameters using this provider when no value is provided by the user.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func defaultResult() async -> Self.DefaultValue?
```

## Discussion

Either a single value or an array of values may be provided. If an array is provided and the parameter requires a single value, only the first element of the array is used.

## Default Implementations

### DynamicOptionsProvider Implementations
- [func defaultResult() async -> Self.DefaultValue?](./defaultresult%28%29-57ptr.md)
  The default value for parameters using this provider when no value is provided by the user.

## See Also

### Returning the parameter options
- [func results() async throws -> Self.Result](./results%28%29.md)
- [associatedtype Result : ResultsCollection](./result.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/dynamicoptionsprovider/defaultresult())*