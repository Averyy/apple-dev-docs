# localizedString(from:style:options:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

A formatted string representation of the given name components.

#### Discussion

This method is a convenience for formatting name components without creating an instance of `NSPersonNameComponentsFormatter`. For greater customizability, you can create an instance of `NSPersonNameComponentsFormatter` and use [`string(from:)`](personnamecomponentsformatter/string(from:).md) instead.

## Parameters

- `components`: The name components to be formatted.
- `nameFormatStyle`: A format style for the name components. For possible values, see  .
- `nameOptions`: The formatting options for the name components. For possible values, see  .

## See Also

- [func string(from: PersonNameComponents) -> String](personnamecomponentsformatter/string(from:).md)
  Returns a string formatted for a given `NSPersonNameComponents` object.
- [func annotatedString(from: PersonNameComponents) -> NSAttributedString](personnamecomponentsformatter/annotatedstring(from:).md)
  Returns an attributed string formatted for a given `NSPersonNameComponents` object, with attribute annotations for each component.
- [func personNameComponents(from: String) -> PersonNameComponents?](personnamecomponentsformatter/personnamecomponents(from:).md)
  Returns a person name components object from a given string.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](personnamecomponentsformatter/getobjectvalue(_:for:errordescription:).md)
  Returns by reference a person name components object after creating it from a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/localizedstring(from:style:options:))*