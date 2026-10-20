# string(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a string formatted for a given `NSPersonNameComponents` object.

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
func string(from components: PersonNameComponents) -> String
```

```objc
- (NSString *) stringFromPersonNameComponents:(NSPersonNameComponents *) components;
```

#### Return Value

A formatted string representation of the given name components.

## Parameters

- `components`: The name components to be formatted.

## See Also

### Converting Between Person Name Components and Strings
- [class func localizedString(from: PersonNameComponents, style: PersonNameComponentsFormatter.Style, options: PersonNameComponentsFormatter.Options) -> String](./localizedstring%28from,style,options%29.md)
  Returns a string formatted for a given `NSPersonNameComponents` object using the provided style and options.
- [func annotatedString(from: PersonNameComponents) -> NSAttributedString](./annotatedstring%28from%29.md)
  Returns an attributed string formatted for a given `NSPersonNameComponents` object, with attribute annotations for each component.
- [func personNameComponents(from: String) -> PersonNameComponents?](./personnamecomponents%28from%29.md)
  Returns a person name components object from a given string.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./getobjectvalue%28_,for,errordescription%29.md)
  Returns by reference a person name components object after creating it from a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/string(from:))*