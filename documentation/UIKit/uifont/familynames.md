# familyNames

**Framework**: UIKit  
**Kind**: property

Returns an array of font family names available on the system.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var familyNames: [String] { get }
```

#### Return Value

An array of `NSString` objects, each of which contains the name of a font family.

#### Discussion

Font family names correspond to the base name of a font, such as `Times New Roman`. You can pass the returned strings to the [`fontNames(forFamilyName:)`](uifont/fontnames(forfamilyname:).md) method to retrieve a list of font names available for that family. You can then use the corresponding font name to retrieve an actual font object.

## See Also

- [class func fontNames(forFamilyName: String) -> [String]](uifont/fontnames(forfamilyname:).md)
  Returns an array of font names available in a particular font family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/familynames)*