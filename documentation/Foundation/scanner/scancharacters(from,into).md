# scanCharacters(from:into:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Scans the string as long as characters from a given character set are encountered, accumulating characters into a string that’s returned by reference.

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
func scanCharacters(from set: CharacterSet, into result: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

```objc
- (BOOL) scanCharactersFromSet:(NSCharacterSet *) set intoString:(NSString **) result;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver scanned any characters, otherwise [`false`](../../Swift/false.md).

#### Discussion

Invoke this method with `NULL` as `stringValue` to simply scan past a given set of characters.

## Parameters

- `set`: The set of characters to scan.
- `result`: Upon return, contains the characters scanned.

## See Also

### Scanning Characters and Strings
- [func scanUpToCharacters(from: CharacterSet, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./scanuptocharacters%28from,into%29.md)
  Scans the string until a character from a given character set is encountered, accumulating characters into a string that’s returned by reference.
- [func scanString(String, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./scanstring%28_,into%29.md)
  Scans a given string, returning an equivalent string object by reference if a match is found.
- [func scanUpTo(String, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./scanupto%28_,into%29.md)
  Scans the string until a given string is encountered, accumulating characters into a string that’s returned by reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/scancharacters(from:into:))*