# urlRepresentationParameter

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

The string representation of the type’s content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var urlRepresentationParameter: String? { get async }
```

#### Discussion

Use this property to provide a string that describes your custom type. When specifying the string, use Swift interpolated values to incorporate data from any properties of your type, and specify only characters that URLs support. The following example shows a custom type that uses data from multiple properties to generate a string for URLs.

```swift
struct MyCustomType: CustomURLRepresentationParameterConvertible {
   var name: String
   var id: UUID

   var urlRepresentationParameter: String? { "\(name)/\(id)" }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/customurlrepresentationparameterconvertible/urlrepresentationparameter)*