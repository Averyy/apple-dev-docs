# localizedString(from:style:options:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a string formatted for a given `NSPersonNameComponents` object using the provided style and options.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func localizedString(from components: PersonNameComponents, style nameFormatStyle: PersonNameComponentsFormatter.Style, options nameOptions: PersonNameComponentsFormatter.Options = []) -> String
```

```objc
+ (NSString *) localizedStringFromPersonNameComponents:(NSPersonNameComponents *) components style:(NSPersonNameComponentsFormatterStyle) nameFormatStyle options:(NSPersonNameComponentsFormatterOptions) nameOptions;
```

## Return Value

A formatted string representation of the given name components.

## Discussion

This method is a convenience for formatting name components without creating an instance of `NSPersonNameComponentsFormatter`. For greater customizability, you can create an instance of `NSPersonNameComponentsFormatter` and use [`string(from:)`](./string%28from%29.md) instead.

## Parameters

- `components`: The name components to be formatted.
- `nameFormatStyle`: A format style for the name components. For possible values, see [`PersonNameComponentsFormatter.Style`](./style-swift.enum.md).
- `nameOptions`: The formatting options for the name components. For possible values, see [`PersonNameComponentsFormatter.Options`](./options.md).

## See Also

### Converting Between Person Name Components and Strings
- [func string(from: PersonNameComponents) -> String](./string%28from%29.md)
  Returns a string formatted for a given `NSPersonNameComponents` object.
- [func annotatedString(from: PersonNameComponents) -> NSAttributedString](./annotatedstring%28from%29.md)
  Returns an attributed string formatted for a given `NSPersonNameComponents` object, with attribute annotations for each component.
- [func personNameComponents(from: String) -> PersonNameComponents?](./personnamecomponents%28from%29.md)
  Returns a person name components object from a given string.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./getobjectvalue%28_,for,errordescription%29.md)
  Returns by reference a person name components object after creating it from a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/localizedstring(from:style:options:))*