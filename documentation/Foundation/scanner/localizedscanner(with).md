# localizedScanner(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an `NSScanner` object that scans a given string according to the user’s default locale.

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
class func localizedScanner(with string: String) -> Any
```

```objc
+ (id) localizedScannerWithString:(NSString *) string;
```

## Return Value

An `NSScanner` object that scans `aString` according to the user’s default locale.

## Discussion

Sets the string to scan by invoking [`init(string:)`](./init%28string%29.md) with `aString`. The locale is set with [`Scanner`](../scanner.md).

## Parameters

- `string`: The string to scan.

## See Also

### Creating a Scanner
- [init(string: String)](./init%28string%29.md)
  Returns an `NSScanner` object initialized to scan a given string.
- [+ scannerWithString:](../nsscanner/scannerwithstring_.md)
  Returns an `NSScanner` object that scans a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/localizedscanner(with:))*