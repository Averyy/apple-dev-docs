# allowedInputSourceLocales

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of locale identifiers that represent the allowed input sources when the text field has the keyboard focus.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var allowedInputSourceLocales: [String]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSString *> * allowedInputSourceLocales;
```

## Discussion

The value of this property is an array of [`NSString`](../../Foundation/nsstring.md) objects, each of which contains a locale identifier. You can assign the meta-locale identifier, [`NSAllRomanInputSourcesLocaleIdentifier`](../nsallromaninputsourceslocaleidentifier.md), to specify input sources that are limited for Roman script editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfieldcell/allowedinputsourcelocales)*