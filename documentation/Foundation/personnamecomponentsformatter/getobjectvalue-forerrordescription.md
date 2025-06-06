# getObjectValue(_:for:errorDescription:)

**Framework**: Foundation  
**Kind**: method

Returns by reference a person name components object after creating it from a given string.

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
func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>?, for string: String, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if conversion succeeded; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `obj`: On return, contains an instance of  , or   if conversion failed.
- `string`: A string that is parsed to create a person name components object.
- `error`: If an error occurs, upon return contains an   object in the   with code   that explains why the conversion failed. If you pass in   for error, you are indicating that you are not interested in error information.

## See Also

- [class func localizedString(from: PersonNameComponents, style: PersonNameComponentsFormatter.Style, options: PersonNameComponentsFormatter.Options) -> String](personnamecomponentsformatter/localizedstring(from:style:options:).md)
  Returns a string formatted for a given `NSPersonNameComponents` object using the provided style and options.
- [func string(from: PersonNameComponents) -> String](personnamecomponentsformatter/string(from:).md)
  Returns a string formatted for a given `NSPersonNameComponents` object.
- [func annotatedString(from: PersonNameComponents) -> NSAttributedString](personnamecomponentsformatter/annotatedstring(from:).md)
  Returns an attributed string formatted for a given `NSPersonNameComponents` object, with attribute annotations for each component.
- [func personNameComponents(from: String) -> PersonNameComponents?](personnamecomponentsformatter/personnamecomponents(from:).md)
  Returns a person name components object from a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/getobjectvalue(_:for:errordescription:))*