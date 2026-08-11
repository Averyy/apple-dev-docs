# urlRepresentation

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

The URL representation of the app intent.

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
static var urlRepresentation: Self.URLRepresentation { get }
```

#### Discussion

Use this property to store the URL for your app intent. When setting the value of this property, you can use a combination of static text and placeholder values to generate the final URL. The following code shows an app intent that opens a specific website page:

```swift
struct OpenAppleDotCom: URLRepresentableIntent {
   static var urlRepresentation: URLRepresentation = "https://www.apple.com/\(\.$page)"

   @Parameter(title: "Page")
   var page: String

   static var title: LocalizedStringResource = "Open Apple website"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/urlrepresentableintent/urlrepresentation-4fzwq)*