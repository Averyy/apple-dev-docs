# extendedTextInputTraits

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An object that customizes text-input appearance and behavior beyond the standard system traits.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var extendedTextInputTraits: (any BEExtendedTextInputTraits)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<BEExtendedTextInputTraits> extendedTextInputTraits;
```

## See Also

### Managing text traits
- [var isEditable: Bool](./iseditable.md)
  A Boolean value that determines the ability to modify text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/extendedtextinputtraits)*