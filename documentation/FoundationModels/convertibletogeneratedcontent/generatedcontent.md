# generatedContent

**Framework**: Foundation Models  
**Kind**: property  
**Required**: Yes

This instance represented as generated content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var generatedContent: GeneratedContent { get }
```

#### Discussion

Conformance to this protocol is provided by the `@Generable` macro. A manual implementation may be used to map values onto properties using different names. Use the generated content property as shown below, to manually return a new [`GeneratedContent`](generatedcontent.md) with the properties you specify.

```swift
struct Person: ConvertibleToGeneratedContent {
   var name: String
   var age: Int

   var generatedContent: GeneratedContent {
       GeneratedContent(properties: [
           "firstName": name,
           "ageInYears": age
       ])
   }
}
```

> ❗ **Important**: If your type also conforms to [`ConvertibleFromGeneratedContent`](convertiblefromgeneratedcontent.md), it is critical that this implementation be symmetrical with [`init(_:)`](convertiblefromgeneratedcontent/init(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/convertibletogeneratedcontent/generatedcontent)*