# delegate

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A delegate object that receives messages about the parsing process.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
unowned(unsafe) var delegate: (any XMLParserDelegate)? { get set }
```

```objc
@property (assign, nullable) id<NSXMLParserDelegate> delegate;
```

## Discussion

For methods to be implemented by the delegate, see [`XMLParserDelegate`](../xmlparserdelegate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/delegate)*