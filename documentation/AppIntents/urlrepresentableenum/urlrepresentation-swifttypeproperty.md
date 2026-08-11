# urlRepresentation

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

The URL representation of the app enum.

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

Use this property to store the URL for your custom app enum. When setting the value of this property, you can use a combination of static text and placeholder values to generate the final URL. For example, you might include the raw value of the enum in the URL, as shown in the following example:

```swift
enum Destination: String, AppEnum, URLRepresentableEnum {
   case root
   case locationServices

   static var urlRepresentation = URLRepresentation("https://example.com/root=\(.rawValue)")
}
```

If you need to differentiate URLs by more than the enum’s current value, provide an array of values for your representation instead. The following example shows the same enum from the previous example, but with distinct strings for each case.

```swift
enum Destination: String, AppEnum, URLRepresentableEnum {
   case root
   case locationServices

   static var urlRepresentation = URLRepresentation([
      .root: "https://example.com/link1=\(.root)",
      .locationServices: "https://example.com/link2=\(.locationServices)"
   ])
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/urlrepresentableenum/urlrepresentation-swift.type.property)*