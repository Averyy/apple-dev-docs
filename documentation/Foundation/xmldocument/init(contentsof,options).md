# init(contentsOf:options:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes and returns an NSXMLDocument object created from the XML or HTML contents of a URL-referenced source

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
convenience init(contentsOf url: URL, options mask: XMLNode.Options = []) throws
```

```objc
- (instancetype) initWithContentsOfURL:(NSURL *) url options:(NSXMLNodeOptions) mask error:(NSError **) error;
```

#### Return Value

An initialized `NSXMLDocument` object, or  `nil` if initialization fails because of parsing errors or other reasons.

#### Discussion

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: An [`NSURL`](../nsurl.md) object specifying a URL source.
- `mask`: A bit mask for input options. You can specify multiple options by bit-OR’ing them. See Constants for a list of valid input options.

## See Also

### Related Documentation
- [Tree-Based XML Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/NSXML.html#//apple_ref/doc/uid/TP40001269)
### Initializing NSXMLDocument Objects
- [init(data: Data, options: XMLNode.Options) throws](./init%28data,options%29.md)
  Initializes and returns an `NSXMLDocument` object created from an [`NSData`](../nsdata.md) object.
- [init(rootElement: XMLElement?)](./init%28rootelement%29.md)
  Returns an `NSXMLDocument` object initialized with a single child, the root element.
- [convenience init(xmlString: String, options: XMLNode.Options) throws](./init%28xmlstring,options%29-65m2r.md)
  Initializes and returns an `NSXMLDocument` object created from a string containing XML markup text.
- [class func replacementClass(for: AnyClass) -> AnyClass](./replacementclass%28for%29.md)
  Overridden by subclasses to substitute a custom class for an NSXML class that the parser uses to create node instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/init(contentsof:options:))*