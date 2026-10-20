# suiteNames

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the names of the suite definitions currently loaded by the application.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var suiteNames: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * suiteNames;
```

## See Also

### Getting Suite Information
- [func suite(forAppleEventCode: FourCharCode) -> String?](./suite%28forappleeventcode%29.md)
  Returns the name of the suite definition associated with the given four-character Apple event code, `code`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/suitenames)*