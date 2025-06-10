# init(properties:)

**Framework**: Foundation Models  
**Kind**: init

Creates an object with the properties you specify.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(properties: KeyValuePairs<String, any ConvertibleToGeneratedContent>)
```

#### Discussion

The order of properties is important. For [`Generable`](generable.md) types, the order must match the order properties in the types `schema`.

## See Also

- [init(_:)](generatedcontent/init(_:).md)
  Creates an object with the content you specify.
- [init<C>(elements: C)](generatedcontent/init(elements:).md)
  Creates an object with an array of elements you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/init(properties:))*