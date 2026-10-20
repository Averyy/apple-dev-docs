# scanString(_:into:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Scans a given string, returning an equivalent string object by reference if a match is found.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
func scanString(_ string: String, into result: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

```objc
- (BOOL) scanString:(NSString *) string intoString:(NSString **) result;
```

#### Return Value

[`true`](../../Swift/true.md) if `string` matches the characters at the scan location, otherwise [`false`](../../Swift/false.md).

#### Discussion

If `string` is present at the current scan location, then the current scan location is advanced to after the string; otherwise the scan location does not change.

Invoke this method with `NULL` as `stringValue` to simply scan past a given string.

## Parameters

- `string`: The string for which to scan at the current scan location.
- `result`: Upon return, if the receiver contains a string equivalent to `string` at the current scan location, contains a string equivalent to `string`.

## See Also

### Scanning Characters and Strings
- [func scanCharacters(from: CharacterSet, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./scancharacters%28from,into%29.md)
  Scans the string as long as characters from a given character set are encountered, accumulating characters into a string that’s returned by reference.
- [func scanUpToCharacters(from: CharacterSet, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./scanuptocharacters%28from,into%29.md)
  Scans the string until a character from a given character set is encountered, accumulating characters into a string that’s returned by reference.
- [func scanUpTo(String, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./scanupto%28_,into%29.md)
  Scans the string until a given string is encountered, accumulating characters into a string that’s returned by reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/scanstring(_:into:))*