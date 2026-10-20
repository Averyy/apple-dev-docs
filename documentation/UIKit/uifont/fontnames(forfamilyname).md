# fontNames(forFamilyName:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns an array of font names available in a particular font family.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func fontNames(forFamilyName familyName: String) -> [String]
```

```objc
+ (NSArray<NSString *> *) fontNamesForFamilyName:(NSString *) familyName;
```

#### Return Value

An array of `NSString` objects, each of which contains a font name associated with the specified family.

#### Discussion

You can pass the returned strings as parameters to the [`init(name:size:)`](./init%28name,size%29.md) method to retrieve an actual font object.

## Parameters

- `familyName`: The name of the font family. Use the [`familyNames`](./familynames.md) method to get an array of the available font family names on the system.

## See Also

### Related Documentation
- [init?(name: String, size: CGFloat)](./init%28name,size%29.md)
  Creates and returns a font object for the specified font name and size.
### Getting the Available Font Names
- [class var familyNames: [String]](./familynames.md)
  Returns an array of font family names available on the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/fontnames(forfamilyname:))*