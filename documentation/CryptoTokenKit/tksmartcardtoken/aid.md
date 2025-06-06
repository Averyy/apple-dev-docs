# aid

**Framework**: CryptoTokenKit  
**Kind**: property

The ISO 7816-4 application identifiers of the Smart Card.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var aid: Data? { get }
```

#### Discussion

This value is specified in the Smart Card token extension’s `NSExtensionAttributes` property list by the `com.apple.ctk.aid` attribute. If this attribute specifies multiple AIDs, this parameter represents the application identifier found on the card that is already preselected.  If the `com.apple.ctk.aid` attribute is not present, no application is automatically preselected and the value of this property is `nil`.

For more information, see [`App Extension Keys`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AppExtensionKeys.html#//apple_ref/doc/uid/TP40014212) in [`Information Property List Key Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009247).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtoken/aid)*