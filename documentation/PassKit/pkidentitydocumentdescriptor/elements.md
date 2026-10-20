# elements

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A list of identity elements to request.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var elements: [PKIdentityElement] { get }
```

```objc
@property (nonatomic, readonly) NSArray<PKIdentityElement *> * elements;
```

## See Also

### Inspecting elements
- [var issuerIdentifiers: [Data]](./issueridentifiers.md)
  A list of X.509 authority key identifiers your app accepts.
- [class PKIdentityElement](../pkidentityelement.md)
  An object that represents the elements an app requests from identity documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitydocumentdescriptor/elements)*