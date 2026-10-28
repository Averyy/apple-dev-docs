# init(xmlString:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an `NSXMLElement` object created from a specified string containing XML markup.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(xmlString string: String) throws
```

```objc
- (instancetype) initWithXMLString:(NSString *) string error:(NSError **) error;
```

## Return Value

The initialized `NSXMLElement` object or `nil` if initialization did not succeed.

## Discussion

> **Handling Errors in Swift**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `string`: A string containing XML markup for an element.

## See Also

### Initializing NSXMLElement Objects
- [convenience init(name: String)](./init%28name%29.md)
  Returns an `NSXMLElement` object initialized with the specified name.
- [convenience init(name: String, stringValue: String?)](./init%28name,stringvalue%29.md)
  Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.
- [init(name: String, uri: String?)](./init%28name,uri%29-1r286.md)
  Returns an `NSXMLElement` object initialized with the specified name and URI.
- [convenience init(kind: XMLNode.Kind, options: XMLNode.Options)](./init%28kind,options%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/init(xmlstring:)-7vkg7)*