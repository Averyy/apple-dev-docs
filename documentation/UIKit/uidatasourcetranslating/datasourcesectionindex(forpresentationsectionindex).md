# dataSourceSectionIndex(forPresentationSectionIndex:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Translates a section index in your presented layout to the equivalent section index in your data source object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func dataSourceSectionIndex(forPresentationSectionIndex presentationSectionIndex: Int) -> Int
```

```objc
- (NSInteger) dataSourceSectionIndexForPresentationSectionIndex:(NSInteger) presentationSectionIndex;
```

#### Return Value

The index path of the same section in the data source object, or `nil` if the section is no longer in the data source.

## Parameters

- `presentationSectionIndex`: The index path of a section in your presentation layer.

## See Also

### Managing section positions
- [func presentationSectionIndex(forDataSourceSectionIndex: Int) -> Int](./presentationsectionindex%28fordatasourcesectionindex%29.md)
  Translates a section index in your data source object to the equivalent section index in your presented layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatasourcetranslating/datasourcesectionindex(forpresentationsectionindex:))*