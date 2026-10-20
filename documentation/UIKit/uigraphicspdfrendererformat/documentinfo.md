# documentInfo

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A dictionary that specifies additional information to be associated with the PDFs created by the PDF renderer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var documentInfo: [String : Any] { get set }
```

```objc
@property (nonatomic, copy) NSDictionary<NSString *,id> * documentInfo;
```

#### Discussion

You can use these keys to specify additional metadata and security information for the PDF, such as the author or the password for accessing it.

The keys used in this dictionary are described in  [Auxiliary Dictionary Keys](../../CoreGraphics/auxiliary-dictionary-keys.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrendererformat/documentinfo)*