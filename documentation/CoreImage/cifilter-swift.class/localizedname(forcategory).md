# localizedName(forCategory:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Returns  the localized name for the specified filter category.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func localizedName(forCategory category: String) -> String
```

```objc
+ (NSString *) localizedNameForCategory:(NSString *) category;
```

#### Return Value

The localized name for the filter category.

## Parameters

- `category`: A filter category.

## See Also

### Getting localized information for registered filters
- [class func localizedName(forFilterName: String) -> String?](./localizedname%28forfiltername%29.md)
  Returns the localized name for the specified filter name.
- [class func localizedDescription(forFilterName: String) -> String?](./localizeddescription%28forfiltername%29.md)
  Returns the localized description of a filter for display in the user interface.
- [class func localizedReferenceDocumentation(forFilterName: String) -> URL?](./localizedreferencedocumentation%28forfiltername%29.md)
  Returns the location of the localized reference documentation that describes the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/localizedname(forcategory:))*