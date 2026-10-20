# suite(forAppleEventCode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the name of the suite definition associated with the given four-character Apple event code, `code`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func suite(forAppleEventCode appleEventCode: FourCharCode) -> String?
```

```objc
- (NSString *) suiteForAppleEventCode:(FourCharCode) appleEventCode;
```

## See Also

### Getting Suite Information
- [var suiteNames: [String]](./suitenames.md)
  Returns the names of the suite definitions currently loaded by the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/suite(forappleeventcode:))*