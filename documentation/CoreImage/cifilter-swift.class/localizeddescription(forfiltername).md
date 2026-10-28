# localizedDescription(forFilterName:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Returns the localized description of a filter for display in the user interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func localizedDescription(forFilterName filterName: String) -> String?
```

```objc
+ (NSString *) localizedDescriptionForFilterName:(NSString *) filterName;
```

## Return Value

The localized description of the filter.

## Parameters

- `filterName`: The filter name.

## See Also

### Getting localized information for registered filters
- [class func localizedName(forFilterName: String) -> String?](./localizedname%28forfiltername%29.md)
  Returns the localized name for the specified filter name.
- [class func localizedName(forCategory: String) -> String](./localizedname%28forcategory%29.md)
  Returns  the localized name for the specified filter category.
- [class func localizedReferenceDocumentation(forFilterName: String) -> URL?](./localizedreferencedocumentation%28forfiltername%29.md)
  Returns the location of the localized reference documentation that describes the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/localizeddescription(forfiltername:))*