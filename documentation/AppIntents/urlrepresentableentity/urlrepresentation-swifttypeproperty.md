# urlRepresentation

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

The URL representation of the app entity.

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

Use this property to store the URL for your app entity. When setting the value of this property, you can use a combination of static text and placeholder values to generate the final URL. The following code creates a representation for the entity that includes its unique ID:

```swift
struct MyAppData: AppEntity, URLRepresentableEntity {
    static let defaultQuery = MyAppDataQuery()

    @Property(title: "Content ID")
    var contentID: String

    static var urlRepresentation = URLRepresentation("https://example.com/note=\(.$contentID)")
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/urlrepresentableentity/urlrepresentation-swift.type.property)*