# CGPDFDictionaryApplierFunction

**Framework**: Core Graphics  
**Kind**: typealias

Performs custom processing on a key-value pair from a PDF dictionary, using optional contextual information.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias CGPDFDictionaryApplierFunction = (UnsafePointer<CChar>, CGPDFObjectRef, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

[`CGPDFDictionaryApplierFunction`](cgpdfdictionaryapplierfunction.md) defines the callback for [`CGPDFDictionaryApplyFunction(_:_:_:)`](cgpdfdictionaryapplyfunction(_:_:_:).md), that enumerates all of the entries in the dictionary, calling your custom applier function once for each entry. The current key, its associated value, and the contextual information are passed to your applier function using the `key`, `value`, and `info` parameters respectively.

## Parameters

- `key`: The current key in the dictionary.
- `object`: The value in the dictionary associated with the key.
- `info`: The contextual information that your provided in the   parameter in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdictionaryapplierfunction)*