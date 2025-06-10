# objectByApplyingXSLT(at:arguments:)

**Framework**: Foundation  
**Kind**: method

Applies the XSLT pattern rules and templates located at a specified URL to the receiver and returns a document object containing transformed XML markup or an [`NSData`](nsdata.md) object containing plain text, RTF text, and so on.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func objectByApplyingXSLT(at xsltURL: URL, arguments argument: [String : String]?) throws -> Any
```

#### Return Value

Depending on intended output, the returns an `NSXMLDocument` object  an [`NSData`](nsdata.md) data containing transformed XML or HTML markup. If the message is supposed to create plain text or RTF, then an `NSData` object is returned, otherwise an XML document object. The method returns  `nil` if XSLT processing did not succeed.

#### Discussion

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `xsltURL`: An   object specifying a valid URL.
- `argument`: A dictionary containing   key-value pairs that are passed as runtime parameters to the XSLT processor. Pass in   if you have no parameters to pass.

## See Also

- [func object(byApplyingXSLT: Data, arguments: [String : String]?) throws -> Any](xmldocument/object(byapplyingxslt:arguments:).md)
  Applies the XSLT pattern rules and templates (specified as a data object) to the receiver and returns a document object containing transformed XML or HTML markup.
- [func object(byApplyingXSLTString: String, arguments: [String : String]?) throws -> Any](xmldocument/object(byapplyingxsltstring:arguments:).md)
  Applies the XSLT pattern rules and templates (specified as a string) to the receiver and returns a document object containing transformed XML or HTML markup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/objectbyapplyingxslt(at:arguments:))*