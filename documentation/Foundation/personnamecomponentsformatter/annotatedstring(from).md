# annotatedString(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an attributed string formatted for a given `NSPersonNameComponents` object, with attribute annotations for each component.

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
func annotatedString(from components: PersonNameComponents) -> NSAttributedString
```

```objc
- (NSAttributedString *) annotatedStringFromPersonNameComponents:(NSPersonNameComponents *) components;
```

## Return Value

An attributed string representation of the given name components. You can determine the person component corresponding to a particular range of the attributed string by querying the `NSPersonNameComponentKey` attribute, providing one of the `NSPersonNameComponent` constant values defined below as the attribute value.

## Discussion

Use this method to style individual components of a formatted name, such as a name in a label.

## Parameters

- `components`: A formatted string representation of the given name components.

## See Also

### Converting Between Person Name Components and Strings
- [class func localizedString(from: PersonNameComponents, style: PersonNameComponentsFormatter.Style, options: PersonNameComponentsFormatter.Options) -> String](./localizedstring%28from,style,options%29.md)
  Returns a string formatted for a given `NSPersonNameComponents` object using the provided style and options.
- [func string(from: PersonNameComponents) -> String](./string%28from%29.md)
  Returns a string formatted for a given `NSPersonNameComponents` object.
- [func personNameComponents(from: String) -> PersonNameComponents?](./personnamecomponents%28from%29.md)
  Returns a person name components object from a given string.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./getobjectvalue%28_,for,errordescription%29.md)
  Returns by reference a person name components object after creating it from a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/annotatedstring(from:))*