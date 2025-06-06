# presentationSectionIndex(forDataSourceSectionIndex:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Translates a section index in your data source object to the equivalent section index in your presented layout.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func presentationSectionIndex(forDataSourceSectionIndex dataSourceSectionIndex: Int) -> Int
```

#### Return Value

The index path of the same section in the presentation layer of your object, or `nil` if the section is not in the presentation layer.

## Parameters

- `dataSourceSectionIndex`: The index path of a section in the data source object.

## See Also

- [func dataSourceSectionIndex(forPresentationSectionIndex: Int) -> Int](uidatasourcetranslating/datasourcesectionindex(forpresentationsectionindex:).md)
  Translates a section index in your presented layout to the equivalent section index in your data source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatasourcetranslating/presentationsectionindex(fordatasourcesectionindex:))*