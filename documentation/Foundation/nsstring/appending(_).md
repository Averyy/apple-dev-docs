# appending(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a new string made by appending a given string to the receiver.

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
func appending(_ aString: String) -> String
```

```objc
- (NSString *) stringByAppendingString:(NSString *) aString;
```

#### Return Value

A new string made by appending `aString` to the receiver.

#### Discussion

This code excerpt, for example:

```objc
NSString *errorTag = @"Error: ";
NSString *errorString = @"premature end of file.";
NSString *errorMessage = [errorTag stringByAppendingString:errorString];
```

produces the string “`Error: premature end of file.`”.

## Parameters

- `aString`: The string to append to the receiver. This value must not be `nil`.

  > ❗ **Important**:  Raises an `NSInvalidArgumentException` if `aString` is `nil`.

## See Also

### Combining Strings
- [func appendingFormat(NSString, any CVarArg...) -> NSString](./appendingformat%28_,_%29.md)
- [func padding(toLength: Int, withPad: String, startingAt: Int) -> String](./padding%28tolength,withpad,startingat%29.md)
  Returns a new string formed from the receiver by either removing characters from the end, or by appending as many occurrences as necessary of a given pad string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/appending(_:))*