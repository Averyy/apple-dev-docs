# init(string:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an `NSScanner` object initialized to scan a given string.

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
init(string: String)
```

```objc
- (instancetype) initWithString:(NSString *) string;
```

#### Return Value

An `NSScanner` object initialized to scan `aString` from the beginning. The returned object might be different than the original receiver.

## Parameters

- `string`: The string to scan.

## See Also

### Creating a Scanner
- [class func localizedScanner(with: String) -> Any](./localizedscanner%28with%29.md)
  Returns an `NSScanner` object that scans a given string according to the user’s default locale.
### Related Documentation
- [+ scannerWithString:](../nsscanner/scannerwithstring_.md)
  Returns an `NSScanner` object that scans a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/init(string:))*