# getObjectValue(_:for:errorDescription:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) getObjectValue:(id*) obj forString:(NSString *) string errorDescription:(NSString **) error;
```

## Return Value

[`true`](../../Swift/true.md) if conversion succeeded; otherwise [`false`](../../Swift/false.md).

## Parameters

- `obj`: On return, contains an instance of [`NSPersonNameComponents`](../nspersonnamecomponents.md), or `nil` if conversion failed.
- `string`: A string that is parsed to create a person name components object.
- `error`: If an error occurs, upon return contains an [`NSError`](../nserror.md) object in the [`NSCocoaErrorDomain`](../nscocoaerrordomain.md) with code [`NSFormattingError`](../nsformattingerror-swift.var.md) that explains why the conversion failed. If you pass in `nil` for error, you are indicating that you are not interested in error information.

## See Also

### Converting Between Person Name Components and Strings
- [class func localizedString(from: PersonNameComponents, style: PersonNameComponentsFormatter.Style, options: PersonNameComponentsFormatter.Options) -> String](./localizedstring%28from,style,options%29.md)
  Returns a string formatted for a given `NSPersonNameComponents` object using the provided style and options.
- [func string(from: PersonNameComponents) -> String](./string%28from%29.md)
  Returns a string formatted for a given `NSPersonNameComponents` object.
- [func annotatedString(from: PersonNameComponents) -> NSAttributedString](./annotatedstring%28from%29.md)
  Returns an attributed string formatted for a given `NSPersonNameComponents` object, with attribute annotations for each component.
- [func personNameComponents(from: String) -> PersonNameComponents?](./personnamecomponents%28from%29.md)
  Returns a person name components object from a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/getobjectvalue(_:for:errordescription:))*