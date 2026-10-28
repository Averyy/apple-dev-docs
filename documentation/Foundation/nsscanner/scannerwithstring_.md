# scannerWithString:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an `NSScanner` object that scans a given string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) scannerWithString:(NSString *) string;
```

## Return Value

An `NSScanner` object that scans `aString`.

## Discussion

Sets the string to scan by invoking [`init(string:)`](../scanner/init%28string%29.md) with `aString`.

## Parameters

- `string`: The string to scan.

## See Also

### Related Documentation
- [String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i)
### Creating a Scanner
- [class func localizedScanner(with: String) -> Any](../scanner/localizedscanner%28with%29.md)
  Returns an `NSScanner` object that scans a given string according to the user’s default locale.
- [init(string: String)](../scanner/init%28string%29.md)
  Returns an `NSScanner` object initialized to scan a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscanner/scannerwithstring:)*